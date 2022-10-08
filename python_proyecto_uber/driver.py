from account import Account

class Driver (Account):
    def __init__ (self, id, name, document, email, password) -> None:
        super().__init__(id, name, document, email, password)