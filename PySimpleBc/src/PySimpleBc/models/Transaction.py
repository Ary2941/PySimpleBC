from abc import ABC
import copy

class Transactionx(ABC):
    def __init__(self,**kwargs):
        for chave, valor in kwargs.items():
            setattr(self, chave, valor)

    def to_dict(self):
        dict_respresentation = copy.deepcopy(self.__dict__)
        return dict_respresentation