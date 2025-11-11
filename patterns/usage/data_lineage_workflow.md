# Data Lineage Workflow

## Purpose

Ensure training, validation, and test datasets for AWS Bedrock and GCP Vertex AI workloads are tracked, validated, and auditable to satisfy EU AI Act Art. 10 and ISO 42001 data governance requirements.

## Workflow Stages

1. **Ingestion**
   - Register source systems and dataset purpose.
   - Perform legal and contractual checks (usage rights).
   - Record in `templates/data_inventory.csv`.
2. **Preparation**
   - Apply preprocessing pipelines with version control.
   - Generate bias and representativeness metrics; attach reports.
   - Store config hashes in lineage metadata store.
3. **Validation**
   - Execute validation suite (statistical tests, fairness, robustness).
   - Log results using OpenTelemetry events tagged with `aims_control_id`.
   - Capture approvals in ticketing system.
4. **Release**
   - Publish dataset version with checksum, owners, scope of use.
   - Update model cards with dataset references.
   - Archive immutable copy in compliant storage (S3 Glacier / GCS Archive).

## Evidence Artifacts

- Dataset datasheet (link).
- Bias/fairness assessment reports.
- Access control logs and approval workflows.
- Immutable storage verification (checksum, retention policy).

## Ownership Matrix

| Role | Responsibilities |
|------|------------------|
| Data Steward | Maintains data inventory, oversees lineage capture |
| ML Engineer | Executes validation suite, logs metrics |
| Compliance Officer | Reviews documentation, ensures retention policies |

## Automation Hooks

- Integrate with OpenLineage or Data Catalog APIs for metadata capture.
- Emit lineage events to SIEM and PMM dashboards.
- Trigger alerts when datasets lack assigned `purpose_of_use` metadata.
