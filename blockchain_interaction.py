from web3 import Web3

class BlockchainInteraction:
    def __init__(self):
        # Connect to the blockchain
        self.w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/your-infura-project-id'))

    def get_account_balance(self, address):
        # Get the balance of a given blockchain account
        balance = self.w3.eth.get_balance(address)
        return self.w3.fromWei(balance, 'ether')

    def send_transaction(self, sender, recipient, amount):
        # Send a transaction from one account to another
        transaction = {
            'from': sender,
            'to': recipient,
            'value': self.w3.toWei(amount, 'ether'),
            'gas': 21000,
            'gasPrice': self.w3.toWei('50', 'gwei')
        }
        signed_transaction = self.w3.eth.account.sign_transaction(transaction, private_key)
        transaction_hash = self.w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
        return transaction_hash

    def load_contract(self, contract_address):
        # Load a smart contract at a given address
        contract = self.w3.eth.contract(address=contract_address, abi=contract_abi)
        return contract
