provider "aws" {  
  region = var.aws_region  
  profile = var.aws_profile
  default_tags {
    tags = {
      Admin-WorkloadName = "cohort9-song-api-producer"
      Admin-Environment = var.env
      Admin-ServiceDomain = var.service_domain
      Auto-OrchestratedBy = "EASIKit"
    }
  }  
}  

# the bucket itself must already exist and would be managed by a
# central Team AWS Account Core project, speak to your SOM/domain tech lead for details
terraform {
  # bucket should already exist, e.g. with easikit-aws-core/module/tfstate-backend
  # e.g bucket = "ucl-isd-identity-dev-terraform-state"
  #     key    = "dev/person-api-producer/terraform.tfstate
  backend "s3" {
    bucket = "ucl-isd-aais-nonprod-terraform-state"
    key    = "dev/cohort9-song-api-producer/terraform.tfstate"
    region = "eu-west-2"
  }
}


terraform {
  required_providers {
    ansiblevault = {
      source  = "MeilleursAgents/ansiblevault"
      version = "2.2.0"
    }
  }
}

provider "ansiblevault" {
  vault_path  = pathexpand("../../../../.vault/vault-pass.txt")
  root_folder = path.cwd
}
