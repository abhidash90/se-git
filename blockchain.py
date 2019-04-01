import hashlib

def generatehash(value,prev_hash,txn_id):
	m = hashlib.sha256(value+prev_hash+txn_id)
	return m.digest()

def gitadd:
    print("git verification")
	
def getgenesisblock():
	return Block(1,0,1)

class Block:
	def __init__(self,value,prev_hash,txn_id):
		self.value = value
		self.prev_hash = prev_hash
		self.txn_id = txn_id
		self.hash =  generatehash(value,prev_hash,txn_id)
		
		
class Blockchain:
	current = None
	block_list = list()
	def __init__(self):
		Blockchain.current = 0
		Blockchain.block_list.append(getgenesisblock())
	
	def addblock(value,txn_id):
		cur_block = Blockchain.block_list[current]
		new_block = Block(value,cur_block.hash,txn_id)
		Blockchain.block_list.append(new_block)
		current+=1
		

block_chain = Blockchain()
block_chain.addblock(20,1335)
print(Blockchain.block_list)
			