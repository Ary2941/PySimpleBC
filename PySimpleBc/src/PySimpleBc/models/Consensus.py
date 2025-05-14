from abc import ABC

class Consensusx(ABC):
    def __init__(self):
        pass

    def invoke_consensus(self, *args,**kwargs): # tratamento da transação
        return True