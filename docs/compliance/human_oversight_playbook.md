# Human Oversight Playbook (EU AI Act Art. 14)

## Objective

Ensure qualified personnel supervise AI system outputs, retain the ability to override decisions, and maintain documented evidence of oversight effectiveness.

## Oversight Model

- **Mode:** HITL / HOTL (select and justify).
- **Systems Covered:** (list Bedrock, Vertex AI solutions).
- **Oversight Tools:** (UI, dashboards, alerting channels).

## Operator Requirements

- Training curriculum with competency assessment.
- Access control policy (least privilege, MFA).
- Duty rotation and fatigue management.

## Procedures

1. Review AI output with context (confidence, explanation).
2. Decide approve/override; document rationale with reason codes.
3. Escalate abnormal events to SME within defined SLA.
4. Capture logs via OpenTelemetry and store in immutable repository.
5. Participate in periodic oversight effectiveness reviews.

## Metrics & KPIs

- Override rate (%).
- Time to respond to high-risk decisions.
- Operator comprehension score.
- Number of incidents escalated to PMM.

## Evidence Checklist

- Training records and certifications.
- Oversight decision logs.
- Quarterly effectiveness assessments.
- Tool validation tests (demonstrate override functionality).
