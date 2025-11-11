# Control Mapping – GCP Vertex AI Foundation

| Control | Requirement Summary | Terraform Resource(s) | Evidence Location |
|---------|---------------------|-----------------------|-------------------|
| ISO 42001 Cl. 6.1 (Actions to Address Risk) | Enforce service perimeter and restricted data egress | `google_access_context_manager_service_perimeter.vertex`, `google_compute_firewall.vertex` | Service perimeter change log, network diagrams |
| EU AI Act Art. 9 (Risk Management) | Segregate environments and limit privilege | `google_project_iam_binding.*`, `google_iam_workload_identity_pool_provider.vertex` | IAM review records, risk log |
| EU AI Act Art. 10 (Data Governance) | Ensure dataset lineage and encryption | `google_vertex_ai_dataset.*`, `google_kms_crypto_key.dataset` | Data inventory, CMEK rotation reports |
| EU AI Act Art. 12 (Logging) | Capture prediction, training, and pipeline logs | `google_logging_project_sink.vertex`, `google_pubsub_topic.logging` | Logging dashboards, access reviews |
| EU AI Act Art. 14 (Human Oversight) | Hook manual review workflows into pipelines | `google_cloudfunctions_function.review_dispatch`, `google_pubsub_subscription.human_review` | Oversight runbook, operator training |
| EU AI Act Art. 72 (PMM) | Feed runtime telemetry to PMM analytics | `google_monitoring_dashboard.pmm`, `google_logging_metric.model_drift` | PMM reports, corrective actions |
