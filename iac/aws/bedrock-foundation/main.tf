// Placeholder Terraform configuration for AWS Bedrock foundation stack.
// Replace with modules and resources that implement the documented controls.
terraform {
  required_version = ">= 1.6.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.region
}

module "networking" {
  source = "../modules/networking"

  vpc_cidr_block          = var.vpc_cidr_block
  enable_network_firewall = true
  allowed_bedrock_services = [
    "bedrock.amazonaws.com",
  ]
}

// TODO: add modules for IAM, logging, data governance, and PMM integrations.
