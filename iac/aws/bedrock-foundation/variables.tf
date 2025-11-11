variable "region" {
  description = "AWS region hosting Bedrock workloads."
  type        = string
  default     = "us-east-1"
}

variable "vpc_cidr_block" {
  description = "CIDR block for the Bedrock VPC. Restrict width to reduce blast radius."
  type        = string
  default     = "10.10.0.0/16"
}

variable "environment" {
  description = "Environment tag (e.g., dev, staging, prod) used for control evidence linkage."
  type        = string
}

variable "tags" {
  description = "Map of tags applied to all resources, include aims_control_id for traceability."
  type        = map(string)
  default     = {}
}
