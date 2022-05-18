import pymysql
from pymysql.cursors import DictCursor

CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'db_project',
    'cursorclass': DictCursor  # [{},{}]
}


class Db:
    def __init__(self):
        self.connect = pymysql.Connect(**CONFIG)  # connect db

    def get_cursor(self):

        return self.connect.cursor()

    def commit_close(self, exe_error=None):
        try:
            if exe_error:
                self.connect.rollback()

            else:
                self.connect.commit()

        except Exception as e:
            print(e)

        finally:
            if self.connect:
                self.connect.close()
                self.connect = None


class BaseDao:
    def __init__(self):
        self.db = Db()

    def find_all(self, table):
        sql = 'select * from %s;' % table
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        self.db.commit_close()
        return all_rows








