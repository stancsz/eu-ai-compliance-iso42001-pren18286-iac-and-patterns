# Human Oversight Runbook (HITL/HOTL)

## Purpose

Define how human operators supervise AWS Bedrock and GCP Vertex AI systems, including override mechanisms, escalation paths, and evidence capture, to satisfy EU AI Act Art. 14 and ISO 42001 oversight requirements.

## Scope

- Bedrock use cases: (e.g., customer support copilot, content moderation)
- Vertex AI use cases: (e.g., document classification, risk scoring)

## Roles & Responsibilities

| Role | Responsibilities | Backup | Evidence |
|------|------------------|--------|----------|
| Human Supervisor | Review model outputs, approve/override decisions, log rationale | | Training record link |
| AI Product Owner | Maintain oversight procedures, ensure operator training | | Oversight review notes |
| Compliance Lead | Audit overrides, track KPIs, report to AIMS management review | | Audit log reference |

## Oversight Workflow

1. **Detection:** Operator receives AI output with confidence/trace context.
2. **Assessment:** Operator applies decision tree (`link to SOP`) and requests additional context if needed.
3. **Override/Approval:** Operator records decision in oversight UI; overrides require mandatory reason code.
4. **Escalation:** For safety-critical exceptions, notify on-call SME within 15 minutes via PagerDuty/Teams.
5. **Logging:** All actions emit structured events to OpenTelemetry (`patterns/code/otel/`) and SIEM.

## Controls & Monitoring

- Minimum override sample rate: `X%` per release, tracked in PMM dashboards.
- Operator comprehension surveys conducted quarterly; store results in `templates/operator_training_log.csv`.
- Alerts for sustained override rates above threshold; escalate to risk management for mitigation.

## Evidence Checklist

- Oversight training curriculum and attendance.
- Override audit trail (`system`, `query_id`, `decision`, `operator_id`, `reason`).
- Quarterly review minutes summarizing oversight effectiveness.
