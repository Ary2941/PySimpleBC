# PySimpleBc

**PySimpleBc** é uma biblioteca Python minimalista e extensível para criação de blockchains customizados. Ideal para estudos, prototipagem rápida e simulações de sistemas distribuídos. Você define os modelos — a biblioteca cuida da infraestrutura.

> 🔐 **Requisito**: [cryptography](https://pypi.org/project/cryptography/) é a única dependência obrigatória.

---

## ✨ Recursos

- Criação de blockchains totalmente customizáveis
- Suporte a múltiplos nós (terminais)
- Verificação de assinaturas com carteiras digitais
- Contratos inteligentes plugáveis
- Estrutura modular para consenso, blocos e transações
- Leve, simples e fácil de entender

---

## 📦 Instalação

```bash
pip install -e PySimpleBc
# Clone ou integre o PySimpleBc ao seu projeto
```

---

## 🚀 Exemplo de Uso

```python
from PySimpleBc import Blockchain

# Inicia um terminal executando uma blockchain
terminal = Blockchain(port=5050)
```

### Substituindo os modelos padrão:

```python
from custom_models import (
    MyTransaction,
    MyWallet,
    MyBlock,
    MySmartContract,
    MyConsensus,
    MyTerminal
)

terminal = Blockchain(
    transaction_model=MyTransaction,
    wallet_model=MyWallet,
    block_model=MyBlock,
    smart_contract_model=MySmartContract,
    consensus_model=MyConsensus,
    terminal_model=MyTerminal,
    port=5051
)
```

---

## 🧱 Componentes

### `Blockchainx`

Classe principal da blockchain, com suporte a:

- Adição e validação de transações (`add_transaction`)
- Criação e validação de blocos (`create_block`)
- Retorno da cadeia atual (`get_chain`)

### `Terminalx`

Simula um terminal/nó da rede blockchain. Usa a classe `Blockchainx` internamente e pode ser estendido para conexões em rede, persistência ou APIs.

---

## 📂 Estrutura Modular

Você pode substituir os seguintes componentes:

| Componente         | Descrição                                 |
|--------------------|--------------------------------------------|
| `Transactionx`     | Modelo de transação                       |
| `Walletx`          | Carteira e verificação de assinatura      |
| `Blockx`           | Lógica do bloco, hash, e validação        |
| `SmartContractx`   | Lógica de contratos inteligentes          |
| `Consensusx`       | Implementação do protocolo de consenso    |
| `Terminalx`        | Comportamento do nó na rede               |

---

## ✅ Requisitos

- Python 3.8 ou superior

---

## 📄 Licença

MIT © [Amaury Luiz Chaves Junior]