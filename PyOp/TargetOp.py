from fabric import Connection
from GetConfig import GetConfig
from DbOp import DbOp

import time
import datetime


class TargetOp:
    def __init__(self, host_ip, host_password):
        self.conf = GetConfig().get_config()
        self.target_host = self.conf.get('target_host')
        self.target_host_ip = host_ip
        self.target_host_port = self.target_host.get('port')
        self.target_host_user = self.target_host.get('user')
        self.target_host_pwd = host_password
        self.db_inst = DbOp()
        self.db_inst.create_installed_table()
        self.db_inst.create_update_table()

    def conditional_decorator(self, condition):
        def decorator(func):
            if not condition:
                return func
        return decorator

    def connect(self):
        connect = Connection(
            host=self.target_host_ip,
            # host='1.1.1.1',
            port=22,
            user='root',
            connect_kwargs={
                "password": self.target_host_pwd,
            },
            connect_timeout=5
        )
        return connect

    def chk_connect(self):
        status = False
        connect_hdle = self.connect()
        try:
            connect_hdle.open()
        except Exception:
            # raise TimeoutError("SSH connection failed !")
            # status = False
            raise Exception("SSH connection failed !")
            status = False
        else:
            status = True
        finally:
            connect_hdle.close()
            return status

    def run_cmd(self, cmd, warn=False):
        try:
            result = self.connect().run(cmd, warn=warn)
            # result = connect.run(r'rpm -qa --queryformat "%{NAME} %{EPOCH} %{VERSION} %{RELEASE} %{ARCH}\n"')
            return result
        except Exception as err:
            raise err("Command execution Failed !")
        finally:
            self.connect().close()

    def run_cmd_mod(self, ip, password, cmd, warn=False):
        try:
            if self.chk_connect_mod():
                result = self.connect_mod(ip, password).run(cmd, warn=warn)
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
                current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                for index, each in enumerate(list_info):
                    if each:
                        dict_each = dict()
                        list_each = each.split()
                        dict_each = {
                            'NAME': list_each[0],
                            'VERSION': list_each[1],
                            'ARCH': list_each[2],
                            'TIME': current_time,
                            'IP': self.target_host_ip
                        }
                        # print(dict_each)
                        list_info[index] = dict_each
                        # self.db_inst.insert_installed_table(dict_each)
                # print(list_info)
                if list_info:
                    # print(list_info)
                    return list_info
                else:
                    raise Exception('Get installed packages info failed !')

    def installed_info_into_db(self):
        pkg_info_list = self.query_installed_pkg()
        # print(pkg_info_list)
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
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            for index, each in enumerate(list_info):
                if each:
                    # print(each)
                    list_each = each.split()
                    # print(list_each)
                    dict_each = {
                        'NAME': list_each[0],
                        'VERSION': list_each[1],
                        'ARCH': list_each[2],
                        'REPO': list_each[3],
                        'TIME': current_time,
                        'IP': self.target_host_ip
                    }
                    # if dict_each['REPO'] != "base":
                    #     dict_each.update({'DETAIL': 'More'})
                    # else:
                    #     dict_each.update({'DETAIL': 'Base'})
                    # print(dict_each)
                    list_info[index] = dict_each
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

    def update_info_details(self, pkg_name="SDL"):
        chk_words = ['Command exited with status', "= stdout =", '(no stderr)']
        info = self.run_cmd(
            "repoquery -q --qf='%{name} %{version}-%{release} %{arch} %{repoid}' --show-duplicates " +
            "{_name}\n".format(_name=pkg_name), warn=True
        )
        list_info = str(info).split("\n")
        # print(list_info)
        for chk_word in chk_words:
            for each in list_info:
                if chk_word in each:
                    list_info.remove(each)
        list_info = [each for each in list_info if each != '']
        if list_info:
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            for index, each in enumerate(list_info):
                if each:
                    # print(each)
                    list_each = each.split()
                    # print(list_each)
                    dict_each = {
                        'NAME': list_each[0],
                        'VERSION': list_each[1],
                        'ARCH': list_each[2],
                        'REPO': list_each[3],
                        'TIME': current_time,
                        'IP': self.target_host_ip
                    }
                    # if dict_each['REPO'] != "base":
                    #     dict_each.update({'DETAIL': 'More'})
                    # else:
                    #     dict_each.update({'DETAIL': 'Base'})
                    # print(dict_each)
                    list_info[index] = dict_each
            # print(list_info)
            return list_info
        else:
            raise Exception('None Packages update detail information !')
        # print(list_info)

    def update_info_details_into_db(self):
        update_info_list = self.update_info_details()
        try:
            self.db_inst.insert_update_info_details(update_info_list)
        except Exception as err:
            raise err("DB Operation Failed !")
