class DaoDependents:
    def __init__(self, mid, pname, age, cost):
        self.__mid = mid
        self.__pname = pname
        self.__age = age
        self.__cost = cost

    @property
    def mid(self):
        return self.__mid

    @mid.setter
    def mid(self, mid):
        self.__mid = mid

    @property
    def pname(self):
        return self.__pname

    @pname.setter
    def pname(self,pname):
        self.__pname=pname

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        self.__age=age

    @property
    def cost(self):
        return self.__cost
    @cost.setter
    def cost(self,cost):
        self.__cost=cost
