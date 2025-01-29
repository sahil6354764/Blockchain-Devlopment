import hashlib
class Block:
    def __init__(self, index,timestamp,data,previous_has):
        self.index = Index
        self.timestamp = timestamp
        self.data = Data 
        self.previous_hash = Previous_has 
        self.hash = self.compute_hash
    
    def compute_hash(self):
        block_data = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_data.encode()).hexdigest()

if __name__=="__main__":
    #genesis block
    genesis_block =Block(
        index=0,
        timestamp="2025",
        data="genesis block data",
        previous_hash="0"
    )
print("genesis block:")
print(f"index: {genesis_block.index}")
print(f"timestamp: {genesis_block.timestamp}")
print(f"data: {genesis_block.data}")
print(f"previous hash: {genesis_block.previous_hash}")
