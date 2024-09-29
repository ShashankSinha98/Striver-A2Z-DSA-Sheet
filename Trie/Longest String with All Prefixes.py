from sys import *
from collections import *
from math import *

from typing import *

class TrieNode:
    def __init__(self, c: chr) -> None:
        self.c = c
        self.childrens = [None] * 26
        self.isWordEnd = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode(c='\0')
    
    def add(self, s):
        tmp = self.root
        for c in s:
            if tmp.childrens[ord(c)-ord('a')]==None:
                nn = TrieNode(c)
                tmp.childrens[ord(c)-ord('a')] = nn
            tmp = tmp.childrens[ord(c)-ord('a')]
        
        tmp.isWordEnd = True
    

    def isPresent(self, s) -> bool:
        tmp = self.root
        for c in s:
            if tmp.childrens[ord(c)-ord('a')]==None:
                return False

            tmp = tmp.childrens[ord(c)-ord('a')]
        
        return tmp.isWordEnd

def completeString(n: int, a: List[str])-> str:
    
    tr = Trie()
    maxLen = 0
    res = None

    for ai in a:
        tr.add(s=ai)
    
    for i in range(len(a)):
        ai = a[i]

        if len(ai) >= maxLen:
            isComplete = True
            for j in range(len(a)):
                s = ai[:j+1]
                if not tr.isPresent(s):
                    isComplete = False
                    break
            if isComplete:
                if len(ai) > maxLen:
                    maxLen = len(ai)
                    res = ai
                elif len(ai) == maxLen:
                    if ai < res:
                        res = ai
    return res


if __name__ == "__main__":
    arr = ["n", "ni", "nin", "ninj", "ninja", "abcde","a","ab","abc","abcd"]
    print(completeString(len(arr), arr))
