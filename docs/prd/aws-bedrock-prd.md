# PRD: AWS Bedrock Compliance-Aligned Service

## Executive Summary

Design a Bedrock-based generative AI service that meets ISO/IEC 42001 AIMS requirements and EU AI Act obligations for high-risk systems.

## Goals & Non-Goals

- **Goals**
  - Deliver controlled Bedrock inference endpoints with auditable oversight.
  - Implement data governance, logging, and PMM integrations out of the box.
  - Provide evidence artifacts aligned with auditors' expectations.
- **Non-Goals**
  - Training custom foundation models (focus on fine-tuning/inference).
  - Replacing enterprise ticketing or documentation systems.

## Stakeholders

| Role | Name | Responsibilities |
|------|------|------------------|
| Product Owner |  | Scope, roadmap, compliance sign-off |
| Platform Lead |  | IaC deployment, guardrails |
| ML Lead |  | Prompt design, evaluation, risk mitigation |
| Compliance Lead |  | Control mapping, evidence collection |
| Security Lead |  | IAM, logging integrity, incident response |

## User Personas & Use Cases

- **Customer Support Agent** — consumes AI-generated responses, must escalate unsafe outputs.
- **Compliance Officer** — reviews oversight logs, verifies controls.
- **ML Engineer** — tunes prompts, monitors performance and drift.

## Functional Requirements

1. Bedrock inference API reachable only from approved VPCs/subnets.
2. Human oversight UI with override action writing to immutable logs.
3. Automated logging to S3/SIEM with OTel schema (`patterns/code/otel`).
4. Risk register and PMM integration via templates (`templates/`).
5. Alerting for policy violations (e.g., override spike, drift metrics).

## Non-Functional & Compliance Requirements

| Requirement | Control Reference | Owner | Evidence |
|-------------|-------------------|-------|----------|
| Risk Management | ISO 42001 Cl. 6 / EU AI Act Art. 9 | Compliance Lead | `docs/compliance/risk_management_plan.md` |
| Data Governance | EU AI Act Art. 10 | Data Steward | `docs/compliance/data_gov_playbook.md` |
| Logging & Traceability | EU AI Act Art. 12 | Platform Lead | `docs/compliance/logging_monitoring_plan.md` |
| Human Oversight | EU AI Act Art. 14 | Product Owner | `patterns/usage/human_oversight_runbook.md` |
| PMM | EU AI Act Art. 72 | ML Lead | `docs/compliance/pmm_plan.md` |
| Internal Audit | ISO 42001 Cl. 9.2 | Compliance Lead | `docs/compliance/internal_audit_checklist.md` |

## Architecture Overview

- **IaC**: `iac/aws/bedrock-foundation` for VPC, IAM, logging.
- **App Layer**: Lambda/API Gateway (or container) invoking Bedrock.
- **Telemetry**: OpenTelemetry collector -> CloudWatch/S3/SIEM.
- **Oversight UI**: Web app integrated with Cognito and audit logs.
- **Data Storage**: S3 buckets with CMEK and access logging.

## Control Implementation Matrix

| Feature | Control Objective | Implementation | Validation |
|---------|-------------------|----------------|------------|
| VPC Endpoint | Restrict access to Bedrock | PrivateLink, security groups | Pen test, network scan |
| Prompt Logging | Trace decision inputs | OTel span with `payload_hash` | Log integrity checks |
| Override Workflow | HITL/HOTL capability | UI + SNS + Lambda | Tabletop exercise |
| Drift Detection | PMM trigger | CloudWatch metrics + EventBridge | Simulation test |
| Change Approval | Maintain audit trail | Terraform pipeline + change log | Internal audit review |

## Delivery Plan

1. **Phase 0** — Finalize requirements, update risk plan, assign owners.
2. **Phase 1** — Deploy shared controls (`iac/aws/shared-controls`), set up logging.
3. **Phase 2** — Build inference service, implement OTel instrumentation.
4. **Phase 3** — Develop oversight UI and integrate override workflow.
5. **Phase 4** — Conduct validation (security review, bias tests, tabletop).
6. **Phase 5** — Launch PMM cycle, prepare technical documentation bundle.

## Open Issues & Risks

- Pending DPIA approval for dataset usage.
- Need to confirm data residency restrictions.
- Human oversight tool UX requires accessibility review.

## Acceptance Criteria

- All controls mapped with evidence links in `CONTROL_MAPPING.md`.
- Successful dry-run of incident notification procedure.
- PMM report generated prior to production launch.
- Internal audit walkthrough completed with no major non-conformities.
