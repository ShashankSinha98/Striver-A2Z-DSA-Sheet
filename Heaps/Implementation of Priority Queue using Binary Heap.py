#Initial Template for Python 3
H = [0] * 10009
s = -1

def parent(i):
    return (i - 1) // 2
    
def leftChild(i):
    return 2 * i + 1
    
def rightChild(i):
    return 2 * i + 2
    
def shiftUp(i):
    while i > 0 and H[parent(i)] < H[i]:
        H[parent(i)], H[i] = H[i], H[parent(i)]
        i = parent(i)
        
def shiftDown(i):
    maxIndex = i
    l = leftChild(i)
    if l <= s and H[l] > H[maxIndex]:
        maxIndex = l
    r = rightChild(i)
    if r <= s and H[r] > H[maxIndex]:
        maxIndex = r
    if (i != maxIndex):
        H[i], H[maxIndex] = H[maxIndex], H[i]
        shiftDown(maxIndex)

def insert(p):
    global s
    s += 1
    H[s] = p
    shiftUp(s)

from typing import Optional
class Solution:
    def extractMax(self):
        global s
        # Code here
        res = H[0]
        H[0] = H[s]
        s -= 1

        currPos = 0
        while(not self.isLeaf(currPos)):
            largestElementIdx = currPos

            if self.getLeftChild(currPos) != None and self.getLeftChild(currPos) > H[currPos]:
                largestElementIdx = 2*currPos + 1
            
            if self.getRightChild(currPos) != None and self.getRightChild(currPos) > H[largestElementIdx]:
                largestElementIdx = 2*currPos + 2
            
            if largestElementIdx==currPos:
                break
            
            H[currPos], H[largestElementIdx] = H[largestElementIdx], H[currPos]
            currPos = largestElementIdx
        
        return res
    
    def isLeaf(self, idx: int) -> bool:
        return (2*idx > s-1)

    def getLeftChild(self, idx: int) -> Optional[int|None]:
        if (2*idx+1 <= s):
            return H[2*idx+1]
        else:
            return None
        
    def getRightChild(self, idx: int) -> Optional[int|None]:
        if (2*idx+2 <= s):
            return H[2*idx+2]
        else:
            return None
