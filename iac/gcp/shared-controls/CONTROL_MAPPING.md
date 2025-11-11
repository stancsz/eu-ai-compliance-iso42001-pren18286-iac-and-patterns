# Control Mapping – GCP Shared Controls

| Control | Requirement Summary | Terraform Resource(s) | Evidence Location |
|---------|---------------------|-----------------------|-------------------|
| ISO 42001 Cl. 7.4 (Communication) | Configure centralized logging and alert routing | `google_logging_project_sink.audit`, `google_monitoring_notification_channel.soc` | Alerting runbook, on-call rotation |
| EU AI Act Art. 12 (Logging) | Preserve immutable audit logs for AI systems | `google_storage_bucket.audit_logs`, `google_logging_bucket_config.retention` | Bucket retention policy, access review |
| EU AI Act Art. 15 (Accuracy & Robustness) | Enable SCC findings for AI workloads | `google_scc_notification_config.default`, `google_scc_source.findings` | SCC reports, remediation records |
| ISO 42001 Cl. 9.1 (Monitoring) | Provide KPIs for management review | `google_monitoring_dashboard.aims`, `google_monitoring_alert_policy.*` | Management review packs, KPI logs |
