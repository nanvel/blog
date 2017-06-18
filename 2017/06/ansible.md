labels: Draft
		Tools
created: 2017-06-12T18:44
modified: 2017-06-18T22:50
place: Phuket, Thailand
comments: true

# Ansible notes

[TOC]

Agentless automation.

A tool for provisioning servers, managing their configuration, and deploying applications.

Ansible = configuration management (Pupet, Chef) + deployment (Capistrano, Fabric) + ad-hoc task execution (Func, ssh).

Ansible aims to be:

- clear
- fast
- complete
- efficient
- secure

> When developers begin to think of infrastructure as part of their application, stability and performance become normative.
>
> Ansible for DevOps by Jeff Geerling

## Commands

Ping:
```bash
ansible <group> -m ping -u <username>
```

Verbose:
```bash
ansible ... -vvvv
```

Run an executable:
```bash
ansible <group> -a "free -m" -u <username>
```

Setup details:
```
ansible <group> -m setup
```

Ad-hoc commands:
```bash
ansible <group> -b -m <command> -a <arguments>  # -b == become (root)
ansible mygroup -b -m yum -a "name=ntp state=present"
ansible .... --limit "192.168.60.1"  # limit to one instance, can use patterns
```

## Playbook syntax

Playbook - a set of tasks (plays) that will be run against a particular server or set of servers.

Example:
```yaml
---
- hosts: all
  become: yes
  vars_files:
    - vars.yml
  vars:
    - myvar: myvalue
  pre_tasks:
    ...
  tasks:
	- name: Install ... {{ myvar }}
	  yum: ...
	  notity:
	    - do something
	- include: my-tasks.yml
  post_tasks:
    ...
  handlers:
    - do something
      ...
    - include: my-handlers.yml
```

Privileged access (use sudo):
```
become: yes
```

Create a user group:
```bash
ansible <group> -b -m group -a "name=<user group> state=present"  # use state=absent to disable
```

Create a user:
```bash
ansible <group> -b -m user -a "name=myuser group=<user group> createhome=yes generate_ssh_key=yes"
# for delete, just use state=absent remove=yes
```

ansible-playbook arguments:

- `--inventory`
- `--check`, check, but don't change (dry run)

[Handlers](http://docs.ansible.com/ansible/playbooks_intro.html#handlers-running-operations-on-change): Running Operations On Change.

### Modules

Also known as "task plugins" or "library plugins".

See [Ansible modules](http://docs.ansible.com/ansible/modules_by_category.html).

- `yum`
- [`apt`](http://docs.ansible.com/ansible/apt_module.html)
- `package`
- `easy_install`
- `service`
- `group`
- [`user`](http://docs.ansible.com/ansible/user_module.html)
- [`copy`](http://docs.ansible.com/ansible/copy_module.html)
- [`get_url`](http://docs.ansible.com/ansible/get_url_module.html) - download files
- `fetch`
- `unarchive`
- [`file`](http://docs.ansible.com/ansible/file_module.html) - create directories and files
- `copy` - can copy app folder
- `cron`
- [`lineinfile`](http://docs.ansible.com/ansible/lineinfile_module.html) - find a line using regexp and replace
- [`shell`](http://docs.ansible.com/ansible/shell_module.html) - ansible's command module is the preferred option for running commands on a host. However command doesn't run the command via the remote shell `/bin/sh`, so options like `<>|&` and local environment variables won't work
- `raw` - raw command via ssh
- `script`
- [`set_fact`](http://docs.ansible.com/ansible/set_fact_module.html) - dynamically define fariables
- [`debug`](http://docs.ansible.com/ansible/debug_module.html)

### Conditional statements

`when`:
```yaml
- apt:
	name: vim
  when: is_local
  # when: "(is_local is defined) and is_local"
  # when: "'ready' in my_result.stdout"
```

`changed_when`
`failed_when`
`wait_for` - wait for a server start listening on a port

## Inventory file syntax

```text
[app]
102.168.60.1
102.168.60.2

[db]
102.168.60.3

# group "multi"
[multi:children]
app
db

[multi:vars]
ansible_ssh_user=myuser
ansible_ssh_private_key_file=~/...
```

## Roles

```text
my_role/
  meta/
    main.yml
  tasks/
    main.yml
```

```yaml
- hosts: all
  roles:
    - my_role
```

Meta:
```yaml
---
dependencied: []
```

### Ansible galaxy

```bash
ansible-galaxy init <role name>
```

## Tips

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

### Vagrant

Working with [Vagrant](https://www.vagrantup.com/):
```bash
vagrant box add <repository>/<image>
vagrant init <repository>/<image>
vagrant up
vagrant ssh
vagrant halt  # shut down
vagrant destroy  # completely destroy the box
vagrant ssh-config  # ssh details
```

Vagrant features:

- network interface management
- shared folder management
- multi-machine management
- provisioning

[Download Vagrant](https://www.vagrantup.com/downloads.html).

### ENV variables

```yaml
- tasks
  - name: "Set an environment variable"
    lineinfile:
    	path=~/.bash_profile
    	regexp=^ENV_VAR=
    	line=ENV_VAR=value
```

Can use `register` to store env variable and use later.
For system-wide use: `/etc/environment`.

Per play:
```yaml
- name:
  ...
  environment:
    my_env_var: my_value
```

### Reach host machine

Use `10.0.2.2`.

### Join playbooks

```yaml
- hosts: all
  tasks:
    ...
- include: playbook1.yml
- include: playbook2.yml
```

## Best practices

See [Ansible Best Practices](http://docs.ansible.com/ansible/playbooks_best_practices.html).

### Documentation

```bash
ansible-doc <module name>
```

### Variables

Use all lowercase letters.

Passing variables:
```
ansible-playbook playbook.yaml --extra-vars "@vars.yml"
```

Conditional:
```
vars_files:
  - "myvars_{{ myvar }}".yml
```

See [playbook variables](http://docs.ansible.com/ansible/playbooks_variables.html).

Variables precedence:

- role defaults
- inventory file or script group vars
- inventory group_vars/all
- playbook group_vars/all
- inventory group_vars/*
- playbook group_vars/*
- inventory file or script host vars
- inventory host_vars/*
- playbook host_vars/*
- host facts
- play vars
- play vars_prompt
- play vars_files
- role vars (defined in role/vars/main.yml)
- block vars (only for tasks in block)
- task vars (only for the task)
- role (and include_role) params
- include params
- include_vars
- set_facts / registered vars
- extra vars (always win precedence)

[Registered variables](http://docs.ansible.com/ansible/playbooks_variables.html#registered-variables): save command stdout and stderr.

```yaml
- shell: <my_command>
  register:
    my_command_result
# "{{ my_command_result.stdout }}"
```

[Facts](http://docs.ansible.com/ansible/playbooks_variables.html#information-discovered-from-systems-facts) are information derived from speaking with your remote systems.

### Vaults

Encryption: AES-256.

Edit:
```
ansible-vault edit
```

Run:
```bash
ansible-playbook playbook.yml --ask-vault-pass
```

Works faster with:
```bash
pip install cryptography
```

### Debug

Verbose:
```bash
ansible-playbook playbook.yml -v
```

### Role names

`ansible-role-...` - easier to find on GitHub.

## Vocabulary

### Idempotence

Idempotence is the ability to run an operation which produces the same result whether run once or multiple times.

### ad-hoc

Ad-hoc - made or happening only for a particular purpose or need, not planned before it happens.

## Links

[Ansible for DevOps](https://www.amazon.com/Ansible-DevOps-Server-configuration-management/dp/098639341X) by Jeff Geerling
[Ansible documentation](http://docs.ansible.com/)
