from abc import ABC

class Terminalx(ABC):
    def __init__(self,port=5050, **kwargs):

        for chave, valor in kwargs.items():
            setattr(self, chave, valor)

    def add_transaction(self, tx_data):
        '''
        add transaction on chain (must be in a dict format)
        '''

        if self.blockchain:
            self.blockchain.add_transaction(tx_data)
            # se tamanho for x, criar bloco
        else:
            print("blockchain not set")
    
    def create_block(self):
        '''
        create block using transactions on pool
        '''
        if self.blockchain:
            block = self.blockchain.create_block()
        else:
            print("blockchain not set")

    def run(self):
        return True
    
    def get_chain(self):
        return self.blockchain.get_chain()
    
    def __str__(self):
        string = '-----BEGIN CHAIN-----\n'
        for item in self.blockchain.get_chain():
            string += str(item)+'\n'
        string += '-----END CHAIN-----'
        return string