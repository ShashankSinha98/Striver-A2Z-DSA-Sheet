from typing import Optional


class Trie:

    class TrieNode:
        def __init__(self, ch: chr) -> None:
            self.char = ch
            self.childs = [None] * 26
            self.isEnd = False


    def __init__(self):
        self.root = Trie.TrieNode('')
        

    def insert(self, word: str) -> None:
        curr = self.root

        for ch in word:
            
            if curr.childs[ord(ch)-ord('a')] == None:
                curr.childs[ord(ch)-ord('a')] = Trie.TrieNode(ch)
            
            curr = curr.childs[ord(ch)-ord('a')]
        
        curr.isEnd = True


    def display(self) -> None:
        def _display(currN: Trie.TrieNode, currS: str) -> None:
            if currN.isEnd:
                print(currS)
            
            for i, n in enumerate(currN.childs):
                if n != None:
                    _display(n, currS+chr(i+ord('a')))
        
        _display(self.root, "")


    def search(self, word: str) -> bool:
        curr = self.root

        for ch in word:
            if curr.childs[ord(ch)-ord('a')] == None:
                return False
            curr = curr.childs[ord(ch)-ord('a')]
        
        return curr.isEnd


    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for ch in prefix:
            if curr.childs[ord(ch)-ord('a')] == None:
                return False
            curr = curr.childs[ord(ch)-ord('a')]
        
        return True


if __name__ == "__main__":

    tr = Trie()
    tr.insert('apple')
    print(tr.search('apple'))
    print(tr.search('app'))
    print(tr.startsWith('app'))
    tr.insert('app')
    print(tr.search('app'))
    tr.display()
