daixijun.redis
=========

[![Build Status](https://github.com/daixijun/ansible-role-redis/workflows/build/badge.svg)](https://github.com/daixijun/ansible-role-redis/actions)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-daixijun.redis-660198.svg?style=flat)](https://galaxy.ansible.com/daixijun/redis/)
[![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/daixijun/ansible-role-redis?sort=semver)](https://github.com/daixijun/ansible-role-redis/tags)

配置Redis环境

* [x] 主从集群
* [x] 哨兵(Sentinel)集群
* [ ] Redis Cluster
* [x] Redis 6.0 以上版本支持TLS加密

Requirements
--------------

* Centos/RHEL 7+
* Ansible 2.9+

Role Variables
--------------

[defaults/main.yaml](./defaults/main.yml)

Example Playbook
----------------

* 主从集群配置 [converge.yml](./molecule/default/converge.yml)
* 哨兵集群配置 [converge.yml](./molecule/sentinel/converge.yml)
* 主从集群开启TLS [converge.yml](./molecule/tls/converge.yml)
* 哨兵模式下主从开启TLS [converge.yml](./molecule/sentinel_tls/converge.yml)

License
-------

BSD

Author Information
------------------

Xijun Dai <daixijun1990@gmail.com>

已知问题
------------------

* Sentinel在运行中会重写配置文件，这块没法做到幂等性
