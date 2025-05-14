class Blockchainx:
    def __init__(self, 
            transaction_model = None,
            smart_contract_model = None,
            wallet_model = None,
            block_model = None,
            consensus_model = None,
            ):
        
        self.transaction_model = transaction_model
        self.smart_contract_model = smart_contract_model()
        self.wallet_model = wallet_model()
        self.block_model = block_model
        self.chain = []
        self.current_transactions = []

    def add_transaction(self, tx_data):
        tx = self.transaction_model(**tx_data)
        if not self.wallet_model.signature_valid(tx):
            raise ValueError("invalid signature")
        self.smart_contract_model.handle_transaction(tx)
        self.current_transactions.append(tx)
        
    def create_block(self,block = None,previous_hash="GENESIS"):
        isFromPool = False
        if block is None:
            isFromPool = True
            if not self.chain == []:
                previous_hash = self.chain[-1].hash

            block = self.block_model(
                prev = previous_hash,
                index =  len(self.chain) + 1,
                transactions = [tx.to_dict() for tx in self.current_transactions],
            )

            block.hash = block.hash_block()

        if block.hash == previous_hash:
            raise ValueError("Block hash is equal to previous hash.")

        #print(block.index, len(self.chain) + 1)
        if block.index != (len(self.chain)+1):
            raise ValueError("Block index is not correct.")

        self.block_model.isValid(block)
        
        block = self.smart_contract_model.handle_block(block)
        #print (f"block {block} created")
        self.chain.append(block)
        if isFromPool:
            self.current_transactions = []
        return block
    
    def get_chain(self):
        blockdict = []
        for block in self.chain:
            blockdict.append(block.__dict__)
        return blockdict
