from abc import ABC

class Message(ABC):
    def __init__(self, **kwargs):
        for chave, valor in kwargs.items():
            setattr(self, chave, valor)

    def shareblock(self): #precisa de formato dict para entrar no bloco
        return self.__dict__

class SmartContractx(ABC):
    def handle_transaction(self, *args,**kwargs): # tratamento da transação
        return True
    

    def handle_block(self, block): # tratamento do bloco
        return block