class Node:
    def __init__(self, val = '') -> None:
        self.val = val
        self.links = {}
    def __repr__(self) -> str:
        return str(self.val) + '->' + str(self.links.keys())

class Trie:
    def __init__(self):
        self.head = Node('root')

    def insert(self, word: str) -> None:
        temp = self.head 
        
        for c in word:
            if c in temp.links:
                temp = temp.links[c]
            else:
                temp.links[c] = Node(val = c)
                temp = temp.links[c]
        temp.links['end'] = None
        

    def search(self, word: str) -> bool:
        temp = self.head
        for c in word:
            if c in temp.links:
                temp = temp.links[c]
            else:
                return False
        return True if 'end' in temp.links else False
            


    def startsWith(self, prefix: str) -> bool:
        temp = self.head
        for c in prefix:
            if c in temp.links:
                temp = temp.links[c]
            else:
                return False
        return True 


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('word')
obj.insert('work')
param_2 = obj.search("word")
print(o)
param_3 = obj.startsWith("prefix")