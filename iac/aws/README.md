# AWS Landing Zone for Bedrock

This folder scaffolds the IaC required to deploy AWS Bedrock workloads under ISO/IEC 42001 and EU AI Act obligations. It separates shared guardrails from workload-specific stacks so that evidence can be mapped per control.

## Directory Layout

```
bedrock-foundation/
  main.tf                 # Terraform entry point (placeholder)
  variables.tf            # Input definitions with compliance defaults
  CONTROL_MAPPING.md      # Links Terraform resources to control objectives
shared-controls/
  cloudtrail.tf
  securityhub.tf
  CONTROL_MAPPING.md
```

## Implementation Notes

- **Identity segregation**: Use separate AWS accounts for development, staging, and production. Enforce SSO and MFA through AWS IAM Identity Center.
- **Network controls**: Restrict Bedrock access via VPC endpoints, private subnets, and AWS Network Firewall.
- **Audit & logging**: Centralize CloudTrail, CloudWatch, and Bedrock invocation logs in a dedicated audit account with immutable storage.
- **Data governance**: Parameterize S3 bucket policies and KMS keys to enforce purpose limitation and encryption requirements.
- **Change management**: Integrate Terraform execution plans with your ticketing system and store approvals in `templates/change_log.csv`.

> ✅ **Action for Platform Team**: Populate `main.tf` and `variables.tf` with your baseline modules (e.g., networking, IAM, logging). Update `CONTROL_MAPPING.md` with resource IDs and evidence links after each deployment.
