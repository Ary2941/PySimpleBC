

from .models.Block import Blockx
from .models.Terminal import Terminalx
from .models.Transaction import Transactionx
from .models.SmartContract import SmartContractx
from .models.Wallet import Walletx
from .models.Consensus import Consensusx
from .models.Blockchain import Blockchainx


def Blockchain( 
    transaction_model = Transactionx,
    smart_contract_model = SmartContractx,
    wallet_model = Walletx,
    block_model = Blockx,
    consensus_model = Consensusx,
    terminal_model = Terminalx,
    port = 5050,
    ):
    '''
    creates a terminal with a blockchain
    terminal are used to connect ledges from the chain
    '''

    terminal_model = terminal_model(port)
    terminal_model.blockchain = Blockchainx(
        transaction_model=transaction_model,
        smart_contract_model=smart_contract_model,
        wallet_model=wallet_model,
        block_model=block_model,
        consensus_model=consensus_model,
    )
    terminal_model.run()

    return terminal_model