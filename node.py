class Node:

    def __init__(self, blockchain):
        self.blockchain = []

    def get_transaction_value(self):
        """ Returns the input of the user (a new transaction amount) as a float """
        tx_recipient = input("Enter the recipient of the transaction: ")
        tx_amount = float(input("Your transaction amount please: "))
        return (tx_recipient, tx_amount)


    def get_user_choice(self):
        return input("Your choice:")


    def print_blockchainelements(self):
        #Output the blockchain list to the console
        for block in self.blockchain:
            print(block)


    def listen_for_input(self):
        waiting_for_input = True
        while waiting_for_input:
            print("Please choose:")
            print("1: Add a new transaction value")
            print("2: Min a new block")
            print("3: Output the blockchain blocks")
            print("5: Check transaction validity")
            print("h: Manipulate the chain")
            print("q: To quit")
            user_choice = self.get_user_choice()
            if(user_choice == "1"):
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data
                if add_transaction(recipient, amount=amount):
                    print("Added transaction!")
                else:
                    print("Transaction failed")
                print(open_transactions)
            elif(user_choice == "2"):
                if mine_block():
                    open_transactions = []
                    save_data()
            elif(user_choice == "3"):
                self.print_blockchainelements()
            elif(user_choice == "4"):
                verifier = Verification()
                if verifier.verify_transactions(open_transactions, get_balance):
                    print("All transactions are valid")
                else:
                    print("A transaction is invalid")
            elif(user_choice == "h"):
                if len(self.blockchain) > 0:
                    self.blockchain[0] = {
                        "previous_hash": "",
                        "index": 0,
                        "transactions": [{"sender": "Chris", "recipient": "Max", "amount": 100}]
                    }
            elif(user_choice == "q"):
                waiting_for_input = False
            else:
                print("Input was invalid, please pick a value from the list")
            verifier = Verification()
            if verifier.verify_chain(self.blockchain) == False:
                print("invalid blockchain")
                waiting_for_input = False
            print('Balance of {}: {:6.2f}'.format(owner, get_balance(owner)))
        else:
            print("User left!")

        print("Done")