class ModelMember:
    def __init__(self,mid,fname,lname,phone,address,email,gender,bid,mtype,password,username):
        self.__email=email
        self.__gender=gender
        self.__bid=bid
        self.__mtype=mtype
        self.__password=password
        self.__mid=mid
        self.__fname=fname
        self.__lname=lname
        self.__phone=phone
        self.__address=address
        self.__username=username

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username



    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def mtype(self):
        return self.__mtype

    @mtype.setter
    def mtype(self, mtype):
        self.__mtype = mtype

    @property
    def bid(self):
        return self.__bid

    @bid.setter
    def bid(self, bid):
        self.__bid = bid

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.__gender = gender


    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self,address):
        self.__address=address


    @property
    def mid(self):
        return  self.__mid
    @mid.setter
    def mid(self,mid):
        self.__mid=mid

    @property
    def fname(self):
        return self.__fname

    @fname.setter
    def fname(self, fname):
        self.__fname = fname

    @property
    def lname(self):
        return self.__lname

    @lname.setter
    def lname(self, lname):
        self.__lname = lname

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
