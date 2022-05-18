from gym.daos import BaseDao


class DaoBranch(BaseDao):
    def find_all(self):
        return super().find_all('branch')


    def find_specific_branch(self,bid):
        sql='select * from branch where bid= %d' % bid
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        self.db.commit_close()
        return all_rows

    def find_how_many_employee(self, bid):
        sql="select count(distinct e.eid) from employee e inner join branch b on b.bid=e.bid where bid = %d" % bid
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        self.db.commit_close()
        return all_rows

    def find_section(self,bid):
        sql="select s.sid, s.sname, s.duty from branch b inner join section s on s.bid=b.bid where b.bid= %d" %bid
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        self.db.commit_close()
        return all_rows

    def find_address(self,bid):
        sql="select l.address from branch b inner join location l on b.postcode=l.postcode where bid=%d" %bid
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        self.db.commit_close()
        return all_rows

    def insert(self,bid, bname,email,phone,postcode):
        sql="insert into branch(bid, bname,email,phone,postcode) values(%d,'%s','%s','%s','%s') "\
            %(bid, bname,email,phone,postcode)
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()

    def delete(self, bid):
        sql = 'delete from branch where bid= %d' % bid
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()

    def update(self,bname,email,phone,postcode,bid):
        sql="update branch set bname='%s' , email= '%s', phone='%s', postcode='%s' where bid= %d " % \
            (bname,email,phone,postcode,bid)
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()



