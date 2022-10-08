class Car:
    __id = int
    __license = str
    __driver = str
    _passengers = int

    def __init__ (self, id, license, driver, passengers) -> None:
        self.__id = id
        self.__license = license
        self.__driver = driver
        self.setPassengers(passengers)

    def getId (self):
        return self.__id

    def setId (self, id):
        self.__id = id

    def getLicense (self):
        return self.__license

    def setLicense (self, license):
        self.__license = license

    def getDriver (self):
        return self.__driver

    def setDriver (self, driver):
        self.__driver = driver

    def getPassengers (self):
        return self._passengers

    def setPassengers (self, passengers):
        if passengers >= 4:
            self._passengers = passengers
        else:
            print("Car Passengers Must be 4 or more")