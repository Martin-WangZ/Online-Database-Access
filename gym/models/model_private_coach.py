class ModelPrivateCoach:
    def __init__(self, rid, fname, lname, teaching_age, gender, email, phone, age, price_for_training, password):
        self.__rid = rid
        self.__fname = fname
        self.__lname = lname
        self.__teaching_age = teaching_age
        self.__gender = gender
        self.__email = email
        self.__phone = phone
        self.__age = age
        self.__price_for_training = price_for_training
        self.__password = password

    @property
    def rid(self):
        return self.__rid

    @rid.setter
    def rid(self, rid):
        self.__rid = rid

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
    def teaching_age(self):
        return self.__teaching_age

    @teaching_age.setter
    def teaching_age(self, teaching_age):
        self.__teaching_age = teaching_age

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.__gender = gender

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
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def price_for_training(self):
        return self.__price_for_training

    @price_for_training.setter
    def price_for_training(self, price_for_training):
        self.__price_for_training = price_for_training

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password
