# GCP Landing Zone for Vertex AI

This folder scaffolds the IaC required to deploy GCP Vertex AI workloads within compliant guardrails.

## Directory Layout

```
vertex-foundation/
  main.tf                 # Terraform (or Google Deployment Manager) entry point
  variables.tf
  CONTROL_MAPPING.md
shared-controls/
  logging.tf
  security.tf
  CONTROL_MAPPING.md
```

## Implementation Notes

- **Project structure**: Isolate runtime, data, and audit projects. Enforce folder-level policies (constraints, CMEK).
- **Network controls**: Restrict Vertex AI endpoints to private service connect. Use VPC Service Controls to prevent data exfiltration.
- **Audit & logging**: Route Cloud Audit Logs and Vertex AI pipeline logs to a centralized project with bucket-level retention.
- **Data governance**: Require CMEK for all storage, note keys and rotation cadence in data governance documentation.
- **Change management**: Connect Terraform or `gcloud` pipelines to approval workflows and record change IDs in `templates/change_log.csv`.

> ✅ **Action for Platform Team**: Populate the placeholder Terraform files and maintain `CONTROL_MAPPING.md` to reflect deployed guardrails and evidence references.
