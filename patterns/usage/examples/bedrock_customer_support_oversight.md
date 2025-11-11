# Example: Bedrock Customer Support Oversight

## Context

- **System:** Bedrock GPT-based response assistant
- **Risk Level:** High (customer-facing, potential rights impact)
- **Environment:** Production
- **Control References:** `LOG-12`, `HITL-14`

## Oversight Workflow Snapshot

| Step | Description | Evidence |
|------|-------------|----------|
| Detection | Agent receives AI-generated response with confidence 0.62 and flagged phrase `refund denied`. | OTel trace `trace-8472`, helpdesk ticket `HD-4491` |
| Assessment | Agent reviews knowledge base, identifies missing policy clause, adds clarification. | Override UI log entry `override-2025-03-07-1459` |
| Override | Agent edits final reply, marks reason code `POLICY_GAP`. | SIEM log search `override_reason:POLICY_GAP` |
| Escalation | No escalation needed; override within SLA. | Oversight dashboard screenshot |

## Metrics & Observations

- Override rate (rolling 7-day): **4.2%** (target < 5%).
- Average intervention time: **2.5 minutes** (target < 3 minutes).
- Operator feedback: “Need faster access to recent policy updates.”

## Follow-Up Actions

- Product team to update prompt grounding with latest refund policy (Change ID `CHG-221`).
- Compliance lead to review override reason trends during next PMM session.
