# Control Mapping – AWS Shared Controls

| Control | Requirement Summary | Terraform Resource(s) | Evidence Location |
|---------|---------------------|-----------------------|-------------------|
| ISO 42001 Cl. 7.5 (Documented Info) | Centralize logs and configuration baselines | `aws_cloudtrail.trail`, `aws_config_configuration_recorder.recorder` | Logging retention policy, config snapshots |
| EU AI Act Art. 12 (Logging) | Maintain tamper-evident logs for AI services | `aws_cloudwatch_log_group.organization`, `aws_s3_bucket.audit_logs` | SIEM dashboards, log integrity checks |
| EU AI Act Art. 15 (Accuracy & Robustness) | Enable Security Hub controls for AI endpoints | `aws_securityhub_standards_subscription.default` | Security Hub reports, remediation runbooks |
| ISO 42001 Cl. 9.1 (Monitoring) | Provide metrics for management review | `aws_cloudwatch_metric_alarm.*` | Management review minutes, KPIs |

> Update `Terraform Resource(s)` with module outputs when implementing in Terraform or CloudFormation.
