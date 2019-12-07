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

    def connect(self):
        connect = Connection(
            host=self.target_host_ip,
            port=self.target_host_port,
            user=self.target_host_user,
            connect_kwargs={
                "password": self.target_host_pwd,
            },
            connect_timeout=10
        )
        return connect

    def run_cmd(self, cmd):
        try:
            result = self.connect().run(cmd)
            # result = connect.run(r'rpm -qa --queryformat "%{NAME} %{EPOCH} %{VERSION} %{RELEASE} %{ARCH}\n"')
            return result
        except Exception as err:
            raise err("Command execution Failed !")
        finally:
            self.connect().close()

    def installed_pkg_info(self):
        # info = self.run_cmd(r'rpm -qa --queryformat "%-60{NAME} %-12{EPOCH} %-25{VERSION} %-35{RELEASE} %-8{ARCH}\n"')
        # info = self.run_cmd(r'rpm -qa --queryformat "%{NAME} %{EPOCH} %{VERSION} %{RELEASE} %{ARCH}\n"')
        info = self.run_cmd('rpm -qa --queryformat "%{NAME} %{VERSION}%{RELEASE} %{ARCH}\n"')
        info = str(info)
        if info:

            return info
        else:
            raise Exception('Get installed packages info failed !')

    def installed_info_list(self):
        chk_words = ['Command exited with status', "stdout", '(no stderr)']
        list_info = []
        list_info = self.installed_pkg_info().split('\n')

        if list_info:
            for chk_word in chk_words:
                for each in list_info:
                    if chk_word in each:
                        list_info.remove(each)
            # if not any(bad_word in line for bad_word in bad_words):
            # list_info = [each for each in list_info if ]
            list_info = [each for each in list_info if each != '']
            if list_info:
                return list_info
            else:
                raise Exception('Get installed packages info failed !')
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
    install_val = target_host.installed_pkg_info()
    list_val = target_host.installed_info_list()
    # update_val = target_host.update_pkg_info()
    # print(install_val)
    print(list_val)

