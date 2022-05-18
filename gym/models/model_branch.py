class ModelBranch:
    def __init__(self,bid, bname,email,phone,postcode):
        self.__bid=bid
        self.__bname=bname
        self.__email=email
        self.__phone=phone
        self.__postcode=postcode

    @property
    def bid(self):
        return self.__bid

    @bid.setter
    def bid(self,bid):
        self.__bid=bid

    @property
    def bname(self):
        return self.__bname

    @bname.setter
    def bname(self, bname):
        self.__bname = bname

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @property
    def postcode(self):
        return self.__postcode

    @postcode.setter
    def postcode(self, postcode):
        self.__postcode = postcode

