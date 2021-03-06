from gym.daos import BaseDao


class DaoEmployee(BaseDao):
    def find_all(self):
         return super().find_all('employee')

    def find_employee(self,eid):
        sql= "select * from employee where eid=%d;" %eid
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        self.db.commit_close()
        return all_rows

    def find_intern(self):
        sql = 'select * from employee where is_internship=1;'
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        self.db.commit_close()
        return all_rows

    def find_non_intern(self):
        sql = 'select * from employee where is_internship=0;'
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        self.db.commit_close()
        return all_rows

    def find_manager(self,eid):
        sql = 'select e1.eid, e1.fname, e1.lname,e1.email,e1.salary,e1.mid from ' \
              'employee e1 inner  join employee e2 on e1.mid=e2.eid where e1.eid= %d' % eid
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        self.db.commit_close()
        return all_rows

    def sum_salary(self):
        sql="select count(salary) from employee"
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        self.db.commit_close()
        return all_rows

    def find_branch(self,eid):
        sql = 'select b.bid,b.bname,b.postcode,b.email from ' \
              'employee e inner join branch b on e.bid=b.bid where eid= %d' % eid
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        self.db.commit_close()
        return all_rows

    def find_facility(self,eid):
        sql= 'select f.fid, f.status_label from ' \
             'employee e inner join facility f on f.eid=e.eid where e.eid = %d' % eid
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        self.db.commit_close()
        return all_rows

    def insert(self, eid, fname, lname, email, phone, salary, gender, mid, bid, password, is_internship,username):

        sql = "insert into employee(eid, fname, lname, email, phone, salary, gender, mid, bid, password,is_internship,username)" \
              " values(%d,'%s','%s','%s','%s',%d,'%s',%d,%d,'%s',%d,'%s')"   \
              % (eid,fname, lname, email, phone, salary, gender, mid, bid, password, is_internship,username)
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()

    def delete(self,eid):
        sql='delete from employee where eid= %d' % eid
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()

    def update(self, email, phone, salary,password, is_internship,username,eid):
        sql = "update employee set  email='%s', phone='%s', salary=%d,password='%s', is_internship=%d ,username='%s' where eid= %d " \
              % (email, phone, salary,password, is_internship,username,eid)
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()


if __name__ == '__main__':
    dao = DaoEmployee()
    #print(dao.find_facility(2))
