labels: Draft
        AWS
        HighScalability
created: 2017-06-08T16:38
modified: 2017-11-27T14:36
place: Phuket, Thailand
comments: true

# System engineering

[TOC]

Amazon Route 53 - a highly available and scalable cloud Domain Name System (DNS) web service.
AWS EC2 instance - virtual computing environment.
AWS AMI - preconfigured templates for instances (operation system and additional software). You can launch different types of instances from a single AMI.

## AWS

### AWS terms in plain English

[Amazon Web Services in Plain English](https://www.expeditedssl.com/aws-in-plain-english).

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

## AWS Lambda

### OCR

OCR speed: ~1 page per execution, ~320MB * 1minute.
See [lambda-text-extractor](https://github.com/skylander86/lambda-text-extractor/blob/master/README.md) on GitHub.

## VPC

VPC is a software-defined network (SDN) optimized for moving massive amounts of packets into, out of and across AWS regions.

[How should I connect to my Amazon virtual private cloud?](https://aws.amazon.com/premiumsupport/knowledge-center/connect-vpc/)

### Subnets

> Ensure that no backend EC2 instances are provisioned in public subnets in order to protect them from exposure to the Internet. In this context, backend instances are EC2 instances that do not require direct access to the public internet such as database, API or caching servers. As best practice, all EC2 instances that are not Internet-facing should run within a private subnet, behind a NAT gateway that allows downloading software updates and implementing security patches or accessing other AWS resources like SQS and SNS.
>
> [Cloud Conformity](https://www.cloudconformity.com/conformity-rules/EC2/instance-not-in-public-subnet.html)

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

## Deployment

Deployment strategies:

- single server deployment
- zero-downtime multi-server deployment
- capistrano-style and blue-green deployments

## Security

Your infrastructure as weak as the weakest server.

Use secure and encrypten communication.
Disable root login and use sudo.
Remove unused software, open only required ports.
Use the principle of least privilege.
Update the OS and installed software.
Use a properly configured firewall.
Make sure log files are populated and rotated.
Monitor logins and block suspect ip addresses.
Disable password based ssh authentication.
Use a nonstandard port for ssh.

## Bash

Memory usage:
```bash
free -f
```

Disk usage:
```bash
df -h
```

Date:
```bash
date
```

Get a service status:
```bash
service <service name> status
```

Watch file changes:
```bash
tail -f <file path>
```

## SSL

These files are required (`/etc/nginx/ssl/`):

- `dhparam4096.pem`
- `ssl.conf`
- `public_wild.pem`
- `private_wild.key`

Generating `dhparam`:
```bash
sudo openssl dhparam -out /etc/nginx/ssl/dhparam4096.pem 4096
```


## Best practices

### Credentials

Credentials, private keys must be passed through env variables.

To check: [credstash](https://github.com/fugue/credstash).

## Vocabulary

### Cowboy coding

Cowboy coding - working directly in a production environment, not documenting or incapsulating changes in code, and not having a way to roll back to a previous version.

### Subnet masks

Standard subnet masks:

- Class A: 255.0.0.0
- Class B: 255.255.0.0
- Class C: 255.255.255.0

10.0.0.0/16 - 65536 private IPv4 addresses.
10.0.0.0/24 - 256 private IPv4 addresses.

### Private network addresses

https://en.wikipedia.org/wiki/Private_network

```text
10.0.0.0 – 10.255.255.255
172.16.0.0 – 172.31.255.255
192.168.0.0 – 192.168.255.255
```

Private network: the shared [private networking on DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-set-up-and-use-digitalocean-private-networking) droplets is represented by a second interface on each server that has no internet access.

### Viartual machine vs Container

Viartual machine (VM) emulates an entire computer system, including hardware. Example: ViartualBox.

A container emulates the user space of an operating system. Examples: Docker, CoreOS.

## Links

[Practical VPC Design](https://medium.com/aws-activate-startup-blog/practical-vpc-design-8412e1a18dcc) by Amazon Web Services Startup Program
[Dev2Ops](http://dev2ops.org/)
[AWS blog](https://aws.amazon.com/blogs/aws/)
