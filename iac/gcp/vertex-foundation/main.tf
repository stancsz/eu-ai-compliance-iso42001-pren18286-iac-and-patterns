// Placeholder Terraform configuration for GCP Vertex AI foundation stack.
terraform {
  required_version = ">= 1.6.0"

  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

module "service_perimeter" {
  source = "../modules/service_perimeter"

  project_ids     = var.secured_project_ids
  access_level    = var.access_level
  control_context = var.control_context
}

// TODO: add modules for Vertex AI pipelines, Cloud Logging sinks, CMEK, and PMM hooks.
