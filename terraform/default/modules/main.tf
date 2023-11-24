module "lambda" {
  source      = "git@github.com:ucl-isd/easikit-terraform-lambda.git//module"

  # the propogated from the terraform.tfvars.json config element, all mandatory
  func_name             = local.config.name         # (defined in the target tfvars)
  image_ecr             = local.config.image_ecr    # (defined in the target tfvars)
  image_repo            = local.config.image_repo   # (defined in the target tfvars)

  # the propogated from the terraform.tfvars.json config element, can be omitted
  env_vars              = local.env_vars            # (combination of module and target)

  # core variables, from variables.tf, always just here
  name        = var.name
  serv        = var.serv
  env         = var.env
  vrsn        = var.vrsn
}

locals {
  # will auto update as things are added to config vars
  # under { "config": "endpoints": { ... } }
  # will associate them with the above lambda
  # to include a second lambda, create additional lambda_maps and merge() them
  lambda_map = { for e, ep in local.config.endpoints: e => {
      lambda_name       = module.lambda.lambda_function_name
      lambda_invoke_arn = module.lambda.lambda_function_invoke_arn
      http_method       = ep.http_method
      resource_path     = ep.resource_path
    }
  }
}


module "gateway" {
  source      = "git@github.com:ucl-isd/easikit-terraform-api-gateway.git//module"

  # output variables from the lambda modules
  lambda_functions      = local.lambda_map           # (required)

  # the propogated from the terraform.tfvars.json config element
  domain_name           = local.config.domain_name   # (from target tfvars)
  context_path          = local.config.context_path  # (from module tfvars)
  api_version           = local.config.api_version   # (from target tfvars)
  authoriser            = local.config.authoriser    # (from target tfvars)
  client_id             = local.config.client_id     # (from target tfvars)

  # core variables, from variables.tf, always just here
  name        = var.name
  serv        = var.serv
  env         = var.env
  vrsn        = var.vrsn
}