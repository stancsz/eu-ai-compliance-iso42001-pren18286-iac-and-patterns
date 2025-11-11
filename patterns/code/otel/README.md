# OpenTelemetry Code Patterns

This folder demonstrates how to instrument AI services and pipelines with OpenTelemetry (OTel) to satisfy EU AI Act Art. 12 (logging & traceability) and ISO 42001 monitoring obligations.

## Contents

- `python_inference_example.py` — Bedrock inference wrapper with structured tracing.
- `vertex_pipeline_instrumentation.md` — Guidance for instrumenting Vertex AI pipelines.
- `otel_schema.yaml` — Canonical schema for AI compliance events.

## Implementation Guidance

- Record `aims_control_id`, `eu_ai_act_article`, and `risk_level` attributes in spans/events.
- Emit override decisions, data lineage checks, and PMM metrics as telemetry events.
- Ship telemetry to centralized collector with enforced retention policies.

> Replace placeholders with production-ready code and integrate with your collector (e.g., AWS Distro for OpenTelemetry, Google Cloud Ops Agent).
