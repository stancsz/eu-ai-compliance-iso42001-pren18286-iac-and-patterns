# Example: Vertex AI Document Classifier PMM Cycle

## Period

- **System:** Vertex AI document classification pipeline
- **Period Covered:** 2025-02-01 → 2025-02-28
- **Prepared By:** ML Ops Lead
- **Reviewed By:** Compliance Officer

## Key Metrics

| Metric | Target | Actual | Trend | Notes |
|--------|--------|--------|-------|-------|
| Precision | ≥ 0.92 | 0.915 | ▼ | Slight drop due to new document layout |
| Drift score | ≤ 0.2 | 0.18 | ▲ | Within limit; monitor |
| Complaints | 0 | 1 | ▲ | Incorrect risk rating filed |
| Override rate | ≤ 3% | 2.4% | ▬ | On target |

## Incidents & Complaints

- `INC-3058`: Customer reported misclassified risk letter; investigation traced to missing template in training data. Mitigated by adding template to dataset and re-running validation.

## Actions

- Retraining scheduled (`RUN-2025-03-04`) with updated dataset.
- Data steward to update datasheet (`DS-vertex-risk-v14`) and document new template coverage.
- Risk management entry `RISK-17` residual rating updated to `Medium`.

## Evidence Links

- OTel trace sample: `trace-vertex-20250218-2201`
- PMM dashboard snapshot: `confluence://pmm/vertex/feb-2025`
- Change ticket: `CHG-228`
