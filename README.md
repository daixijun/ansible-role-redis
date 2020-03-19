Redis
=========

Ansible redis role

Requirements
--------------

* Centos/RHEL 6+
* Ansible 2.5+

Role Variables
--------------

```yaml
---
redis_version: 5.0.5
redis_upgrade: false
redis_download_url: https://mirror.azure.cn/redis/releases/redis-{{ redis_version }}.tar.gz
redis_data_dir: /var/lib/redis
redis_log_dir: /var/log/redis
redis_items:
  - port: 6379
    bind: 0.0.0.0
    password: ''
    unixsocket: ''
    timeout: 300
    databases: 16
    loglevel: notice
    logfile: /dev/null
    keepalive: 60
    maxclients: 10000
    maxmemory: 500mb
    maxmemory_policy: volatile-lru
    appendonly: 'yes'
    appendfilename: appendonly.aof
    appendfsync: everysec
    slaveof: ''  # eg: masterip masterport
    master_password: ''
    disabled_commands: []
```

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
- hosts: servers
  roles:
    - role: daixijun.redis
      redis_version: 5.0.5
```

License
-------

BSD

Author Information
------------------

Xijun Dai <daixijun1990@gmail.com>

已知问题
------------------

* Sentinel在运行中会重写配置文件，这块没法做到幂等性
