blockchain = [[1]]


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount):
    blockchain.append([get_last_blockchain_value(), transaction_amount])

add_value(5.3)
add_value(4)
add_value(2)

print(blockchain)
