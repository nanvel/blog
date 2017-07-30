labels: Draft
        Tools
created: 2017-07-07T20:12
modified: 2017-07-07T20:12
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

## Vocabulary

### Infrastructure as Code

Infrastructure as Code (IAC) - write and execute code to define, deploy, and update your infrastructure.

## Links

[Terraform At Scale](https://www.youtube.com/watch?v=RldRDryLiXs) by Calvin French-Owen on YouTube
[Terraform: Up and Running](https://www.amazon.com/Terraform-Running-Writing-Infrastructure-Code-ebook/dp/B06XKHGJHP/) by Yevgeniy Brikman
