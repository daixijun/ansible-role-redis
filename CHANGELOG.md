# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

### [2.0.2](https://github.com/daixijun/ansible-role-redis/compare/v2.0.1...v2.0.2) (2020-07-27)


### Bug Fixes

* 修复6.0以上版本在未开启TLS功能时,配置文件中包含TLS相关配置导致slave节点crash的问题 ([395422b](https://github.com/daixijun/ansible-role-redis/commit/395422bf5bae674b130eb3b89be085070d68ff79))
* **sentinel:** 修复 sentinel max open files 默认4096的问题 ([1884528](https://github.com/daixijun/ansible-role-redis/commit/1884528e10cbdafb5826b187cf4568a73e62fdb0))

### [2.0.1](https://github.com/daixijun/ansible-role-redis/compare/v2.0.0...v2.0.1) (2020-06-22)


### Bug Fixes

* 更新默认版本为 6.0.5 ([a2539a3](https://github.com/daixijun/ansible-role-redis/commit/a2539a37a3db6f8a24cfe286624826ef7d7a5dc0))
* **galaxy:** 去除依赖 ([1041722](https://github.com/daixijun/ansible-role-redis/commit/1041722007ee97db036aa911a73c400b0144d308))

## [2.0.0](https://github.com/daixijun/ansible-role-redis/compare/v1.0.0...v2.0.0) (2020-04-23)


### ⚠ BREAKING CHANGES

* 移除redis_sentinel_monitors 变量
- 移除 `redis_sentinel_monitors` 变量,使用 `redis_sentinel_monitor_xxx` 配置单实例
- xxx_ssl_enable 变量修改为 `xxx_ssl`

### Features

* 移除 redis_sentinel 多实例配置 ([a51f108](https://github.com/daixijun/ansible-role-redis/commit/a51f108fdf2951ef63d397efc50ad74da3fa7c80))


### Bug Fixes

* 修复老版本 service 配置文件路径问题 ([a9ad3a6](https://github.com/daixijun/ansible-role-redis/commit/a9ad3a69ea71953921ec9cb15d7e16c69690d5b7))

## [1.0.0](https://github.com/daixijun/ansible-role-redis/compare/v0.0.6...v1.0.0) (2020-04-07)


### ⚠ BREAKING CHANGES

* 移除`redis_items`变量，不再支持部署多个实例

### Features

* 添加 Diffie-Hellman ([278ca98](https://github.com/daixijun/ansible-role-redis/commit/278ca98b0756521bb3c994c6d1bf78625d0dc017))


### Bug Fixes

* **sysctl:** 修改 net.core.somaxconn 值为 32768 ([f8206e6](https://github.com/daixijun/ansible-role-redis/commit/f8206e61a42147e1d5c707df022fa2b6ee41e4d4))
* 补全变量名称 ([9f802c5](https://github.com/daixijun/ansible-role-redis/commit/9f802c584f6cd572b20d2907a34b696a97df75e0))
* **sentinel:** 修复测试时移除的条件判断 ([c51a070](https://github.com/daixijun/ansible-role-redis/commit/c51a07075797677ceb42b8af5fb00ae4f19cb9bb))
* **sentinel:** 修改 down-after-milliseconds 默认时间为 1 杪 ([26dbe41](https://github.com/daixijun/ansible-role-redis/commit/26dbe41f41e360157ecdac74f25ca777de869f1b))
* 移除部分日志输出 ([3fa2558](https://github.com/daixijun/ansible-role-redis/commit/3fa2558783f121b27aae503ff56d525f3983d3f8))


* 整个项目重构 ([b572685](https://github.com/daixijun/ansible-role-redis/commit/b572685800f83700ecc987dc7da08f087018f139))

### [0.0.6](https://github.com/daixijun/ansible-role-redis/compare/v0.0.5...v0.0.6) (2020-03-19)


### Features

* add sentinel ([2132269](https://github.com/daixijun/ansible-role-redis/commit/2132269c2a6c54517b54156a1a6e01a3205eb719))


### Bug Fixes

* 启动前调整 somaxconn 参数为512 ([04a77cd](https://github.com/daixijun/ansible-role-redis/commit/04a77cd55c1fde67a29d0ad540490f0a9e079a80))

### [0.0.5](https://github.com/daixijun/ansible-role-redis/compare/v0.0.4...v0.0.5) (2020-01-03)


### Features

* 修改安装包下载方式 ([dbdbca3](https://github.com/daixijun/ansible-role-redis/commit/dbdbca31ce689c04d66b12d0ee594fabfda0a378))
