class ModelHome:
    def __init__(self,id, title ,content, image ):
        self.__id=id
        self.__title=title
        self.__content=content
        self.__image=image

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,id):
        self.__id=id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):
        self.__content = content

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, image):
        self.__image = image