class ModelSection:
    def __init__(self,sid,sname,duty,bid):
        self.__sid= sid
        self.__sname = sname
        self.__duty= duty
        self.__bid=bid

    @property
    def sid(self):
        return self.__sid

    @sid.setter
    def sid(self,sid):
        self.__sid=sid

    @property
    def sname(self):
        return self.__sname

    @sname.setter
    def sname(self,sname):
        self.__sname=sname

    @property
    def duty(self):
        return self.__duty

    @duty.setter
    def duty(self,duty):
        self.__duty=duty

    @property
    def bid(self):
        return self.__bid

    @bid.setter
    def bid(self,bid):
        self.__bid=bid
