from fabric import Connection
from GetConfig import GetConfig
from DbOp import DbOp


class TargetHost:
    def __init__(self):
        self.conf = GetConfig().get_config()
        self.target_host = self.conf.get('target_host')
        # print(self.target_host)
        self.target_host_ip = self.target_host.get('ip')
        self.target_host_port = self.target_host.get('port')
        self.target_host_user = self.target_host.get('user')
        self.target_host_pwd = self.target_host.get('pwd')
        self.db_inst = DbOp()
        self.db_inst.create_installed_table()
        self.db_inst.create_update_table()

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

    def run_cmd(self, cmd, warn=False):
        try:
            result = self.connect().run(cmd, warn=warn)
            # result = connect.run(r'rpm -qa --queryformat "%{NAME} %{EPOCH} %{VERSION} %{RELEASE} %{ARCH}\n"')
            return result
        except Exception as err:
            raise err("Command execution Failed !")
        finally:
            self.connect().close()

    def query_installed_pkg(self):
        # info = self.run_cmd(r'rpm -qa --queryformat "%-60{NAME} %-12{EPOCH} %-25{VERSION} %-35{RELEASE} %-8{ARCH}\n"')
        # info = self.run_cmd(r'rpm -qa --queryformat "%{NAME} %{EPOCH} %{VERSION} %{RELEASE} %{ARCH}\n"')
        chk_words = ['Command exited with status', "stdout", '(no stderr)']
        info = self.run_cmd('rpm -qa --queryformat "%{NAME} %{VERSION}-%{RELEASE} %{ARCH}\n"')
        info = str(info)
        if info:
            list_info = info.split('\n')
            for chk_word in chk_words:
                for each in list_info:
                    if chk_word in each:
                        list_info.remove(each)
            list_info = [each for each in list_info if each != '']
            if list_info:
                for index, each in enumerate(list_info):
                    if each:
                        dict_each = dict()
                        list_each = each.split()
                        dict_each = {
                            'NAME': list_each[0],
                            'VERSION': list_each[1],
                            'ARCH': list_each[2]
                        }
                        # print(dict_each)
                        list_info[index] = dict_each
                        # self.db_inst.insert_installed_table(dict_each)
                # print(list_info)
                if list_info:
                    return list_info
                else:
                    raise Exception('Get installed packages info failed !')

    def installed_pkg_list(self):
        pass

    def installed_info_into_db(self):
        pkg_info_list = self.query_installed_pkg()
        try:
            self.db_inst.insert_installed_info(pkg_info_list)
        except Exception as err:
            raise err("DB Operation Failed !")

    def update_pkg_info(self):
        chk_words = ['Command exited with status', "= stdout =", '(no stderr)']
        # info = self.run_cmd('yum list updates| xargs -n3 | column -t\n', warn=True)
        info = self.run_cmd(
            'repoquery -q -a --qf="%{name} %{version}-%{release} %{arch} %{repoid}" --pkgnarrow=updates\n', warn=True
        )
        info = str(info)
        list_info = info.split('\n')
        for chk_word in chk_words:
            for each in list_info:
                if chk_word in each:
                    list_info.remove(each)
        list_info = [each for each in list_info if each != '']
        if list_info:
            for index, each in enumerate(list_info):
                if each:
                    # print(each)
                    list_each = each.split()
                    # print(list_each)
                    dict_each = {
                        'NAME': list_each[0],
                        'VERSION': list_each[1],
                        'ARCH': list_each[2],
                        'REPO': list_each[3]
                    }
                    # print(dict_each)
                    list_info[index] = dict_each
                    # self.db_inst.insert_installed_table(dict_each)
            # print(list_info)
            return list_info
        else:
            raise Exception('No packages need to update !')

    def update_info_into_db(self):
        update_info_list = self.update_pkg_info()
        try:
            self.db_inst.insert_update_info(update_info_list)
        except Exception as err:
            raise err("DB Operation Failed !")


    def update_pkg_info_backup(self):
        # pkg_info_list = self.connect(r'yum --showduplicates list "tar.*"')
        # pkg_info_list = self.installed_pkg_list()
        # update_info_list = []
        # for each in pkg_info_list:
        #     pkg_name = each['NAME']
        #     print(pkg_name)
        #     update_info = self.run_cmd("yum --showduplicates list %s", pkg_name)
        #     print(update_info)
        update_info_list = []
        pkg_info_list = self.query_installed_pkg()
        for index, pkg in enumerate(pkg_info_list):
            pkg_name = pkg['NAME']
            update_info = self.run_cmd("yum --showduplicates list " + pkg_name)
            print(update_info)
            update_info = str(update_info)
            if update_info:
                cont_list = update_info.split('\n')
                for each in cont_list:
                    ori_list = []
                    updt_list = []
                    if pkg_name in each:
                        if '@anaconda' in each:
                            ori_list = each.split()
                        elif 'base' in each:
                            updt_list = each.split()
                    if ori_list and updt_list:
                        if ori_list[1] == updt_list[1]:
                            dict_info = {'NAME': updt_list[0], 'VERSION': updt_list[1]}
                            update_info_list.append(dict_info)
        if update_info_list:
            return update_info_list
        else:
            raise Exception('Get update info failed !')




if __name__ == "__main__":
    target_host = TargetHost()
    # install_val = target_host.query_installed_pkg()
    # list_val = target_host.installed_pkg_list()
    # update_val = target_host.update_pkg_info()
    # print(install_val)
    # print(list_val)
    target_host.installed_info_into_db()
    target_host.update_info_into_db()
    # target_host.installed_info_into_db()

