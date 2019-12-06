from pyhocon import config_parser
from pyhocon import ConfigFactory


class GetConfig:
    def __init__(self):
        pass

    def get_config(self):
        try:
            conf = ConfigFactory.parse_file('./conf/config.conf')
        except Exception as err:
            raise err("Configuration Failed !")
        else:
            return conf





if __name__ == "__main__":
    conf = GetConfig().get_config()
    print(conf)
    target_host_conf = conf.get('target_host')
    print(target_host_conf)
    target_host_pwd = target_host_conf.get('pwd')
    print(target_host_pwd)
    print(type(target_host_pwd))
