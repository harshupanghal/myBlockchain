# -- this library will provide us the imp. functions and algorithms like SHA-256
import hashlib        

# -- Function to generate hash of a block
def hashGenerator(data):          
    result=hashlib.sha256(data.encode())
  
    return result.hexdigest()              # -- used to convert 'result' into hexadecimal

# -- provide a structure to block
class Block:                
    def __init__(self,data,hash,prev_hash):
        self.data=data
        self.hash=hash
        self.prev_hash=prev_hash

class Blockchain:
    def __init__(self):
      genesisPrev=hashGenerator('gen_last')     # -- used to generate previous hash for the genesis block, we can also use it as "0"
      genesisHash=hashGenerator('gen_hash')     # -- generating hash for genesis block

      genesis=Block('genesis-Block',genesisHash,genesisPrev)
      
      self.chain=[genesis]                      # -- used to make a chain and add the block

    def add_block(self,data):
        prev_hash=self.chain[-1].hash           # -- used to get the hash of previous added block
        hash=hashGenerator(data+prev_hash)      # -- herewe are using current block's data and previous hash value to generate the current hash
      
        block=Block(data,hash,prev_hash)
        self.chain.append(block)

blo=Blockchain()
blo.add_block('1')
blo.add_block('2')
blo.add_block('3')

for block in blo.chain:
    print(block.__dict__)                      # -- transforming the chain into a dictionary to print all info. of a block
