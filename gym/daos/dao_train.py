from gym.daos import BaseDao


class DaoTrain(BaseDao):
    def find_all(self):
        return super().find_all('train')

    def find_one(self,rid, mid):
        sql="select * from train where rid=%d and mid=%d" % (rid, mid)
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        self.db.commit_close()
        return all_rows

    def insert(self,rid, mid,hour):
        sql = "insert into train values(%d,%d,%d)" % (rid, mid, hour)
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()

    def delete(self,rid, mid):
        sql="delete from train where rid=%d and mid=%d" % (rid, mid)
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()

    def update(self,rid, mid,hour,rid_condition,mid_condition):
        sql = "update train set rid=%d, mid=%d, hour=%d where rid=%d and mid=%d"\
              % (rid, mid,hour,rid_condition,mid_condition)
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()




