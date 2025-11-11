"""
patterns.usage.usage_examples
Concrete Python examples for:
- metadata extraction / modeling
- usage logging (structured)
- monitoring (Prometheus + optional OpenTelemetry hooks)
- simple data-lineage recording

Drop-in examples; adapt sinks (file/db/observability) to your infra.
"""

from dataclasses import dataclass, asdict
from datetime import datetime
import json
import logging
import os
import time
import uuid
from typing import Any, Dict, List, Optional

# ---------- Metadata ----------

@dataclass
class ModelMetadata:
    name: str
    version: str
    framework: str
    input_schema: Dict[str, Any]
    output_schema: Dict[str, Any]
    created_at: str
    tags: List[str]

    @classmethod
    def from_model_obj(cls, model_obj: Any) -> "ModelMetadata":
        """
        Example metadata extractor. Replace attribute reads with your model's API.
        """
        return cls(
            name=getattr(model_obj, "name", "unknown-model"),
            version=getattr(model_obj, "version", "0.0.0"),
            framework=getattr(model_obj, "framework", "unknown-framework"),
            input_schema=getattr(model_obj, "input_schema", {"type": "unknown"}),
            output_schema=getattr(model_obj, "output_schema", {"type": "unknown"}),
            created_at=getattr(model_obj, "created_at", datetime.utcnow().isoformat()),
            tags=getattr(model_obj, "tags", []),
        )

    def to_json(self) -> str:
        return json.dumps(asdict(self), indent=None)


# ---------- Usage Logging (structured) ----------

logger = logging.getLogger("patterns.usage")
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler()
    fmt = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(fmt)
    logger.addHandler(handler)

class UsageRecorder:
    """
    Records individual usage events in structured logs and persists to a local jsonl file.
    Replace or extend persistence with desired telemetry sink.
    """
    def __init__(self, out_path: str = "patterns/usage/usage_events.jsonl"):
        self.out_path = out_path
        os.makedirs(os.path.dirname(self.out_path), exist_ok=True)

    def record(
        self,
        model_meta: ModelMetadata,
        input_summary: Dict[str, Any],
        output_summary: Dict[str, Any],
        user_id: Optional[str],
        latency_ms: float,
        tags: Optional[List[str]] = None,
    ):
        event = {
            "id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat(),
            "model": asdict(model_meta),
            "input": input_summary,
            "output": output_summary,
            "user_id": user_id,
            "latency_ms": latency_ms,
            "tags": tags or [],
        }
        # Structured log line
        logger.info("usage_event %s", json.dumps(event, separators=(",", ":")))
        # Persist to file (append JSON-lines)
        with open(self.out_path, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(event) + "\n")


# ---------- Monitoring (Prometheus + optional OpenTelemetry) ----------

# Lightweight Prometheus example. In production, expose metrics on a dedicated endpoint.
try:
    from prometheus_client import Counter, Histogram, start_http_server

    REQUEST_COUNT = Counter("model_requests_total", "Total model requests", ["model_name", "status"])
    REQUEST_LATENCY = Histogram("model_request_latency_seconds", "Model request latency seconds", ["model_name"])

    def start_metrics_server(port: int = 8000):
        """Starts Prometheus metrics HTTP server on the given port (blocking in some setups)."""
        start_http_server(port)

    def instrument_request(model_name: str, latency_s: float, status: str = "ok"):
        REQUEST_COUNT.labels(model_name=model_name, status=status).inc()
        REQUEST_LATENCY.labels(model_name=model_name).observe(latency_s)
except Exception:
    # No prometheus installed; provide no-op fallbacks
    def start_metrics_server(port: int = 8000):
        logger.info("prometheus_client not installed; metrics server not started")

    def instrument_request(model_name: str, latency_s: float, status: str = "ok"):
        pass


# Optional: OpenTelemetry metrics / traces stub (illustrative only)
try:
    from opentelemetry import trace
    from opentelemetry.trace import TracerProvider
    from opentelemetry.sdk.trace import TracerProvider as SDKTracerProvider
    from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter

    tracer_provider = SDKTracerProvider()
    tracer_provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))
    trace.set_tracer_provider(tracer_provider)
    tracer = trace.get_tracer(__name__)

    def traced_inference(name: str):
        """Context manager for tracing an inference step."""
        return tracer.start_as_current_span(f"inference.{name}")

except Exception:
    # No-op if OpenTelemetry not installed
    from contextlib import nullcontext
    def traced_inference(name: str):
        return nullcontext()


# ---------- Data Lineage ----------

class LineageRecorder:
    """
    Record simple lineage events to a jsonl file. Replace sink with your data lineage system (e.g., Data Catalog).
    """
    def __init__(self, out_path: str = "patterns/usage/lineage_events.jsonl"):
        self.out_path = out_path
        os.makedirs(os.path.dirname(self.out_path), exist_ok=True)

    def record(self, event_type: str, resource: str, inputs: Dict[str, Any], outputs: Dict[str, Any], actor: Optional[str] = None):
        payload = {
            "id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat(),
            "event_type": event_type,
            "resource": resource,
            "inputs": inputs,
            "outputs": outputs,
            "actor": actor,
        }
        with open(self.out_path, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(payload) + "\n")
        logger.info("lineage_event %s", json.dumps({"id": payload["id"], "resource": resource, "event_type": event_type}))


# ---------- Example usage flow ----------

def example_inference_flow(model_obj: Any, user_id: Optional[str] = None):
    """
    Simulates an inference request path tying together metadata, usage recording, monitoring, lineage, and tracing.
    """
    # metadata
    meta = ModelMetadata.from_model_obj(model_obj)
    logger.info("model_metadata %s", meta.to_json())

    # instantiate recorders
    usage_recorder = UsageRecorder()
    lineage_recorder = LineageRecorder()

    # simulate request
    sample_input = {"text": "When was the golden gate bridge opened?"}
    start = time.time()
    with traced_inference(meta.name):
        # Replace with actual model invocation, e.g., model_obj.predict(sample_input)
        time.sleep(0.05)  # simulate latency
        sample_output = {"answer": "May 27, 1937", "confidence": 0.98}
    latency_s = time.time() - start

    # monitoring
    instrument_request(model_name=meta.name, latency_s=latency_s, status="ok")

    # usage logging
    usage_recorder.record(
        model_meta=meta,
        input_summary={"tokens": 7, "input_preview": sample_input["text"][:128]},
        output_summary={"answer_length": len(sample_output["answer"])},
        user_id=user_id,
        latency_ms=latency_s * 1000,
        tags=["qa", "example"],
    )

    # data lineage
    lineage_recorder.record(
        event_type="inference",
        resource=f"model:{meta.name}:{meta.version}",
        inputs={"prompt": sample_input},
        outputs={"response": sample_output},
        actor=user_id,
    )

    return sample_output


# ---------- Minimal model object for tests / examples ----------

class DummyModel:
    def __init__(self):
        self.name = "dummy-qa-model"
        self.version = "0.1.0"
        self.framework = "custom"
        self.input_schema = {"type": "text"}
        self.output_schema = {"type": "text"}
        self.created_at = datetime.utcnow().isoformat()
        self.tags = ["example", "test"]

    def predict(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        return {"answer": "dummy", "confidence": 0.5}


# ---------- If run as script, show quick demo ----------

if __name__ == "__main__":
    # Optional: start_metrics_server(8000)  # run in background/process in real deployments
    m = DummyModel()
    out = example_inference_flow(m, user_id="user:alice")
    print("demo output:", out)
