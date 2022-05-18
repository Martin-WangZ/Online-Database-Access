class ModelMembership:
    def __init__(self,mtype,priviliege_description):
        self.__mtype=mtype
        self.__priviliege_description=priviliege_description

    @property
    def mtype(self):
        return self.__mtype
    @mtype.setter
    def mtype(self,mtype):
        self.__mtype=mtype

    @property
    def priviliege_description(self):
        return  self.__priviliege_description
    @priviliege_description.setter
    def priviliege_description(self,priviliege_description):
        self.__priviliege_description=priviliege_description