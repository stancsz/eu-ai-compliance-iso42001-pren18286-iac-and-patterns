# Logging & Monitoring Plan (EU AI Act Art. 12, ISO 42001 Cl. 9.1)

## Scope

- AWS Bedrock services (list endpoints).
- GCP Vertex AI services (list endpoints/pipelines).
- Supporting services (data pipelines, human oversight UI).

## Logging Requirements

| Log Type | Source | Retention | Storage Location | Owner |
|----------|--------|-----------|------------------|-------|
| Inference Requests | Bedrock Invoke API | 2 years | S3 Audit Bucket (immutable) | Platform Ops |
| Pipeline Execution | Vertex AI Pipelines | 2 years | Cloud Logging + BigQuery | ML Engineer |
| Human Overrides | Oversight UI | 2 years | SIEM | Compliance |
| Security Events | AWS/GCP native | 7 years | Central SIEM | Security |

## Monitoring & Alerting

- Critical alerts routed to on-call SOC within 5 minutes.
- Drift detection thresholds defined and reviewed quarterly.
- Override rate anomalies trigger PMM escalation.

## OpenTelemetry Integration

- Utilize `patterns/code/otel` schema for trace attributes.
- Collectors deployed in each environment with TLS/mTLS enabled.
- Exporters: AWS OTEL -> CloudWatch/S3, GCP OTEL -> Cloud Logging/BigQuery.

## Evidence Management

- Document log integrity checks (hashing, retention verification).
- Record alert tests and outcomes in `templates/alert_test_log.csv`.
- Link dashboards to management review minutes.
