from hashlib import sha256
import json
import time


class Chain(object):
    def __init__(self):
        self.blockchain = []
        self.pending_transactions = []
        self.add_block(previous_hash="The Times 03/09/2009 Chancellor on brink of second bailout for banks.", proof=123)

    def add_block(self, proof, previous_hash=None):
        block = {
            "index": len(self.blockchain),
            "timestamp": time.time(),
            "transactions": self.pending_transactions,
            "proof": proof,
            "previous_hash": previous_hash or self.hash(self.blockchain[-1]),
        }
        self.pending_transactions = []
        self.blockchain.append(block)

        return block

    def add_transaction(self, sender, recipient, amount):
        transaction = {
            "sender": sender,
            "recipient": recipient,
            "amount": amount
        }
        self.pending_transactions.append(transaction)

        return self.last_block['index'] + 1

    @property
    def last_block(self):
        return self.blockchain[-1]

    @staticmethod
    def hash(block):
        json_block = json.dumps(block, sort_keys=True).encode()
        return sha256(json_block).hexdigest()

    def proof_of_work(self, previous_proof):
        proof = 0
        while self.check_proof(previous_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def check_proof(previous_proof, proof):
        if (sha256(str(proof ** 2 - previous_proof ** 2).encode()).hexdigest()) == '0000':
            return True

    def valid_proof(self, blockchain):
        previous_block = self.blockchain[0]
        block_index = 0

        while block_index < len(blockchain) - 1:
            block = blockchain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            current_proof = block['proof']
            if (sha256(str(current_proof ** 2 - previous_proof ** 2).encode()).hexdigest()) != '0000':
                return False

            previous_block = block
            block_index += 1
        return True
