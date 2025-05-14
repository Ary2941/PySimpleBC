from abc import ABC, abstractmethod
import copy
import hashlib
import json

class Blockx(ABC):
    def __init__(self,**kwargs):
        for chave, valor in kwargs.items():
            setattr(self, chave, valor)

    def hash_block(self, ignore_keys=None):
        if ignore_keys is None:
            ignore_keys = []

        block_data = {k: v for k, v in self.__dict__.items() if k not in ignore_keys}

        block_str = json.dumps(block_data, sort_keys=True).encode()
        return hashlib.sha256(block_str).hexdigest()
    
    def isValid(block): # se não raise valueError
        copia = copy.deepcopy(block)
        if block.hash == copia.hash_block(["hash"]):
            return True
    
        raise ValueError("Block is invalid.")