labels: Draft
        AWS
        HighScalability
created: 2017-06-08T16:38
modified: 2017-06-08T16:38
place: Phuket, Thailand
comments: true

# System engineering

[TOC]

Amazon Route 53 - a highly available and scalable cloud Domain Name System (DNS) web service.
AWS EC2 instance - virtual computing environment.
AWS AMI - preconfigured templates for instances (operation system and additional software). You can launch different types of instances from a single AMI.

## AWS

### Terraform

Terraform - a tool to help manage infrastructure declaratively.

> Moving our infrastructure management into text files allows us to take all our favourite tools and processes for source code and apply them to our infrastructure. Now infrastructure can live in source control, we can review it just like source code, and we can often roll back to an earlier state if something goes wrong.
>
> [Terraform Gotchas And How We Work Around Them](http://heap.engineering/terraform-gotchas/) by Kamal Marhubi

Entry level is lower for new team members, and anyone in the team can find a great understanding of the infrastructure just looking into terraform files.

Articles:

- [Terraform Gotchas And How We Work Around Them](http://heap.engineering/terraform-gotchas/) by Kamal Marhubi at Heap

Best practices:

- run terraform plan -out planfile, Terraform will write the plan to planfile. You can then get exactly that plan to run by running terraform apply planfile
- When you run terraform plan, Terraform refreshes its view of your infrastructure. To do this it only needs read access to your cloud provider ([Read Only Access](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/role_readonly.html))

## AWS ECS

ECS is a set of APIs that turn EC2 instances into compute cluster for container management.

[Our Nightmare2 on Amazon ECS](http://www.appuri.com/blog/-our-docker-nightmare-on-amazon-ecs/) by Bilal Aslam at appuri blog.
[Rebuilding Our Infrastructure with Docker, ECS, and Terraform](https://segment.com/blog/rebuilding-our-infrastructure/) by Calvin French-Owen at segment.
+ [The Seven Biggest Challenges of Deployment to ECS](https://convox.com/blog/ecs-challenges/) on The Convox blog.
[PAAS comparison - Dokku vs Flynn vs Deis vs Kubernetes vs Docker Swarm (2017)](https://news.ycombinator.com/item?id=14531883) on YC
[Kubernetes on AWS EC2](https://kubernetes.io/docs/getting-started-guides/aws/)

!!! caution "Leaking environment variables to CloudTrail"
    See [Our Nightmare2 on Amazon ECS](http://www.appuri.com/blog/-our-docker-nightmare-on-amazon-ecs/). When you start a new service, it logs the service definition including environment variables to CloudTrail!

Alternatives to ECS web console:

- [Convox rack](https://github.com/convox/rack)
- [Empire](https://github.com/remind101/empire)

## To investigate

ECS vs Kubernetes (k8s).
ECS passing configuration.
ECS service discovery without load balancers.
[Terraform](https://www.terraform.io/) - Write, Plan, and Create Infrastructure as Code.
Docker schedulers: Kubernetes, Mesosphere, Nomad, Fleet, Docker Swarm.

[Kubernetes](https://kubernetes.io/docs/home/).
Dokku: Docker powered mini-Heroku. The smallest PaaS implementation you've ever seen.

Tools to build Docker images.

CloudFormation stack.

## Services

Log management:

- [papertrail](https://papertrailapp.com)

Local development:

- Vagrant - a tool for managing local virtual machinese to mimic real-world infrastructure locally (or in the cloud). A server provisioning tool.

Resources monitoring:

- Nagios
- Munin
- Cacti

## Best practices

### Credentials

Credentials, private keys must be passed through env variables.

To check: [credstash](https://github.com/fugue/credstash).

## Vocabulary

### Cowboy coding

Cowboy coding - working directly in a production environment, not documenting or incapsulating changes in code, and not having a way to roll back to a previous version.
