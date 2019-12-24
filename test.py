from time import time
import datetime


class test:

    def __init__(self):
        pass

    def test_list(self, pkg_name="SDL", arch="x86_64"):
        x = "repoquery -q --qf='%{name} %{version}-%{release} %{arch} %{repoid}' --show-duplicates " + "{_name}".format(_name=pkg_name) + "--archlist=" + "{_arch}".format(_arch=arch)
        print(x)

    def time_record(self):
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(current_time)


if __name__ == "__main__":
    # test().test_list()
    test().time_record()

