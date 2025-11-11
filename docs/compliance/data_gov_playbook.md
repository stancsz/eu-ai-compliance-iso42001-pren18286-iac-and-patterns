# Data Governance Playbook (EU AI Act Art. 10)

## Objectives

- Ensure datasets used by AWS Bedrock and GCP Vertex AI workloads are relevant, representative, and documented.
- Maintain lawful basis, usage rights, and lineage for all data processing activities.

## Governance Roles

| Role | Responsibilities | Evidence |
|------|------------------|----------|
| Data Steward | Maintain data inventory & datasheets | Data inventory link |
| Privacy Officer | Approve lawful basis & DPIA | DPIA reference |
| ML Engineer | Conduct bias assessments & validation | Bias report link |

## Data Lifecycle Controls

1. **Collection** — Document source, consent, legal basis.
2. **Preparation** — Record preprocessing steps, bias mitigation strategies.
3. **Validation** — Run statistical tests, fairness checks, security scans.
4. **Deployment** — Enforce access controls, monitor drift, capture audit logs.
5. **Retention & Disposal** — Apply retention policies, document anonymization/deletion.

## Datasheet Template

| Field | Description |
|-------|-------------|
| Dataset Name | |
| Purpose of Use | |
| Source Systems | |
| Preprocessing Pipeline | |
| Bias Assessment Summary | |
| Quality Metrics | |
| Retention Policy | |
| Last Review Date | |

## Monitoring & Alerts

- Drift metrics ingested via OpenTelemetry.
- Automated alerts for missing datasheets or expired reviews.
- Integration with PMM process for continuous improvement.
