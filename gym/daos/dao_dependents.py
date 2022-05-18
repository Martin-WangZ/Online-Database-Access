from gym.daos import BaseDao


class DaoDependents(BaseDao):
    def find_all(self):
        return super().find_all('dependents')

    def insert(self,mid,pname,age,cost):
        sql="insert into dependents(mid,pname,age,cost) values(%d,'%s',%d,%d)" % (mid,pname,age,cost)
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()

    def delete(self, mid,pname):
        sql = "delete from branch where mid= %d and pname='%s'" % (mid,pname)
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()

    def update(self,age,cost,mid,pname):
        sql="update dependents set age=%d, cost=%d where mid= %d and pname='%s'" % (age,cost,mid,pname)
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()


