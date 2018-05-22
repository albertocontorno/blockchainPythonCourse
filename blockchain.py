from functools import reduce
import hashlib as hash
import json
import pickle
from hash_util import hash_block
from collections import OrderedDict
from block import Block
from transaction import Transaction
from verification import Verification

MINING_REWARD = 10
class Blockchain:
    def __init__(self, hosting_node):
        # Initializing our blockchain list
        genesis_block = Block("", 0, [], 100, 0)
        # Initializing our blockchain list
        self.chain = [genesis_block]
        self.open_transactions = []
        self.load_data()
        self.hosting_node = hosting_node_id

#partecipants = set([owner])


    def load_data(self):
        try:
            with open("blockchain.json", mode="r") as f:
                # file_content = pickle.loads(f.read())
                file_content = f.readlines()
                print(file_content)
                # blockchain = file_content["chain"]
                # open_transactions = file_content["ot"]
                blockchain = json.loads(file_content[0][:-1])
                updated_blockchain = []
                for block in blockchain:
                    converted_tx = [Transaction(tx["sender"], tx["recipient"], tx["amount"]) for tx in block["transactions"]]
                    #converted_tx = [OrderedDict([("sender", tx["sender"]), ("recipient", tx["recipient"]), ("amount", tx["amount"])]) for tx in block["transactions"]]

                    updated_block = Block(block["previous_hash"], block["index"], converted_tx, block["proof"], block["timestrap"])

                    updated_blockchain.append(updated_block)

                self.chain = updated_blockchain
                open_transactions = json.loads(file_content[1])
                updated_transactions = []
                for tx in open_transactions:
                    updated_transaction = Transaction(tx["sender"], tx["recipient"], tx["amount"])
                    #updated_transaction = OrderedDict([("sender", tx["sender"]), ("recipient", tx["recipient"]), ("amount", tx["amount"])])
                    updated_transactions.append(updated_transaction)
                self.open_transactions = updated_transactions
        except (IOError, IndexError):
            print("Handled exception")
        finally:
            print("CleanUP")

    def save_data(self):
        try:
            with open("blockchain.json", mode="w") as f:
                saveable_chain = [block.__dict__ for block in [Block(block_el.previous_hash, block_el.index, [tx.__dict__ for tx in block_el.transactions] , block_el.proof, block_el.timestrap) for block_el in self.chain]]
                f.write(json.dumps(saveable_chain))
                f.write("\n")
                saveable_tx = [tx.__dict__.copy() for tx in self.open_transactions]
                f.write(json.dumps(saveable_tx))
                # save_data = {
                #     "chain": blockchain,
                #     "ot": open_transactions
                # }
                # f.write(pickle.dumps(save_data))
        except IOError:
            print("Saving Failed")


    def proof_of_work(self):
        last_block = self.chain[-1]
        last_hash = hash_block(last_block)
        proof = 0
        verifier = Verification()
        while(not verifier.valid_proof(self.open_transactions, last_hash, proof)):
            proof += 1
        return proof


    def get_balance(self, partecipant):
        partecipant = self.hosting_node

        tx_sender = [[tx.amount for tx in block.transactions
                    if tx.sender == partecipant] for block in self.chain]
        open_tx_sender = [tx.amount for tx in self.open_transactions if tx["sender"] == partecipant]
        tx_sender.append(open_tx_sender)
        amount_sent = 0
        amount_sent = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt)
                            if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)

        tx_recipient = [[tx.amount for tx in block.transactions
                        if tx.recipient == partecipant] for block in self.chain]
        amount_recieve = 0
        amount_recieve = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt)
                                if len(tx_amt) > 0 else tx_sum + 0, tx_recipient, 0)

        return amount_recieve - amount_sent


    def get_last_blockchain_value(self):
        """ Return the last value of the current blockchain. """
        if(len(self.chain) < 1):
            return None
        return self.chain[-1]





    def add_transaction(self, recipient, sender, amount=1.0):
        """ Append a new value as well as the last blockchain value to the blockchain.
        Arguments:
            :sender: The sender of the coins that should be addeed.
            :recipient: The recipient of the coins 
            :param: amount: The amount of coins sent with the transaction (default = 1.0)
        """
        # transaction = {"sender": sender, "recipient": recipient, "amount": amount}
        transaction = Transaction(recipient, sender, amount)
        #transaction = OrderedDict([("sender", sender), ("recipient", recipient), ("amount", amount)])
        verifier = Verification()
        if(verifier.verify_transaction(transaction, self.get_balance)):
            self.open_transactions.append(transaction)
            #partecipants.add(sender)
            #partecipants.add(recipient)
            self.save_data()
            return True
        return False


    def mine_block(self):
        print("BLOCKCHAIN ", self.chain)
        last_block = self.chain[-1]
        # for key in last_block:
        #     value = last_block[key]
        #     hashed_block += str(value)
        hashed_block = hash_block(last_block)
        proof = self.proof_of_work()
        # reward_transaction = {
        #     "sender": "MINING",
        #     "recipient": owner,
        #     "amount": MINING_REWARD
        # }
        reward_transaction = Transaction("MINING", self.hosting_node, MINING_REWARD)
        #reward_transaction = OrderedDict([("sender", "MINING"), ("recipient", owner), ("amount", MINING_REWARD)])

        copied_transactions = self.open_transactions[:]
        copied_transactions.append(reward_transaction)
        block = Block(hashed_block, len(self.chain),  copied_transactions, proof)
        self.chain.append(block)
        self.open_transactions = []
        self.save_data()
        return True


