heap = [None for i in range(101)]  # our heap to be used
curr_size = 0

def insertKey (x):
    global curr_size
    
    heap[curr_size] = x
    curr_size += 1

    heapifyUp(idx = curr_size-1)

#Function to delete a key at ith index.
def deleteKey (i):
    global curr_size
    # edge cases
    if i >= curr_size or i < 0:
        return
    heap[i] = heap[curr_size-1]
    curr_size -= 1
    
    currPos = i
    if currPos > 0 and heap[currPos] < heap[(currPos-1)//2]:
        heapifyUp(currPos)
    else:
        heapifyDown(currPos)


#Function to extract minimum value in heap and then to store 
#next minimum value at first index.
def extractMin ():
    global  curr_size
    # edge case
    if curr_size == 0:
        return -1

    res = heap[0] 
    heap[0] = heap[curr_size-1]
    curr_size -= 1

    currPos = 0
    heapifyDown(currPos)
    return res

def heapifyUp(idx: int):
    currPos = idx
    
    while(currPos > 0):
        parentIdx = (currPos-1)//2
        if heap[parentIdx] > heap[currPos]:
            heap[currPos], heap[parentIdx] = heap[parentIdx], heap[currPos]
            currPos = parentIdx
        else:
            break

def heapifyDown(idx: int):
    currPos = idx

    while(not isLeaf(currPos)):
        smallestElementIdx = currPos

        if getLeftChild(currPos)!=None and getLeftChild(currPos) < heap[smallestElementIdx]:
            smallestElementIdx = 2*currPos+1

        if getRightChild(currPos)!=None and getRightChild(currPos) < heap[smallestElementIdx]:
            smallestElementIdx = 2*currPos+2
        
        if smallestElementIdx==currPos:
            break

        heap[currPos], heap[smallestElementIdx] = heap[smallestElementIdx], heap[currPos]  
        currPos = smallestElementIdx

def getLeftChild(idx: int) -> int:
    global curr_size
    if(2*idx+1 < curr_size):
        return heap[2*idx+1]
    else:
        return None
    
def getRightChild(idx: int) -> int:
    global curr_size
    if(2*idx+2 < curr_size):
        return heap[2*idx+2]
    else:
        return None

def isLeaf(idx:int) -> bool:
    return 2*idx >= curr_size-1


if __name__ == "__main__":
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        # initialize every globals
        curr_size = 0
        heap = [0 for i in range(n)]
        i = 0
        while i < len(a):
            if a[i] == 1:
                insertKey(a[i + 1])
                i += 1
            elif a[i] == 2:
                deleteKey(a[i + 1])
                i += 1
            else:
                print(extractMin (), end=" ")
            i += 1



