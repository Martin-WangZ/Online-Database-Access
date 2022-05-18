

class ModelEmployee:
    def __init__(self, eid, fname, lname, email, phone, salary, gender,mid,bid,password, is_internship, username):
        self.__eid = eid
        self.__fname = fname
        self.__lname = lname
        self.__email = email
        self.__phone = phone
        self.__salary = salary
        self.__gender = gender
        self.__mid = mid
        self.__bid = bid
        self.__password = password
        self.__is_internship = is_internship
        self.__username=username

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self,username):
        self.__username=username

    @property
    def eid(self):
        return self.__eid

    @eid.setter
    def eid(self,eid):
        self.__eid=eid

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
    def lname(self,lname):
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

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,salary):
        self.__salary = salary

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.__gender = gender

    @property
    def mid(self):
        return self.__mid

    @mid.setter
    def mid(self, mid):
        self.__mid = mid

    @property
    def bid(self):
        return self.__bid

    @bid.setter
    def bid(self, bid):
        self.__bid = bid

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def is_internship(self):
        return self.__is_internship

    @is_internship.setter
    def is_internship(self, is_internship):
        self.__is_internship = is_internship


