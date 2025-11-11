# Post-Market Monitoring Plan (EU AI Act Art. 72, ISO 42001 Cl. 9.1)

## Purpose

Define how post-deployment monitoring is conducted for AWS Bedrock and GCP Vertex AI workloads, ensuring early detection of performance degradation, safety issues, or rights impacts.

## Governance

- **Owner:** 
- **Participants:** Product, ML Engineering, Compliance, Risk, Support.
- **Meeting Cadence:** (e.g., monthly review, quarterly management report).

## Data Sources

- OpenTelemetry metrics and traces (latency, drift, overrides).
- Customer feedback and complaints.
- Incident response records.
- Security findings (AWS Security Hub, GCP SCC).

## Workflow

1. Collect telemetry and compile PMM dashboard.
2. Review anomalies against risk thresholds.
3. Document incidents and corrective actions.
4. Update risk register and technical documentation.
5. Escalate mandatory notifications (EU AI Act Art. 62) when required.

## Reporting

- Generate PMM report using `templates/pmm_report_template.md`.
- Store approved reports in controlled repository with versioning.
- Present key findings during ISO 42001 management review.

## Evidence

- Signed PMM reports.
- List of corrective actions with status.
- Notifications sent to authorities/regulators (if applicable).
