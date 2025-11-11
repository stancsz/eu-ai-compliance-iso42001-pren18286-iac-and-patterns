# EU AI Compliance Control Reference

This repository is a control reference for teams that must operate AI systems in line with **ISO/IEC 42001** and **prEN 18286 / EU AI Act** requirements. It bundles opinionated scaffolding, patterns, and documentation templates so that platform, product, and compliance teams share a single source for controls, evidence, and responsibilities.

> ⚠️ All content is intentionally templated. Replace placeholders with system-specific details, track decisions in your change records, and store evidence in the locations referenced throughout the repo.

## Standards Alignment

- **ISO/IEC 42001** provides the AI Management System (AIMS) structure: governance, risk treatment, internal audit, and continual improvement.
- **prEN 18286 / EU AI Act** defines the control objectives for high-risk AI systems: risk management, data governance, technical documentation, logging, human oversight, and post-market monitoring.

The repository maps each control area to implementation guidance (IaC and code), operational patterns, and evidence templates to maintain audit readiness.

## Repository Structure

| Path | Description | Primary Owners |
|------|-------------|----------------|
| `iac/` | Cloud landing zones, guardrails, and control mappings for AWS Bedrock and GCP Vertex AI | Platform / Cloud Engineering |
| `patterns/usage/` | Operational runbooks covering human oversight, post-market monitoring, and data lineage | Product / Compliance |
| `patterns/code/otel/` | OpenTelemetry instrumentation patterns, schema, and exporter guidance | ML Engineering / SRE |
| `docs/compliance/` | ISO 42001 & EU AI Act templates: risk, logging, PMM, oversight, internal audit | Compliance / Risk |
| `docs/prd/` | Product Requirement Docs for Bedrock and Vertex AI control baselines | Product / Platform |
| `templates/` | CSV/MD templates for registers, change logs, training, and traceability | Control Owners |

```
├── docs/
│   ├── compliance/      # Control playbooks and ISO/EU templates
│   └── prd/             # Platform-specific PRDs (AWS Bedrock, GCP Vertex AI)
├── iac/
│   ├── aws/             # Terraform stubs + control mapping for Bedrock
│   ├── gcp/             # Terraform stubs + control mapping for Vertex AI
│   └── modules/         # Reusable networking/perimeter modules
├── patterns/
│   ├── usage/           # Operational procedures (HITL, PMM, data lineage)
│   └── code/otel/       # Instrumentation examples & schema
└── templates/           # Evidence capture forms (CSV/Markdown)
```

## Working with Controls

1. **Plan** – Use the PRDs in `docs/prd/` to scope your solution, identify required controls, and assign owners.
2. **Build** – Instantiate infrastructure from `iac/`, populate control mappings, and integrate code/usage patterns.
3. **Instrument** – Apply the OpenTelemetry schema in `patterns/code/otel/otel_schema.yaml`, emit traces/logs to your collector, and tag spans with control IDs for traceability.
4. **Operate** – Run oversight, PMM, and logging processes using the patterns and templates provided.
5. **Evidence** – Store artefacts (risk registers, datasheets, PMM reports, audits, telemetry exports) using the templates in `templates/` and link them back to control mappings.

### Telemetry & Evidence Storage

- **Instrumentation examples:** See `patterns/code/otel/python_inference_example.py` for Bedrock calls and `patterns/code/otel/vertex_pipeline_instrumentation.md` for Vertex AI pipelines.
- **Schema:** Align spans/events with `patterns/code/otel/otel_schema.yaml` so downstream analytics can correlate telemetry to controls.
- **Collector guidance:** Export traces and logs to an OTLP collector (AWS Distro, Cloud Ops Agent, etc.) and persist immutable copies in your audit project/bucket as part of the logging plan (`docs/compliance/logging_monitoring_plan.md`).
- **Trace register:** Record canonical trace IDs tied to model runs using `templates/run_trace_log.csv` to demonstrate auditability.

## Control-to-Repository Mapping

| Control Area | Implementation Guidance | Evidence Template(s) |
|--------------|------------------------|----------------------|
| Risk Management (EU AI Act Art. 9) | `docs/compliance/risk_management_plan.md`, PRDs | `templates/risk_register.csv`, change log |
| Data Governance (Art. 10) | `docs/compliance/data_gov_playbook.md`, usage patterns | `templates/data_inventory.csv` |
| Technical Documentation (Art. 11) | `docs/prd/*`, `docs/compliance/technical_documentation_index.md` | Link to architecture, model cards, validation evidence |
| Logging & Record Keeping (Art. 12) | `patterns/code/otel/`, `docs/compliance/logging_monitoring_plan.md` | `templates/alert_test_log.csv`, SIEM dashboards |
| Human Oversight (Art. 14) | `patterns/usage/human_oversight_runbook.md`, oversight playbook | `templates/operator_training_log.csv` |
| Post-Market Monitoring (Art. 72) | `patterns/usage/post_market_monitoring.md`, PMM plan | `templates/pmm_report_template.md` |
| Internal Audit (ISO 42001 Cl. 9.2) | `docs/compliance/internal_audit_checklist.md` | Audit reports, corrective actions |

## Adoption Checklist

- [ ] Confirm scope, risk classification, and stakeholders in the relevant PRD.
- [ ] Deploy the appropriate IaC stacks and complete `CONTROL_MAPPING.md` entries with resource IDs and evidence links.
- [ ] Instrument workloads with OpenTelemetry using the provided schema and examples.
- [ ] Populate governance templates and registers with project-specific data.
- [ ] Schedule PMM, oversight, and internal audit routines; capture outputs via the provided templates.
- [ ] Review and update artefacts during management review per ISO 42001.

## Contributing

1. Fork or branch from `main`.
2. Update documentation, IaC, or patterns with control references and evidence guidance.
3. Run linting/validation for any code or templates you modify.
4. Submit a pull request referencing the control(s) affected and evidence impact.

For questions about control ownership or audit expectations, reach out to the AI Governance working group or your compliance lead.
