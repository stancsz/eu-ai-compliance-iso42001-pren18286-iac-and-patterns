# Infrastructure as Code (IaC)

This pillar provides secure-by-default landing zones for AWS Bedrock and GCP Vertex AI workloads. The modules are intentionally lightweight: fill in provider-specific details while preserving the documented control mappings and evidence expectations.

## Structure

```
aws/
  bedrock-foundation/       # Core networking, IAM, and Bedrock guardrails
  shared-controls/          # Cross-account services (CloudTrail, Config, Audit)
gcp/
  vertex-foundation/        # Projects, service perimeters, Vertex AI guardrails
  shared-controls/          # SCC, Cloud Logging, IAM controls
modules/                    # Reusable Terraform/Bicep/Deployment Manager modules
policies/                   # OPA/Rego, SCPs, Organization Policies
```

## Getting Started

1. Review the PRD for your target platform in `../docs/prd/`.
2. Instantiate the appropriate foundation stack (AWS or GCP) in a staging environment.
3. Tag all resources with `aims_control_id` to link infrastructure to compliance evidence.
4. Integrate policy checks in CI/CD (`terraform validate`, `cfn_nag`, `gcloud policy troubleshooter`, etc.).
5. Record deployment approvals and change tickets in the `templates/change_log.csv`.

> 📌 **Evidence Hook**: Each module includes a `CONTROL_MAPPING.md` file describing the control objectives it supports. Update these files when extending modules so auditors can trace IaC to regulatory requirements.
