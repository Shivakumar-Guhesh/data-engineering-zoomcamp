variable "credentials" {
  description = "My Credentials"
  # default     = "/d/data-engineering-zoomcamp/keys/terraform-runner_creds.json"
  default = "../../keys/mage-zoomcamp-runner_creds.json"
  #ex: if you have a directory where this file is called keys with your service account json file
  #saved there as my-creds.json you could use default = "./keys/my-creds.json"
}


variable "project" {
  description = "Project"
  default     = "dtc-de-course-411907"
}

variable "region" {
  description = "Region"
  #Update the below to your desired region
  default = "asia-south1-a"
}

variable "location" {
  description = "Project Location"
  #Update the below to your desired location
  default = "ASIA-SOUTH1"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  #Update the below to a unique bucket name
  default = "mage_zoomcamp_bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}
