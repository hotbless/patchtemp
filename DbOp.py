import sqlite3
from GetConfig import GetConfig


class DbOp:
    def __init__(self):
        self.conf = GetConfig().get_config()
        self.db = self.conf.get('db')
        print(self.db)
        self.db_name = self.db.get('name')

    def connect_db(self):
        conn = sqlite3.connect(self.db_name)


if __name__ == "__main__":
    DbOp().connect_db()
