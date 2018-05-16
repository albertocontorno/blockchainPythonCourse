# Initializing our blockchain list
genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transaction': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Myself'
partecipants = set([owner])

def hash_block(block):
    return '-'.join( [ str(block[key]) for key in block] )

def get_last_blockchain_value():
    """ Return the last value of the current blockchain. """
    if(len(blockchain) < 1):
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new value as well as the last blockchain value to the blockchain.
    Arguments:
        :sender: The sender of the coins that should be addeed.
        :recipient: The recipient of the coins 
        :param: amount: The amount of coins sent with the transaction (default = 1.0)
    """
    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
    open_transactions.append(transaction)
    partecipants.add(sender)
    partecipants.add(recipient)


def mine_block():
    last_block = blockchain[-1]
    # for key in last_block:
    #     value = last_block[key]
    #     hashed_block += str(value)
    hashed_block  = hash_block(last_block)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transaction': open_transactions
    }
    blockchain.append(block)
    return True


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float """
    tx_recipient = input("Enter the recipient of the transaction: ")
    tx_amount = float(input("Your transaction amount please: "))
    return (tx_recipient, tx_amount)


def get_user_choice():
    return input("Your choice:")


def print_blockchainelements():
    #Output the blockchain list to the console
    for block in blockchain:
        print(block)


def verify_chain():
    """Verify the current blockchain and return True if it's valid, False """
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if( block["previous_hash"] != hash_block(blockchain[index - 1])):
            return False
    return True
        

waiting_for_input = True
while waiting_for_input:
    print("Please choose:")
    print("1: Add a new transaction value")
    print("2: Mina a new block")
    print("3: Output the blockchain blocks")
    print("4: Output the partecipants")
    print("h: Manipulate the chain")
    print("q: To quit")
    user_choice = get_user_choice()
    if(user_choice == "1"):
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif(user_choice == "2"):
        if mine_block():
            open_transactions = []
    elif(user_choice == "3"):
        print_blockchainelements()
    elif(user_choice == "4"):
        print(partecipants)
    elif(user_choice == "h"):
        if len(blockchain) > 0:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transaction': [{'sender': 'Chris', 'recipient': 'Max', 'amount': 100}]
             }
    elif(user_choice == "q"):
        waiting_for_input = False
    else:
        print("Input was invalid, please pick a value from the list")

    if verify_chain() == False:
        print("invalid blockchain")
        waiting_for_input = False

else:
    print("User left!")

print("Done")
