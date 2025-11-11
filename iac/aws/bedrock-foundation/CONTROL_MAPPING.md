# Control Mapping – AWS Bedrock Foundation

| Control | Requirement Summary | Terraform Resource(s) | Evidence Location |
|---------|---------------------|-----------------------|-------------------|
| ISO 42001 Cl. 8.2 (Risk Treatment) | Enforce risk mitigation controls for AI services | `aws_iam_role.bedrock_execution`, `aws_networkfirewall_firewall.main` | Change tickets, risk register entries |
| EU AI Act Art. 9 (Risk Management) | Ensure runtime isolation & secure connectivity | `aws_vpc.main`, `aws_vpc_endpoint.bedrock` | VPC diagrams, pen-test reports |
| EU AI Act Art. 10 (Data Governance) | Control data residency, encryption, lineage | `aws_s3_bucket.model_artifacts`, `aws_kms_key.bedrock` | Data inventory, key rotation logs |
| EU AI Act Art. 12 (Logging) | Capture inference & system logs | `aws_cloudwatch_log_group.bedrock_invocations`, `aws_cloudtrail.trail` | Log retention policy, SIEM dashboards |
| EU AI Act Art. 14 (Human Oversight) | Enable manual review & fallback | `aws_sns_topic.human_review`, `aws_lambda_function.override_handler` | Oversight runbook, operator training records |
| EU AI Act Art. 72 (PMM) | Feed production telemetry into PMM loop | `aws_eventbridge_rule.pmm_events`, `aws_lambda_function.pmm_ingestor` | PMM reports, incident postmortems |

> Update the `Evidence Location` column with links to Confluence/Jira/SharePoint records after deployment. Auditors expect traceability from IaC to evidence.
