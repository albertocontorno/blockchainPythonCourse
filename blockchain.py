# Initializing our blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Return the last value of the current blockchain. """
    if(len(blockchain) < 1):
        return None
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blockchain value to the blockchain.
    Arguments:
        :transaction_amount: The amount that should be addeed.
        :last_transaction: The last blockchain transaction (default [1])
    """
    if(last_transaction == None):
        last_transaction = [1]

    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float """
    return float(input("Your transaction amount please: "))


def get_user_choice():
    return input("Your choice:")


def print_blockchainelements():
    #Output the blockchain list to the console
    for block in blockchain:
        print(block)


def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1

    return is_valid

waiting_for_input = True
while waiting_for_input:
    print("Please choose:")
    print("1: Add a new transaction value")
    print("2: Output the blockchain blocks")
    print("h: Manipulate the chain")
    print("q: To quit")
    user_choice = get_user_choice()
    if(user_choice == "1"):
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif(user_choice == "2"):
        print_blockchainelements()
    elif(user_choice == "h"):
        if len(blockchain) > 0:
            blockchain[0] = 1
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