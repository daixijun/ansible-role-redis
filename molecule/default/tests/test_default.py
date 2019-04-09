import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_redis_installed(host):
    package_name = _get_redis_package_name(host.system_info.distribution)
    package = host.package(package_name)

    assert package.is_installed


def _get_redis_package_name(host_distro):
    return {
        "centos": "redis",
        "ubuntu": "redis-server",
        "debian": "redis-server"
    }.get(host_distro, "redis")


def test_redis_running(host):
    service = host.service('redis_6379')

    assert service.is_running
