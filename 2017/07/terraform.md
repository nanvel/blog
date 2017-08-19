labels: Draft
        Tools
created: 2017-07-07T20:12
modified: 2017-08-19T13:23
place: Phuket, Thailand
comments: true

# Terraform notes

[TOC]

[Terraform home page](https://www.terraform.io/)
[Terraform Documentation](https://www.terraform.io/docs/index.html)
[Terraform best pratices](https://github.com/hashicorp/best-practices/blob/master/terraform/providers/aws/README.md)

Terraform is a tool for building, changing, and versioning infrastructure safely and efficiently.

!!! note "Infrastructure as Code"
    Infrastructure is described using a high-level configuration syntax. This allows a blueprint of your datacenter to be versioned and treated as you would any other code. Additionally, infrastructure can be shared and re-used.

Terraform allows to write code that is specific to each provider, taking advantage of that provicer's unique functionality, but to use the same language and toolset.

Initial release: 2014.

Other provisioning tools:

- Chef
- Puppet
- Ansible
- SaltStack
- CloudFormation
- OpenStack Heat
## Commands

Commands:

- get
- plan
- apply
- graph (use [Graphviz](http://dreampuf.github.io/GraphvizOnline/) to vizualize)
- destroy

AWS ENV:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`

## Syntax

### Input varaibles

```text
variable "<name>" {
	[description = "<description>"]
	[default = <default value>]
	[type = "<type>"]
}
```

Providing a variable value:

- command line (`-var`, `-var-file`)
- ENV variable (`TF_VAR_<variable name>`)
- default value
- user prompt

Type options (terrafomr can gues the type):

- string
- list
- map

### Outputs variables

```text
output "<name>" {
	value = <value>
}
```

### Data sources

A data source represents a piece of read-only information that is fetched from the provider.

### Lifecycle

`create_before_destroy`: create a replacement resource before destroying the original.

## Tips

Starting service on image setup:
```text
resource "aws_instance" "app" {
	...

	user_data = <<-EOF
	#!bin/bash
	sudo service myservice start
	EOF
}
```
`user_data` - a script that executes when the server is booting.

### Don't put terraform state under version control

Problems:

- someone can forget to push it after changes was applied
- someone can forget to pull the latest version before applyying new changes
- all secrets are stored in plain text in state file

Use remote state storage. Available options:

- Amazon S3
- Azure storage
- HashiCorp Consul and Terraform Pro/Enterprise
- Terragrunt (s3 + ddb)

S3 remote storage:
```text
provider "aws" {
	region = "us-east-1"
}

resource "aws_s3_bucket" "terraform_state" {
	bucket = "my-bucket-name"
	versioning {
		enabled = true
	}
	lifecycle {
		prevent_destroy = true
	}
}
```

```bash
terraform apply
terraform remote config \
	-backend=s3 \
	-backend-config="bucket=my-bucket-name" \
	-backend-config="key=global/s3/terraform.tfstate" \
	-backend-config="region=us-east-1" \
	-backend-config="encrypt=true"
```

### Project structure and isolation

Use a folder per environment.

Resource folder:

- `main.tf`
- `vars.tf`
- `outputs.tf`

### Templet files

Use templates files instead of interpolation, for large scripts.

### Module versioning

Use versioning for modules.

### Count

```text
resource "aws_iam_user" "example" {
    count = 10
	name = "myuser.${count.index}"
}
```

Or

```text
resource "aws_iam_user" "example" {
    count = "${length(var.names)}"
	name = "${element(var.names,count.index)}"
}
```

### If statement

Use `count`.

## Vocabulary

### Infrastructure as Code

Infrastructure as Code (IAC) - write and execute code to define, deploy, and update your infrastructure.

## Links

[Terraform At Scale](https://www.youtube.com/watch?v=RldRDryLiXs) by Calvin French-Owen on YouTube
[Terraform: Up and Running](https://www.amazon.com/Terraform-Running-Writing-Infrastructure-Code-ebook/dp/B06XKHGJHP/) by Yevgeniy Brikman
