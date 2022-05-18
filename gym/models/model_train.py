class ModelTrain:
    def __init__(self, rid, mid, hour):
        self.__rid = rid
        self.__mid = mid
        self.__hour = hour

    @property
    def rid(self):
        return self.__rid

    @rid.setter
    def rid(self, rid):
        self.__rid = rid

    @property
    def mid(self):
        return self.__mid

    @mid.setter
    def mid(self, mid):
        self.__mid = mid

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour):
        self.__hour = hour
