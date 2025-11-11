# Vertex AI Pipeline Instrumentation

## Goal

Capture end-to-end telemetry for Vertex AI pipelines (training, batch prediction, evaluation) with OpenTelemetry to meet EU AI Act logging and ISO 42001 monitoring obligations.

## Steps

1. **Collector Setup**
   - Deploy OpenTelemetry Collector on GKE or Cloud Run.
   - Configure exporters to Cloud Logging, BigQuery, and SIEM.
2. **Pipeline Instrumentation**
   - Inject tracing logic into custom pipeline components using `opentelemetry-sdk`.
   - Propagate context via environment variables and metadata.
   - Emit spans for:
     - Data ingestion (`component: load_data`)
     - Feature engineering (`component: preprocess`)
     - Training (`component: train_model`)
     - Evaluation (`component: evaluate`)
     - Deployment (`component: deploy_endpoint`)
3. **Compliance Metadata**
   - Set attributes: `aims_control_id`, `eu_ai_act_article`, `dataset_id`, `model_card_version`.
   - Log validation metrics and bias assessments as span events.
4. **Alerts & Dashboards**
   - Create logs-based metrics for drift, anomalies, override rates.
   - Integrate alerts with PMM process (`patterns/usage/post_market_monitoring.md`).

## Evidence

- Store pipeline run IDs with trace IDs in `templates/run_trace_log.csv`.
- Attach OTel dashboards to technical documentation packages.
- Include instrumentation design in PRDs and change records.
