from Chain import Chain

chain = Chain()

transaction1 = chain.add_transaction("Vitalik", "Satoshi", 100)

transaction2 = chain.add_transaction("Satoshi", "Alice", 10)

transaction3 = chain.add_transaction("Alice", "Charlie", 34)

chain.add_block(12345)

transaction4 = chain.add_transaction("Bob", "Eve", 23)

transaction5 = chain.add_transaction("Dennis", "Brian", 3)

transaction6 = chain.add_transaction("Ken", "Doug", 88)

chain.add_block(6789)

print(chain.blockchain)

