from Blockchain import Blockchain
from Block import Block


blockchain = Blockchain()
blocks = 10

for n in range(blocks):
    blockchain.mine(Block("Block " + str(n+1)))

while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next