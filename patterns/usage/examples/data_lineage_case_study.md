# Example: Data Lineage Case Study

## Dataset Overview

- **Dataset ID:** `bedrock-support-train-v11`
- **Purpose of Use:** Fine-tuning customer support assistant
- **Source Systems:** Zendesk export, Knowledge base CMS
- **Lawful Basis:** Contractual necessity + user consent within support terms
- **Retention Policy:** 2 years, then anonymized archive

## Lineage Summary

| Stage | Tooling | Notes | Evidence |
|-------|---------|-------|----------|
| Ingestion | AWS Glue crawler | Imported raw tickets into S3 `s3://cust-support-raw` | Data inventory record `INV-443` |
| Preparation | PySpark job `prep_clean_v5` | Redacted PII, mapped intents, balanced classes | Git commit `f1a23cd`, notebook `nb://prep-clean-v5` |
| Validation | Bias check `fairlens` | Detected under-representation of `es-ES` tickets → added samples | Bias report `BR-2025-02` |
| Release | Model registry entry `support-assistant-v11` | Linked datasheet, checksum `sha256:89af...` | MLflow artifact `support-v11` |

## Controls

- `DATA-10`: Datasheet updated with new language coverage section.
- `RISK-09`: Residual risk lowered to `Medium` post-mitigation.
- `LOG-12`: OpenTelemetry events emitted for preprocessing and validation steps (`trace-data-20250305`).

## Next Review

- Schedule lineage review in May 2025 to confirm additional languages remain balanced.
