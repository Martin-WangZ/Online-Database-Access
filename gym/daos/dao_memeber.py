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

    def find_insurance(self,mid):
        sql="select d.mid,d.pname,d.age,d.cost from " \
            "member m inner join dependents d on m.mid=d.mid where m.mid=%d" %mid
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        self.db.commit_close()
        return all_rows

    def find_priviliege(self,mid):
        sql = "select  m.mid,m.fname, m.lname,ms.priviliege_description from " \
              "member m inner join membership ms on m.mtype=ms.mtype where m.mid=%d" % mid
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


    def insert(self,mid,fname,lname,phone,address,email,gender,bid,mtype,password):
        sql="insert into member(mid,fname,lname,phone,address,email,gender,bid,mtype,password) " \
            "values(%d, '%s', '%s', '%s', '%s', '%s', '%s', '%s',%d, '%s', '%s')" \
            % (mid,fname,lname,phone,address,email,gender,bid,mtype,password)
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()

    def delete(self,mid):
        sql="delete from member where mid=%d" % mid
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()

    def update(self,mid,fname,lname,phone,address,email,gender,bid,mtype,password,mid_condition):
        sql="update member set mid=%d,fname='%s',lname='%s',phone='%s',address='%s', " \
            "email='%s', gender='%s', bid=%d, mtype='%s',password='%s' where mid=%d"\
            % (mid,fname,lname,phone,address,email,gender,bid,mtype,password,mid_condition)
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()

