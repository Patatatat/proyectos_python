from car import Car

class UberAdvanced (Car):
    __typeCarAccepted = []
    __seatsMaterial = []

    def __init__ (self, id, license, driver, passengers, typeCarAccepted, seatsMaterial) -> None:
        super().__init__(id, license, driver, passengers)

        self.__typeCarAccepted = typeCarAccepted
        self.__seatsMaterial = seatsMaterial

    def getTypeCarAccepted (self):
        return self.__typeCarAccepted

    def setTypeCarAccepted (self, typeCarAccepted):
        self.__typeCarAccepted = typeCarAccepted
    
    def getSeatsMaterial (self):
        return self.__seatsMaterial
    
    def setSeatsMaterial (self, __seatsMaterial):
        self.__seatsMaterial = __seatsMaterial