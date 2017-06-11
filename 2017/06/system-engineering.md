labels: Draft
created: 2017-06-08T16:38
modified: 2017-06-08T16:38
place: Phuket, Thailand
comments: true

# System engineering

Amazon Route 53 - a highly available and scalable cloud Domain Name System (DNS) web service.
AWS EC2 instance - virtual computing environment.
AWS AMI - preconfigured templates for instances (operation system and additional software). You can launch different types of instances from a single AMI.

## AWS ECS

https://news.ycombinator.com/item?id=12058929

[Our Nightmare2 on Amazon ECS](http://www.appuri.com/blog/-our-docker-nightmare-on-amazon-ecs/) by Bilal Aslam at appuri blog.
[Rebuilding Our Infrastructure with Docker, ECS, and Terraform](https://segment.com/blog/rebuilding-our-infrastructure/) by Calvin French-Owen at segment.
[The Seven Biggest Challenges of Deployment to ECS](https://convox.com/blog/ecs-challenges/) on The Convox blog.

!!! caution "Leaking environment variables to CloudTrail"
    See [Our Nightmare2 on Amazon ECS](http://www.appuri.com/blog/-our-docker-nightmare-on-amazon-ecs/). When you start a new service, it logs the service definition including environment variables to CloudTrail!

## To investigate

ECS vs Kubernetes (k8s).
ECS passing configuration.
ECS service discovery without load balancers.

## Best practices

### Secrets

Secrets (credentials) must be passed through env variables.

To check: [credstash](https://github.com/fugue/credstash).
