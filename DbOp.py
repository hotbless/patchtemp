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
        c = conn.cursor()
        try:
            create_tb_cmd = '''
            CREATE TABLE IF NOT EXISTS INSTALLED
            (NAME TEXT,
            VERSION TEXT,
            ARCH TEXT);
            '''
            c.execute(create_tb_cmd)
            conn.commit()
        except Exception as err:
            raise err('Installed table operation failed !')
        finally:
            c.close
            conn.close()

    def insert_installed_table(self, *args, **kwargs):
        conn = self.connect_db()
        c = conn.cursor()
        try:
            insert_tb_cmd = '''
                    CREATE TABLE IF NOT EXISTS INSTALLED
                    (NAME TEXT,
                    VERSION TEXT,
                    ARCH TEXT);
                    '''
            values = {'title': 'jack', 'type': None, 'genre': 'Action', 'onchapter': None, 'chapters': 6,
                      'status': 'Ongoing'}
            cur.execute(
                'INSERT INTO Media (id, title, type, onchapter, chapters, status) VALUES (:id, :title, :type, :onchapter, :chapters, :status);'), values)
            c.execute(insert_tb_cmd)
            conn.commit()
        except Exception as err:
            raise err('Installed table operation failed !')
        finally:
            c.close
            conn.close()






if __name__ == "__main__":
    DbOp().create_installed_table()
