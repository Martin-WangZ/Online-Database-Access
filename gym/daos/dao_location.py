from gym.daos import BaseDao


class DaoLocation(BaseDao):

    def find_all(self):
        return super().find_all('location')


    def insert(self, postcode, address):

        sql = "insert into location(postcode, address) values('%s','%s')" %(postcode, address)
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()

    def delete(self, postcode):
        sql = "delete from location where postcode='%s'" % postcode
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()

    def update(self,postcode,address,postcode_condition):
        sql="update location set postcode='%s',address='%s' where postcode='%s'" \
            % (postcode,address,postcode_condition)
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()
