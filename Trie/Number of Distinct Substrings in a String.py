class TrieNode:
    def __init__(self, c: chr) -> None:
        self.c = c
        self.childrens = [None] * 26


class Trie:

    def __init__(self) -> None:
        self.root = TrieNode(c='\0')
        self.ref = None
    
    def add(self, c: str, node: TrieNode) -> tuple[int, TrieNode]:
        cnt = 0
          
        if node.childrens[ord(c)-ord('a')]==None:
            nn = TrieNode(c)
            node.childrens[ord(c)-ord('a')] = nn
            cnt+=1
        
        newRef = node.childrens[ord(c)-ord('a')]
        
        return (cnt, newRef)


def countDistinctSubstrings(s) -> int:
    ans = 0
    trie = Trie()
    for i in range(len(s)):
        node = trie.root
        for j in range(i, len(s)):
            c = s[j]
            count, node = trie.add(c, node)
            ans+=count
    
    return ans+1


if __name__ == "__main__":
    s = input("Enter the string: ")
    ans = countDistinctSubstrings(s)
    print("Total no of distinct substrings are: "+str(ans))
