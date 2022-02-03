from hashlib import sha256

import json
import time


class Chain:
    def __init__(self):
        self.blockchain = []
        self.pending = []
        self.add_block(prevhash="Genesis", proof=123)

    def add_transaction(self, sender, recipient, amount):
        transaction = {
            "sender": sender,
            "recipient": recipient,
            "amount": amount
        }
        self.pending.append(transaction)

    def compute_hash(self, block):
        json_block = json.dumps(block, sort_keys=True).encode()
        current_hash = sha256(json_block).hexdigest()
        return current_hash

    def add_block(self, proof, prevhash=None,):
        block = {
            "index": len(self.blockchain),
            "timestamp": time.time(),
            "transactions": self.pending,
            "proof": proof,
            "prevhash": prevhash or self.compute_hash(self.blockchain[-1])
        }
        self.pending = []
        self.blockchain.append(block)
