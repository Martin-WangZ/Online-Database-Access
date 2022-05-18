from gym.daos import BaseDao


class DaoPrivateCoach(BaseDao):
    def find_all(self):
        return super().find_all('private_coach')

    def find_one(self,rid):
        sql="select * from private_coach where rid=%d" % rid
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        self.db.commit_close()
        return all_rows

    def find_members(self,rid):
        sql = "select mid,fname,lname,email,phone,mtype from member where mid in (select mid from train where rid = %d)" % rid
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        self.db.commit_close()
        return all_rows

    def delete(self,rid):
        sql = "delete from private_coach where rid=%d" % rid
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()

    def insert(self,rid, fname, lname, teaching_age, gender, email, phone, age, price_for_training, password):
        sql="insert into private_coach(rid, fname, lname, teaching_age, gender, email, phone, age, price_for_training, password) values(%d,'%s','%s',%d,'%s','%s','%s',%d,%d,,'%s')" \
            % (rid, fname, lname, teaching_age, gender, email, phone, age, price_for_training, password)
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()

    def update(self,rid, fname, lname, teaching_age, gender, email, phone, age, price_for_training, password, rid_condition):
        sql="update private_coach set rid=%d, fname='%s',lname='%s',teaching_age=%d, " \
            "gender='%s',email='%s', phone='%s',age=%d,price_for_training=%d,password='%s' " \
            "where rid=%d" % (rid, fname, lname, teaching_age, gender, email, phone, age, price_for_training, password, rid_condition)
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()
