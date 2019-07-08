import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


def test_redis_installed(host):
    f = host.file("/usr/local/bin/redis-server")

    assert f.exists
    assert f.is_file


def test_redis_user_and_group(host):
    user = host.user("redis")
    group = host.group("redis")

    assert user.name == "redis"
    assert user.shell == "/sbin/nologin"
    assert user.home == "/var/lib/redis"
    assert user.group == "redis"

    assert group.exists


def test_redis_6379_running_and_enabled(host):
    service = host.service("redis_6379")

    assert service.is_running
    assert service.is_enabled


def test_redis_6380_running_and_enabled(host):
    service = host.service("redis_6380")

    assert service.is_running
    assert service.is_enabled
