labels: Blog
        Tools
        Server
created: 2017-06-12T18:44
modified: 2017-11-28T11:06
place: Phuket, Thailand
comments: true

# Ansible notes

[TOC]

Agentless automation.

Ansible is a tool for provisioning servers, managing their configuration, and deploying applications.

Ansible = configuration management (Pupet, Chef) + deployment (Capistrano, Fabric) + ad-hoc task execution (Func, ssh).

Ansible aims to be:

- clear
- fast
- complete
- efficient
- secure

Initial release: 2012.

> When developers begin to think of infrastructure as part of their application, stability and performance become normative.
>
> Ansible for DevOps by Jeff Geerling

## Components

### Commands

Aka tasks.

Ad-hoc commands:
```bash
ansible <group> -b -m <command> -a <arguments>  # -b == become (root)
ansible <group> -m ping -u <username>
ansible mygroup -b -m yum -a "name=ntp state=present"
ansible .... --limit "192.168.60.1"  # limit to one instance, can use patterns
```

Verbose:
```bash
ansible ... -vvvv
```

Combine commands into playbooks.

#### Available modules

Aka "task plugins" or "library plugins".

See [Ansible modules](http://docs.ansible.com/ansible/modules_by_category.html):

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
- [`shell`](http://docs.ansible.com/ansible/shell_module.html) - ansible's command module is the preferred option for running commands on a host. However, command doesn't run the command via the remote shell `/bin/sh`, so options like `<>|&` and local environment variables won't work
- `raw` - raw command via ssh
- `script`
- [`set_fact`](http://docs.ansible.com/ansible/set_fact_module.html) - dynamically define variables
- [`debug`](http://docs.ansible.com/ansible/debug_module.html)

### Playbooks

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

[Handlers](http://docs.ansible.com/ansible/playbooks_intro.html#handlers-running-operations-on-change): Running Operations On Change.

#### `ansible-playbook` utility

`ansible-playbook` arguments:

- `--inventory`
- `--check`, check, but don't change (dry run)

#### Conditional statements

`when`:
```yaml
- apt:
  name: vim
  when: is_local
  # when: "(is_local is defined) and is_local"
  # when: "'ready' in my_result.stdout"
  # when: "my_result.stdout.find(another_var + '/some.js') == -1"
```

`changed_when`
`failed_when`
`wait_for` - e.g. wait for a server start listening on a port

#### Join playbooks

```yaml
- hosts: all
  tasks:
    ...
- include: playbook1.yml
- include: playbook2.yml
  vars:
    - myvar: myvalue
```

And can combine with `when` and `with` loop statements.

Or use ansible roles.

### Inventories

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

Can specify which inventory to use:
```bash
ansible-playbook myplaybook.yml -i inventories/myinventory
```

Inventories can be dynamic.

### Variables

[ansible variables](http://docs.ansible.com/ansible/playbooks_variables.html).

Use all lowercase letters.

Passing a variables file:
```bash
ansible-playbook playbook.yaml --extra-vars "@vars.yml"
```

[Registered variables](http://docs.ansible.com/ansible/playbooks_variables.html#registered-variables): save command stdout and stderr.

```yaml
- shell: <my_command>
  register:
    my_command_result
# "{{ my_command_result.stdout }}"
```

[Facts](http://docs.ansible.com/ansible/playbooks_variables.html#information-discovered-from-systems-facts) are information derived from speaking with your remote systems.

#### Passing configuration through ENV variables

Ansible set ENV variables -> the app loads configuration from ENV variables.

Using `~/.bash_profile`:
```yaml
- tasks
  - name: "Set an environment variable"
    lineinfile:
      path=~/.bash_profile
      regexp=^ENV_VAR=
      line=ENV_VAR=value
```
For system-wide use: `/etc/environment`.

Per play:
```yaml
- name:
  ...
  environment:
    my_env_var: my_value
```

Per shell command can use templates:
```jinja2
cd {{ app_home }} && ENV_KEY1={{ env_val1 }} ENV_KEY2={{ env_val2 }} {{ app_venv }}/bin/python myapp.py
```

Task:
```yaml
- shell: "{{ lookup('template', 'mytemplate.j2') }}"
```

Per supervisor config:
```jinja2
[program:myapp]
command={{ app_home }}/.venv/bin/python myapp.py
process_name=myapp
user={{ app_user }}
directory={{ app_home }}
environment=ENV_KEY1="{{ env_value1 }}",ENV_KEY2="{{ env_value2 }}"
```

#### Sensitive values

```text
ansible/variables/<env>-sensitive.yml
# (don't put it under git index)
# or specify them in command line:
ansible-playbook myplaybook.yml --extra-vars="myvar=myvalue"
```

So `vars_files` will look like:
```yaml
vars_files:
  - common.yml
  - "myservice_{{ env }}.yml"
  - "myservice_{{ env }}_sensitive.yml"
```

And `env` can be specified inside inventories:
```conf
# ...
[all:vars]
env=development
```

Variable prompt:
```yaml
vars_prompt:
  - name: username
    prompt: "What is username?"
    default: anonymous
  - name: password
    prompt: "What is password?"
    private: yes
    confirm: yes
```

Or use Ansible vault.

#### Ansible vault

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

String encryption:
```bash
ansible-vault --vault-password-file <password file> encrypt_string <some string>
```
This command will output a string ready to be included in a YAML file. 

File encryption:
```bash
ansible-vault --vault-password-file <password file> encrypt <file path>
```
Replace the file.

### Roles

Combines tasks, configuration, templates in one reusable package.

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

#### Ansible galaxy

A repository for roles.

```bash
ansible-galaxy init <role name>
```

## Usage

### Documentation

```bash
ansible-doc <module name>
```

### Debug

Verbose:
```bash
ansible-playbook playbook.yml -v
```

### Environments

Can specify environment inside inventories:
```conf
# ...
[all:vars]
env=development
```

And then use it when loading variables:
```yaml
vars_files:
  - "myservice_{{ env }}.yml"
```

### Tags

Allow to run (or exclude) subset of a playbook's tasks, roles, and handlers.

```yaml
roles:
  - {role: myrole, tags: ['install', 'setup']}
tasks:
  - name: "My task"
    someaction: someargs
    tags:
      - setup
```

```bash
ansible-playbook myplaybook.yml --tags "install"
ansible-playbook myplaybook.yml --skip-tags "install"
```

### Vagrant

Use for testing on development machine.

Vagrant is a server templating tool (other are Docker, Packer), create an image instead of configuring each server.

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

Example `Vagrantfile`:
```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/xenial64"

  # NFS shared folder
  # config.vm.synced_folder "./.shared/", "/var/townintel_shared", type: "nfs"

  config.vm.define "myinstance" do |app|
    app.vm.hostname = "myservice.mysite.com"
    app.vm.network:private_network, ip: "10.100.0.10"

    app.vm.provision "ansible" do |ansible|
        ansible.verbose = "v"
        ansible.inventory_path = "./inventories/development"
        ansible.playbook = "myservice.yml"
    end
  end

  # ...

end
```

!!! tip "Reach host machine"
    Host machine is available at `10.0.2.2`.

[Download Vagrant](https://www.vagrantup.com/downloads.html).

### AWS guide

See [Ansible AWS Guide](http://docs.ansible.com/ansible/guide_aws.html).
[Ansible for AWS](https://leanpub.com/ansible-for-aws) book.

### Run ansible through a bastion host

See [Running Ansible Through an SSH Bastion Host](http://blog.scottlowe.org/2015/12/24/running-ansible-through-ssh-bastion-host/) by Scott Lowe.

Example:

```text
# custom ssh configuration file
Host 10.10.10.*
  ProxyCommand ssh -W %h:%p bastion.example.com
  IdentityFile ~/.ssh/private_key.pem

Host bastion.example.com
  Hostname bastion.example.com
  User ubuntu
  IdentityFile ~/.ssh/private_key.pem
  ControlMaster auto
  ControlPath ~/.ssh/ansible-%r@%h:%p
  ControlPersist 5m
```

```text
# ansible.cfg
[ssh_connection]
ssh_args = -F ./ssh.cfg -o ControlMaster=auto -o ControlPersist=30m
control_path = ~/.ssh/ansible-%%r@%%h:%%p
```

Doesn't work for me ^, so I just put the configuration to `~/.ssh/config`.

### Python3

Specify it in inventories:
```conf
[all:vars]
ansible_python_interpreter=/usr/bin/python3
```

### Copy source code

One way:
```yaml
---
- tasks
  - name: "Synchronize the source"
      synchronize:
        dest: "/home/{{ user }}/{{ app }}/"
        src: "{{ item }}"
        rsync_opts:
          - "--exclude=*.pyc"
      become_user: "{{ user }}"
      with_items:
        - ../<some folder>
        - ../<some file>
      notify: server restart
```

## Examples

### Simple Python code deploy

```yaml
---
- name: Deploy
  hosts: <hosts>
  become: true
  vars_files:
    - variables/base.yml
  vars:
    - user: deploy
  tasks:
    - name: "apt-get update"
      apt:
        update_cache: yes
        cache_valid_time: 3600
    - name: "apt-get install"
      apt:
        name: "{{ item }}"
        state: latest
      with_items:
        - build-essential
        - virtualenv
        - python3-dev
    - name: "Create deploy group"
      group:
        name="{{ user }}"
        state=present
    - name: "Create deploy user"
      user:
        name="{{ user }}"
        shell=/bin/bash
        groups="{{ user }}"
        append=yes
    - name: "Synchronize the source"
      synchronize:
        dest: "/home/{{ user }}/<project name>/"
        src: "{{ item }}"
        rsync_opts:
          - "--exclude=*.pyc"
      become_user: "{{ user }}"
      with_items:
        - ../<source>
        - ../requirements.txt
      tags:
        - reload
    - name: "Install requirements"
      pip:
        requirements: "/home/{{ user }}/<project name>/requirements.txt"
        virtualenv: "/home/{{ user }}/.venv"
      become_user: "{{ user }}"
```

## Best practices

See [Ansible Best Practices](http://docs.ansible.com/ansible/playbooks_best_practices.html).

### Role names

`ansible-role-...` - easier to find on GitHub.

### Project structure

```text
- myproject
  - inventories/
  - roles/
  - variables/
  - playbook1.yml
  - playbook2.yml
  - Vagrantfile
```

## Vocabulary

See also [Ansible Glossary](http://docs.ansible.com/ansible/latest/glossary.html).

### Idempotence

Idempotence is the ability to run an operation which produces the same result whether run once or multiple times.

### ad-hoc

Ad-hoc - made or happening only for a particular purpose or need, not planned before it happens.

## Links

[Ansible for DevOps](https://www.amazon.com/Ansible-DevOps-Server-configuration-management/dp/098639341X) by Jeff Geerling
[Ansible documentation](http://docs.ansible.com/)
[Ansible blog](https://www.ansible.com/blog)
