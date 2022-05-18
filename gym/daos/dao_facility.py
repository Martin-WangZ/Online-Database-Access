from gym.daos import BaseDao


class DaoFacility(BaseDao):
    def find_all(self):
        return super().find_all('facility')


    def find_outdoor(self):
        sql = 'select * from facility where is_outdoor=1;'
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        self.db.commit_close()
        return all_rows

    def find_indoor(self):
        sql = 'select * from facility where is_outdoor=0;'
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        self.db.commit_close()
        return all_rows

    def who_manage(self, fid):
        sql = 'select e.eid,e.fname, e.lname, e.phone from ' \
              'facility f inner join employee e on f.eid=e.eid where f.fid = %d' % fid
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        self.db.commit_close()
        return all_rows

    def insert(self,fid,status_label, manufactory, manufacture_date, eid, is_outdoor):
        sql="insert into facility(fid, status_label, manufactory, manufacture_date, eid, is_outdoor) " \
            "values('%d','%s','%s','%s','%d','%d')" \
            %(fid, status_label, manufactory, manufacture_date, eid, is_outdoor)
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()

    def delete(self,fid):
        sql = 'delete from facility where fid= %d' % fid
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()

    def update(self,fid, status_label, manufactory, manufacture_date, eid, is_outdoor,fid_condition):
        sql="update facility set fid=%d, status_label='%s',manufactory='%s'," \
            "manufacture_date='%s',eid=%d,is_outdoor=%d " \
            "where fid=%d" % (fid, status_label, manufactory, manufacture_date, eid, is_outdoor,fid_condition)
        cursor = self.db.get_cursor()
        cursor.execute(sql)
        self.db.commit_close()


if __name__ == '__main__':
    dao=DaoFacility()
    print(dao.delete(7))