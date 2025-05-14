from datetime import datetime

from PySimpleBc import Blockchain

blockchain = Blockchain()

blockchain.add_transaction({
    "user": "Alice",
    "registry": 1,
    "key": "a1",
    "timestamp": datetime.now().isoformat()
})

blockchain.add_transaction({
    "user": "Bruno",
    "registry": 0,
})

blockchain.create_block()

blockchain.add_transaction({
    "Rocambole": True,
})

blockchain.create_block()
blockchain.create_block()

print(blockchain.get_chain())
