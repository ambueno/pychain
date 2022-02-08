from Chain import Chain

chain = Chain()

transaction1 = chain.add_transaction("Amanda", "Satoshi", '70 AC')

transaction2 = chain.add_transaction("Satoshi", "Java", '23 AC')

transaction3 = chain.add_transaction("Java", "Lucas", '34 AC')

chain.add_block(12345)

transaction4 = chain.add_transaction("Ullas", "Benvas", '11 AC')

transaction5 = chain.add_transaction("Leander", "Bryan", '3 AC')

transaction6 = chain.add_transaction("Marcus", "Honda", '88 AC')

chain.add_block(6789)

print(chain.blockchain)
