from gym.daos import BaseDao


class DaoMember(BaseDao):
    def find_all(self):
        return super().find_all('member')

    def find_one(self,mid):
        sql="select * from member where mid=%d" % mid
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        self.db.commit_close()
        return all_rows

    def find_specific_insurance(self,mid):
        sql="select m.fname,m.lname,m.bid,d.age,d.cost from " \
            "member m inner join dependents d on m.mid=d.mid where m.mid=%d" %mid
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        self.db.commit_close()
        return all_rows


    def find_insurance(self):
        sql="select m.fname,m.lname,m.bid,d.age,d.cost from " \
            "member m inner join dependents d on m.mid=d.mid"
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        self.db.commit_close()
        return all_rows


    def find_priviliege(self):
        sql = "select  m.username,m.phone,m.email,ms.priviliege_description from " \
              "member m inner join membership ms on m.mtype=ms.mtype"
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        self.db.commit_close()
        return all_rows

    def find_coach(self,mid):
        sql="select p.rid, p.fname,p.lname from " \
            "private_coach p where p.rid in (select distinct t.rid from train t where t.mid=%d)" % mid
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        self.db.commit_close()
        return all_rows


    def insert(self,mid,phone,bid,mtype,password,username):
        sql="insert into member(mid,phone,bid,mtype,password,username) " \
            "values(%d, '%s', '%s', '%s', '%s', '%s', '%s', '%s',%d, '%s', '%s','%s')" \
            % (mid,phone,bid,mtype,password,username)
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()

    def delete(self,mid):
        sql="delete from member where mid=%d" % mid
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()

    def update(self,mid,phone,bid,mtype,password,username):
        sql="update member set phone='%s',bid=%d,mtype='%s',password='%s',username='%s' " \
            "where mid=%d" %(phone,bid,mtype,password,username,mid)
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()

