# EU AI Compliance Golden Reference

This repository provides a golden reference implementation that helps AI teams meet both **ISO/IEC 42001** (AI Management System) and **prEN 18286 / EU AI Act** (high-risk AI controls) requirements. It contains four pillars:

1. **Infrastructure as Code (IaC)** blueprints for AWS Bedrock and GCP Vertex AI landing zones.
2. **Usage patterns** that demonstrate compliant operating practices (risk, data, oversight, PMM).
3. **Code patterns** focused on observability (OpenTelemetry) and control implementation.
4. **Compliance documentation templates** to operationalize the AI Management System (AIMS).

> ⚠️ This repo is intentionally scaffolded. Replace placeholder sections with project-specific details, track decision logs, and store evidence in the referenced locations to remain audit-ready.

## Repository Layout

```
iac/                 # Cloud landing zones, shared guardrails, control mappings
patterns/
  usage/             # Operational runbooks & HITL/HOTL patterns
  code/otel/         # Observability & logging patterns for services & pipelines
docs/
  compliance/        # ISO 42001 & prEN 18286 templates and playbooks
  prd/               # Product Requirement Docs for AWS Bedrock & GCP Vertex AI solutions
templates/           # Registers, logs, and evidence capture forms
```

## Getting Started

- Use the PRDs in `docs/prd/` to define scope, controls, and responsibilities for Bedrock and Vertex AI workloads.
- Instantiate IaC modules from `iac/` to provision environments with compliance guardrails.
- Adopt usage and code patterns to enforce logging, human oversight, and post-market monitoring.
- Populate compliance templates with project-specific data, linking to evidence in your chosen system of record.

## Compliance Traceability

| Control Area | Repository Source | Evidence Expectations |
|--------------|-------------------|-----------------------|
| Risk Management (Art. 9) | `docs/compliance/risk_management_plan.md` | Risk register, mitigation status, approval logs |
| Data Governance (Art. 10) | `docs/compliance/data_gov_playbook.md` | Data lineage reports, bias assessments, access logs |
| Technical Documentation (Art. 11) | `docs/prd/*`, `templates/model_card.md` | Versioned model cards, design decisions, validation results |
| Logging & Record Keeping (Art. 12) | `patterns/code/otel/`, `docs/compliance/logging_monitoring_plan.md` | Immutable log storage, alerting evidence, access reviews |
| Human Oversight (Art. 14) | `patterns/usage/human_oversight_runbook.md` | Training records, override audit trails, operator feedback |
| Post-Market Monitoring (Art. 72) | `docs/compliance/pmm_plan.md` | PMM reports, incident follow-ups, continuous improvement backlog |
| Internal Audit (ISO 42001 Cl. 9.2) | `docs/compliance/internal_audit_checklist.md` | Audit schedule, findings register, corrective actions |

## Next Steps for Teams

- Assign a **Control Owner** for each template and ensure evidence is linked.
- Integrate IaC modules into CI/CD pipelines with policy checks (e.g., OPA, AWS Config, GCP Policy Controller).
- Embed OpenTelemetry exporters and centralize traces/logs in your SIEM with retention policies that meet regulatory requirements.
- Schedule recurring post-market monitoring reviews and document outcomes in the provided templates.

Maintaining compliance is continuous—treat this scaffold as the foundation for your organization’s AI governance program.
