import sqlite3
from GetConfig import GetConfig


class DbOp:
    def __init__(self):
        self.conf = GetConfig().get_config()
        self.db = self.conf.get('db')
        print(self.db)
        self.db_name = self.db.get('db_name')

    def connect_db(self):
        try:
            conn = sqlite3.connect(self.db_name)
        except Exception as err:
            raise err('Database connection failed !')
        else:
            return conn

    def create_installed_table(self):
        conn = self.connect_db()
        cur = conn.cursor()
        try:
            create_tb_cmd = '''
            CREATE TABLE IF NOT EXISTS INSTALLED_INFO
            (NAME TEXT PRIMARY KEY NOT NULL,
            VERSION TEXT NOT NULL,
            ARCH TEXT NOT NULL,
            CTIME TEXT NOT NULL,
            IP TEXT NOT NULL,
            unique (NAME, VERSION));
            '''
            cur.execute(create_tb_cmd)
            conn.commit()
        except Exception as err:
            raise err('Installed table operation failed !')
        finally:
            cur.close
            conn.close()

    def create_update_table(self):
        conn = self.connect_db()
        cur = conn.cursor()
        try:
            create_tb_cmd = '''
            CREATE TABLE IF NOT EXISTS UPDATE_INFO
            (NAME TEXT PRIMARY KEY NOT NULL,
            VERSION TEXT NOT NULL,
            ARCH TEXT NOT NULL,
            REPO TEXT NOT NULL,
            CTIME TEXT NOT NULL,
            IP TEXT NOT NULL,
            unique (NAME, VERSION));
            '''
            cur.execute(create_tb_cmd)
            conn.commit()
        except Exception as err:
            raise err('Update table operation failed !')
        finally:
            cur.close
            conn.close()

    def insert_installed_info(self, dict_pkgs):
        conn = self.connect_db()
        cur = conn.cursor()
        try:
            # cur.execute(
            #     'INSERT OR REPLACE INTO INSTALLED (NAME, VERSION, ARCH) VALUES (:NAME, :VERSION, :ARCH)', dict_pkgs
            # )
            cur.executemany(
                'INSERT OR REPLACE INTO INSTALLED_INFO (NAME, VERSION, ARCH, TIME, IP) '
                'VALUES (:NAME, :VERSION, :ARCH, :TIME, :IP)', dict_pkgs
            )
        except Exception as err:
            raise err('Insert table operation failed !')
        finally:
            conn.commit()
            cur.close
            conn.close()

    def insert_update_info(self, dict_pkgs):
        conn = self.connect_db()
        cur = conn.cursor()
        try:
            # cur.execute(
            #     'INSERT OR REPLACE INTO INSTALLED (NAME, VERSION, ARCH) VALUES (:NAME, :VERSION, :ARCH)', dict_pkgs
            # )
            cur.executemany(
                'INSERT OR REPLACE INTO UPDATE_INFO (NAME, VERSION, ARCH, REPO, TIME, IP) '
                'VALUES (:NAME, :VERSION, :ARCH, :REPO, :TIME, :IP)', dict_pkgs
            )
        except Exception as err:
            raise err('Insert table operation failed !')
        finally:
            conn.commit()
            cur.close
            conn.close()

    def insert_update_info_details(self, dict_pkgs):
        conn = self.connect_db()
        cur = conn.cursor()
        try:
            # cur.execute(
            #     'INSERT OR REPLACE INTO INSTALLED (NAME, VERSION, ARCH) VALUES (:NAME, :VERSION, :ARCH)', dict_pkgs
            # )
            cur.executemany(
                'INSERT OR REPLACE INTO UPDATE_INFO_DETAILS (NAME, VERSION, ARCH, REPO，TIME, IP) '
                'VALUES (:NAME, :VERSION, :ARCH, :REPO, :TIME, :IP)', dict_pkgs
            )
        except Exception as err:
            raise err('Insert table operation failed !')
        finally:
            conn.commit()
            cur.close
            conn.close()


if __name__ == "__main__":
    db = DbOp()
    db.create_installed_table()
    db.insert_installed_table()
