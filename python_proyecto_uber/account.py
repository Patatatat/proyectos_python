class Account:
    __id = int
    __name = str
    __document = str
    __email = str
    __password = str

    def __init__ (self, id, name, document, email, password) -> None:
        self.__id = id
        self.__name = name
        self.__document = document
        self.__email = email
        self.__password = password

    def getId (self):
        return self.__id

    def setId (self, id):
        self.__id = id

    def getName (self):
        return self.__name

    def setName (self, name):
        self.__name = name

    def getDocument (self):
        return self.__document

    def setDocument (self, document):
        self.__document = document

    def getEmail (self):
        return self.__email

    def setEmail (self, email):
        self.__email = email

    def getPassword (self):
        return self.__password

    def setPassword (self, password):
        self.__password = password