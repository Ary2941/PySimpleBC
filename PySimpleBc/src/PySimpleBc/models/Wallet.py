from abc import ABC

class Walletx(ABC):
    def __init__(self):
        pass
    def sign(self, *args,**kwargs): #usado para assinar a transação
        return ""
    def hash(self,*args,**kwargs): #usado para gerar o hash da transação
        return ""
    def signature_valid(self,*args,**kwargs): #usado para validar o hash da transação
        return True