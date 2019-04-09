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
redis_port: 6379
redis_bind: 127.0.0.1
redis_unixsocket: ''
redis_timeout: 300
redis_databases: 16
redis_data_dir: /var/lib/redis/{{ redis_port }}
redis_loglevel: notice
redis_logfile: /var/log/redis_{{ redis_port }}.log
redis_keepalive: 60
# ===== limit =======
redis_maxclients: 10000
redis_maxmemory: 500mb
redis_maxmemory_policy: volatile-lru
# ===== persistence =====
redis_appendonly: 'yes'
redis_appendfilename: appendonly.aof
redis_appendfsync: everysec
# ===== slave ======
redis_slaveof: '' # eg: masterip masterport
redis_master_password: ''
# ===== security ======
redis_disabled_commands: []
redis_password: ''
```

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: daixijun.redis, redis_port: 6379 }

License
-------

BSD

Author Information
------------------

Xijun Dai <daixijun1990@gmail.com>
