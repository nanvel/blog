# Blog

See: [https://nanvel.name](https://nanvel.name)

Powered by [c2p2](https://github.com/nanvel/c2p2).

## Deploy

```bash
aws cloudformation deploy \
--stack-name nanvel-name \
--region ap-southeast-1 \
--capabilities CAPABILITY_NAMED_IAM \
--template-file stack.yml \
--parameter-overrides VPCArn=vpc-5f39d23a SubnetArn=subnet-e718d982 HostedZoneId=Z03618821Z1L9B8875OJ KeyName=nanvel
```

```bash
ansible-playbook ansible/setup_user.yml -i ansible/production -u ubuntu \
--vault-password-file <password file> \
--private-key <private key>
```

TODO:
- update ssl certificate
