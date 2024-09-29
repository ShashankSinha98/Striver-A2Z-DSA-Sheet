from os import *
from sys import *
from collections import *
from math import *

class Trie:

    class TrieNode:
        def __init__(self, ch: chr) -> None:
            self.char = ch
            self.childs = [None] * 26
            self.prefixCount = 0
            self.wordCount = 0


    def __init__(self):
        # Write your code here.
        self.root = Trie.TrieNode("")


    def insert(self, word):
        # Write your code here.
        curr: Trie.TrieNode = self.root

        for ch in word:
            if curr.childs[ord(ch)-ord('a')]==None:
                curr.childs[ord(ch)-ord('a')] = Trie.TrieNode(ch)
            curr = curr.childs[ord(ch)-ord('a')]
            curr.prefixCount += 1
        
        curr.wordCount += 1


    def countWordsEqualTo(self, word):
        curr: Trie.TrieNode = self.root

        for ch in word:
            if curr.childs[ord(ch)-ord('a')]==None:
                return 0
            curr = curr.childs[ord(ch)-ord('a')]
        
        return curr.wordCount


    def countWordsStartingWith(self, word):
        curr: Trie.TrieNode = self.root

        for ch in word:
            if curr.childs[ord(ch)-ord('a')]==None:
                return 0
            curr = curr.childs[ord(ch)-ord('a')]
        
        return curr.prefixCount


    def erase(self, word):
        curr: Trie.TrieNode = self.root
        for ch in word:
            curr = curr.childs[ord(ch)-ord('a')]
            curr.prefixCount -= 1
        
        curr.wordCount -= 1


if __name__ == "__main__":
    tr = Trie()
    tr.insert("coding")
    tr.insert("ninja")
    print(tr.countWordsEqualTo("coding"))
    print(tr.countWordsStartingWith("nin"))
    tr.erase("coding")
    print(tr.countWordsEqualTo("coding"))
