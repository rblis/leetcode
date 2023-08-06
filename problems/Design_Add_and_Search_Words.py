import collections
class Trie:
    def __init__(self) -> None:
        self.links = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.tri = Trie()

    def addWord(self, word: str) -> None:
        head = self.tri
        for c in word:
            if c not in head.links: head.links[c] = Trie()
            head = head.links[c]
        head.end = True
        


    def search(self, word: str) -> bool:
        def dfs(index, root):
            node  = root
            for i in range(index, len(word)):
                if word[i] == '.':
                    for link in node.links.values():#search all the links to see if next character matches one of the links
                        if dfs(i+1, link): return True
                    return False
                else:
                    if word[i] not in node.links: return False
                    node = node.links[word[i]]
            return node.end
        return dfs(0,self.tri)



# Your WordDictionary object will be instantiated and called as such:
'''
Implement the WordDictionary class:

    WordDictionary() Initializes the object.
    void addWord(word) Adds word to the data structure, it can be matched later.
    bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

'''
obj = WordDictionary()
obj.addWord('a')
obj.addWord('ab')
obj.addWord('mad')
print(obj.search('a'))

'''
    def __init__(self):
        self.tri = Trie('head')

    def addWord(self, word: str) -> None:
        a = self.tri
        dot = None
        for c in word:
            if c not in a.links: a.links[c] = Trie(c)
            if '.' not in a.links: a.links['.'] = Trie('.')
            dot = a.links['.']
            a = a.links[c]
            dot.links = a.links
        a.links['end'] = None
        


    def search(self, word: str) -> bool:
        head = self.tri
        for c in word:
            if c not in head.links: return False
            head = head.links[c]
        if 'end' in head.links: return True
        return False
'''