from fabric import Connection
from GetConfig import GetConfig


class TargetHost:
    def __init__(self):
        self.conf = GetConfig().get_config()
        self.target_host = self.conf.get('target_host')
        print(self.target_host)
        self.target_host_ip = self.target_host.get('ip')
        self.target_host_port = self.target_host.get('port')
        self.target_host_user = self.target_host.get('user')
        self.target_host_pwd = self.target_host.get('pwd')

    def connect(self, cmd):
        connect = Connection(
            host=self.target_host_ip,
            port=self.target_host_port,
            user=self.target_host_user,
            connect_kwargs={
                "password": self.target_host_pwd,
            },
            connect_timeout=10
        )
        result = connect.run(cmd)
        # result = connect.run(r'rpm -qa --queryformat "%{NAME} %{EPOCH} %{VERSION} %{RELEASE} %{ARCH}\n"')
        return result

    def installed_pkg_info(self):
        info = self.connect(r'rpm -qa --queryformat "%-60{NAME} %-12{EPOCH} %-25{VERSION} %-35{RELEASE} %-8{ARCH}\n"')
        if info:
            return info
        else:
            raise Exception('Get installed packages info failed !')

    def update_pkg_info(self):
        # info = self.connect(r'yum --showduplicates list "tar.*"')
        info = self.connect(r'yum -C check-update')
        if info:
            return info
        else:
            raise Exception('Get update info failed !')





if __name__ == "__main__":
    target_host = TargetHost()
    # install_val = target_host.installed_pkg_info()
    update_val = target_host.update_pkg_info()


