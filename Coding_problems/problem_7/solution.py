class TrieNode:
    def __init__(self):
        self.children = {}
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):  # Assuming 32-bit numbers
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
    
    def find_max_xor(self, num):
        node = self.root
        max_xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            # We try to pick the opposite bit to maximize XOR
            toggle_bit = 1 - bit  
            if toggle_bit in node.children:
                max_xor |= (1 << i)
                node = node.children[toggle_bit]
            else:
                node = node.children[bit]
        return max_xor

def find_max_xor(nums):
    trie = Trie()
    max_xor = 0
    
    for num in nums:
        trie.insert(num)
    
    for num in nums:
        max_xor = max(max_xor, trie.find_max_xor(num))
    
    return max_xor

# Example usage
nums = [3, 10, 5, 25, 2, 8]
print(find_max_xor(nums))  # Output: 28
