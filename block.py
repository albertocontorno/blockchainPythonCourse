from time import time
from utility.printable import Printable

class Block(Printable):

    def __init__(self, previous_hash, index, transactions, proof, timestrap = time()):
        self.previous_hash = previous_hash
        self.index = index
        self.transactions = transactions
        self.proof = proof
        self.timestrap = timestrap
