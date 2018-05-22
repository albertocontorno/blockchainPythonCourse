
from blockchain import Blockchain

from uuid import uuid4
from verification import Verification
class Node:

    def __init__(self):
        #self.id = str(uuid4())
        self.id= 'MySelf'
        self.blockchain = Blockchain(self.id)

    def get_transaction_value(self):
        """ Returns the input of the user (a new transaction amount) as a float """
        tx_recipient = input("Enter the recipient of the transaction: ")
        tx_amount = float(input("Your transaction amount please: "))
        return (tx_recipient, tx_amount)


    def get_user_choice(self):
        return input("Your choice:")


    def print_blockchainelements(self):
        #Output the blockchain list to the console
        for block in self.blockchain.chain:
            print(block)
        else:
            print('-'*20)


    def listen_for_input(self):
        waiting_for_input = True
        while waiting_for_input:
            print("Please choose:")
            print("1: Add a new transaction value")
            print("2: Min a new block")
            print("3: Output the blockchain blocks")
            print("5: Check transaction validity")
            print("q: To quit")
            user_choice = self.get_user_choice()
            if(user_choice == "1"):
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data
                if self.blockchain.add_transaction(recipient, self.id, amount=amount):
                    print("Added transaction!")
                else:
                    print("Transaction failed")
                print(self.blockchain.get_open_transactions())
            elif(user_choice == "2"):
                self.blockchain.mine_block()
            elif(user_choice == "3"):
                self.print_blockchainelements()
            elif(user_choice == "4"): 
                if Verification.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance):
                    print("All transactions are valid")
                else:
                    print("A transaction is invalid")
            elif(user_choice == "q"):
                waiting_for_input = False
            else:
                print("Input was invalid, please pick a value from the list")
            if Verification.verify_chain(self.blockchain.chain) == False:
                print("invalid blockchain")
                waiting_for_input = False
            print('Balance of {}: {:6.2f}'.format(self.id, self.blockchain.get_balance()))
        else:
            print("User left!")

        print("Done")


node = Node()
node.listen_for_input()