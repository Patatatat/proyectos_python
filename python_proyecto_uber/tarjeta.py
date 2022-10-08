from re import S
from tarjeta import payment
from datetime import date
class tarjeta(payment):
    franquicia = str
    fechaDeVencimiento = date
    CVV = str

    def __init__(self, id, franquicia, fechaDeVencimiento, CVV):
        super.__init__(id)
        self.franquicia = franquicia
        self.fechaDeVencimiento = fechaDeVencimiento
        self.CVV = CVV