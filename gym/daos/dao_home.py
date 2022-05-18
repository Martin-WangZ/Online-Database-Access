from gym.daos import BaseDao


class DaoHome(BaseDao):
    def find_all(self):
        return super().find_all('home')