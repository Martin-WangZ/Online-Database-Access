class ModelLocation:
    def __init__(self, postcode, address):
        self.__postcode = postcode
        self.__address = address

    @property
    def postcode(self):
        return self.__postcode

    @postcode.setter
    def postcode(self, postcode):
        return self.__postcode

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address
