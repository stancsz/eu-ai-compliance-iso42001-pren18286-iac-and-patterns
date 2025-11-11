# PRD: GCP Vertex AI Compliance-Aligned Platform

## Executive Summary

Deliver a Vertex AI-based platform for high-risk AI workloads that complies with ISO/IEC 42001 management system controls and EU AI Act mandates.

## Goals & Non-Goals

- **Goals**
  - Provision secure Vertex AI environments with VPC Service Controls.
  - Standardize data governance, telemetry, and PMM integrations.
  - Provide auditable documentation artifacts linked to deployments.
- **Non-Goals**
  - Building generic AutoML tooling beyond compliance scope.
  - Managing downstream application UI/UX (handled by product teams).

## Stakeholders

| Role | Name | Responsibilities |
|------|------|------------------|
| Product Owner |  | Requirements, prioritization, compliance sign-off |
| Platform Lead |  | IaC, service perimeters, identity management |
| ML Lead |  | Pipeline design, validation, monitoring |
| Compliance Lead |  | Control alignment, evidence collection |
| Security Lead |  | SCC findings, access reviews, incident response |

## Use Cases

- **Document Classification** — process regulated documents with human oversight.
- **Risk Scoring** — infer risk ratings requiring audit trails and overrides.
- **Data Extraction** — structured extraction with bias and drift monitoring.

## Functional Requirements

1. Vertex AI projects isolated via folders, service perimeters, and policy constraints.
2. Pipelines instrumented with OpenTelemetry tracing (`patterns/code/otel`).
3. Automated datasheet generation and storage in `templates/data_inventory.csv`.
4. Oversight workflow integrated with Pub/Sub + Cloud Functions for overrides.
5. PMM dashboards in Cloud Monitoring with drift, performance, complaint metrics.

## Non-Functional & Compliance Requirements

| Requirement | Control Reference | Owner | Evidence |
|-------------|-------------------|-------|----------|
| Risk Management | ISO 42001 Cl. 6 / EU AI Act Art. 9 | Compliance Lead | `docs/compliance/risk_management_plan.md` |
| Data Governance | EU AI Act Art. 10 | Data Steward | `docs/compliance/data_gov_playbook.md` |
| Logging & Monitoring | EU AI Act Art. 12 | Platform Lead | `docs/compliance/logging_monitoring_plan.md` |
| Human Oversight | EU AI Act Art. 14 | Product Owner | `patterns/usage/human_oversight_runbook.md` |
| PMM | EU AI Act Art. 72 | ML Lead | `docs/compliance/pmm_plan.md` |
| Internal Audit | ISO 42001 Cl. 9.2 | Compliance Lead | `docs/compliance/internal_audit_checklist.md` |

## Architecture Overview

- **IaC**: `iac/gcp/vertex-foundation` with service perimeter module.
- **Identity**: Workload Identity Federation, conditional access.
- **Pipelines**: Vertex AI Pipelines with TFX/Custom components.
- **Telemetry**: OpenTelemetry SDK -> Cloud Logging/BigQuery -> SIEM.
- **Oversight**: Pub/Sub events to Cloud Functions notifying human reviewers.
- **Data Storage**: CMEK-encrypted buckets & BigQuery datasets with retention.

## Control Implementation Matrix

| Feature | Control Objective | Implementation | Validation |
|---------|-------------------|----------------|------------|
| Service Perimeter | Prevent data exfiltration | Access Context Manager | Exfiltration simulation |
| Lineage Capture | Datasheet evidence | Data Catalog + templates | Internal audit review |
| Telemetry | Traceability | OTel spans, logs-based metrics | Alert test log |
| Human Override | HITL capability | Pub/Sub -> Cloud Functions -> UI | Tabletop exercise |
| PMM Dashboard | Continuous monitoring | Cloud Monitoring dashboards | PMM report |

## Delivery Plan

1. **Phase 0** — Finalize requirements, assign control owners, update risk plan.
2. **Phase 1** — Deploy shared controls (`iac/gcp/shared-controls`), configure logging.
3. **Phase 2** — Build service perimeters, IAM, CMEK via IaC.
4. **Phase 3** — Implement pipelines with OTel instrumentation.
5. **Phase 4** — Integrate oversight workflow and PMM dashboards.
6. **Phase 5** — Conduct validation (bias testing, security review, simulation).
7. **Phase 6** — Produce documentation bundle and internal audit walkthrough.

## Open Issues & Risks

- Need to confirm acceptable data residency regions.
- Pending integration with enterprise IAM/SSO.
- Additional tooling required for automated datasheet generation.

## Acceptance Criteria

- Control mappings completed with links in `CONTROL_MAPPING.md`.
- Successful test of perimeter enforcement and incident response.
- PMM report generated and reviewed before go-live.
- Internal audit sign-off with resolved findings.
