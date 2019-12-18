class test:

    def __init__(self):
        pass

    def test_list(self, pkg_name="SDL", arch="x86_64"):
        x = "repoquery -q --qf='%{name} %{version}-%{release} %{arch} %{repoid}' --show-duplicates " + "{_name}".format(_name=pkg_name) + "--archlist=" + "{_arch}".format(_arch=arch)
        print(x)


if __name__ == "__main__":
    test().test_list()

