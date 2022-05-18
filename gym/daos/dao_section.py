from gym.daos import BaseDao


class DaoSection(BaseDao):
    def find_all(self):
        return super().find_all('section')

    def belong_branch(self, sid):
        sql = "select b.bid, b.bname, b.email, b.phone, b. from " \
              "branch b inner join section s on s.bid=b.bid where sid= %d" % sid
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        self.db.commit_close()
        return all_rows

    def insert(self,sid,sname,duty,bid):
        sql="insert into section(sid,sname,duty,bid) values(%d,'%s','%s',%d)" % (sid,sname,duty,bid)
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()

    def delete(self,sid):
        sql = "delete from section where sid=%d" %sid
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()

    def update(self,sid,sname,duty,bid, sid_condition):
        sql="update section set sid=%d, sname='%s',duty='%s',bid=%d,sid=%d where sid=%d" \
            % (sid,sname,duty,bid, sid_condition)
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()




if __name__ == '__main__':
    dao = DaoSection()
    print(dao.find_all())
