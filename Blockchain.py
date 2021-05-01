from Block import Block

class Blockchain:

    difficulty = 10
    maxNonce = 2**32
    target = 2 ** (256-difficulty)

    block = Block("Genesis")
    dummy = head = block

    def add(self, block):

        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1

        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1


def main():
    blockchain = Blockchain()
    blockchain.mine(Block("Test 1"))


if __name__ == '__main__':
    main()