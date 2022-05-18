from gym.daos import BaseDao


class DaoHome(BaseDao):
    def find_all(self):
        return super().find_all('home')

    def delete_all(self,id):
        sql = "delete from home where id=%d " %id
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()
        