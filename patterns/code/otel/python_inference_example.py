"""
Example: Instrumented AWS Bedrock inference call with OpenTelemetry.

Replace placeholders with production code and integrate with your telemetry backend.
"""

from contextlib import contextmanager
from datetime import datetime
from typing import Any, Dict

from opentelemetry import trace
from opentelemetry.trace import Span

# Placeholder Bedrock client import; replace with boto3 or AWS SDK call
# from my_bedrock_client import invoke_model

tracer = trace.get_tracer(__name__)


@contextmanager
def compliance_span(name: str, attributes: Dict[str, Any]) -> Span:
    """Utility context manager wrapping OTel spans with compliance metadata."""
    with tracer.start_as_current_span(name) as span:
        span.set_attribute("aims_control_id", attributes.get("aims_control_id"))
        span.set_attribute("eu_ai_act_article", attributes.get("eu_ai_act_article"))
        span.set_attribute("risk_level", attributes.get("risk_level"))
        span.set_attribute("model_version", attributes.get("model_version"))
        span.set_attribute("intended_use", attributes.get("intended_use"))
        yield span
        span.set_attribute("compliance.timestamp", datetime.utcnow().isoformat() + "Z")


def run_inference(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Wrap AWS Bedrock inference request with compliance telemetry.

    Args:
        payload: Input parameters for the model invocation.

    Returns:
        Dict containing the model response.
    """
    compliance_context = {
        "aims_control_id": "LOG-12",
        "eu_ai_act_article": "Art12",
        "risk_level": "high",
        "model_version": payload.get("model_version", "unknown"),
        "intended_use": payload.get("intended_use", "unspecified"),
    }

    with compliance_span("bedrock.invoke", compliance_context) as span:
        span.add_event(
            "input_received",
            attributes={
                "payload_hash": payload.get("payload_hash"),
                "user_context": payload.get("user_context"),
                "purpose_of_use": payload.get("purpose_of_use"),
            },
        )

        # response = invoke_model(payload)  # TODO: integrate with Bedrock SDK
        response = {"status": "placeholder", "body": "..."}  # Replace in implementation

        span.add_event(
            "model_response",
            attributes={
                "response_code": response.get("status"),
                "latency_ms": response.get("latency_ms"),
                "override_required": response.get("override_required", False),
            },
        )

        return response


if __name__ == "__main__":
    # Example invocation; remove in production.
    sample_payload = {
        "model_version": "v1.3.0",
        "payload_hash": "sha256:...",
        "user_context": "analyst_portal",
        "purpose_of_use": "customer_support",
    }
    run_inference(sample_payload)
