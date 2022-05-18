from gym.daos import BaseDao


class DaoMemebership(BaseDao):

    def find_all(self):
        return super().find_all('membership')

    def find_priviliege(self,mtype):
        sql="select priviliege_description from membership where mtype='%s'" % mtype
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        self.db.commit_close()
        return all_rows

    def delete(self,mtype):
        sql="delete from membership where mtype='%s'" % mtype
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()

    def insert(self,mtype,priviliege_description):
        sql="insert into membership(mtype,priviliege_description) values('%s','%s')" \
            % (mtype,priviliege_description)
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()

    def update(self,mtype,priviliege_description,mtype_condition):
        sql="update membership set mtype='%s',priviliege_description='%s' where mtype='%s'" \
            % (mtype,priviliege_description,mtype_condition)
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()

