variable "project_id" {
  description = "Primary GCP project hosting Vertex AI workloads."
  type        = string
}

variable "region" {
  description = "GCP region for Vertex AI resources."
  type        = string
  default     = "us-central1"
}

variable "secured_project_ids" {
  description = "List of project IDs included in the Vertex AI service perimeter."
  type        = list(string)
}

variable "access_level" {
  description = "Access level name applied to the service perimeter (Access Context Manager)."
  type        = string
}

variable "control_context" {
  description = "Map of control metadata (e.g., aims_control_id) applied to resources."
  type        = map(string)
  default     = {}
}
