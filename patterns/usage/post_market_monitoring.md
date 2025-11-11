# Post-Market Monitoring (PMM) Pattern

## Objectives

- Continuously evaluate AI system performance, safety, and rights impact after deployment.
- Feed insights back into risk management, data governance, and change management processes.

## Cadence

- **Weekly:** Automated metric review (accuracy, drift, latency, complaint volume).
- **Monthly:** Cross-functional PMM meeting (Product, Compliance, Risk, Ops).
- **Quarterly:** Management review per ISO 42001.

## Inputs

- Model performance dashboards (bedrock, vertex ai)
- Incident and complaint logs
- Human override statistics
- Data quality alerts (bias, drift)

## Activities

1. Collect telemetry from OpenTelemetry pipelines (`patterns/code/otel/`) and consolidate in PMM dashboard.
2. Review outstanding incidents; validate containment and corrective actions.
3. Update risk register entries with new residual risk assessments.
4. Determine if retraining, feature changes, or decommissioning is required.
5. Document decisions and assign action owners with target dates.

## Outputs & Evidence

- PMM report stored in `templates/pmm_report_template.md` with links to supporting evidence.
- Updated risk register entries (`templates/risk_register.csv`).
- Change tickets for remediation actions.
- Notification to competent authorities if serious incidents identified (per EU AI Act Art. 62).
