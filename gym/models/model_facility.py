

class ModelFacility:
    def __init__(self, fid, status_label, manufactory, manufacture_date, eid, is_outdoor):
        self.__fid=fid
        self.__status_label=status_label
        self.__manufactory=manufactory
        self.__manufacture_date= manufacture_date
        self.__eid=eid
        self.__is_outdoor=is_outdoor

    @property
    def fid(self):
        return self.__fid

    @fid.setter
    def fid(self,fid):
        self.__fid= fid

    @property
    def status_label(self):
        return self.__status_label

    @status_label.setter
    def status_label(self,status_label):
        self.__status_label=status_label

    @property
    def manufactory(self):
        return self.__manufactory

    @manufactory.setter
    def manufactory(self,manufactory):
        self.__manufactory=manufactory

    @property
    def manufacture_date(self):
        return self.__manufacture_date

    @manufacture_date.setter
    def manufacture_date(self,manufacture_date):
        self.__manufacture_date=manufacture_date

    @property
    def eid(self):
        return self.__eid

    @eid.setter
    def eid(self,eid):
        self.__eid=eid

    @property
    def is_outdoor(self):
        return self.__is_outdoor

    @is_outdoor.setter
    def is_outdoor(self, is_outdoor):
        self.__is_outdoor = is_outdoor

