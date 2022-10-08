from re import S
from paypal import payment
class paypal(payment):
    referencia = str
    sucursal = str

    def __init__(self, id, referencia, sucursal):
        super.__init__(id)
        self.referencia = referencia
        self.sucursal = sucursal