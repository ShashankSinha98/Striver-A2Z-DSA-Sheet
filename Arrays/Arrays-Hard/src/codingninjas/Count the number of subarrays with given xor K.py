def subarraysWithSumK(arr: [int], b: int) -> int:
    prefixXorDict = {}

    count = 0
    currXor = 0
    for i in range(len(arr)):
        currXor = currXor ^ arr[i]

        if currXor == b:
            count+=1
        
        remm = currXor ^ b
        #print("cx: ",currXor, " remm: ",remm)
        if remm in prefixXorDict:
            c = prefixXorDict[remm]
            count += c
        
        if currXor not in prefixXorDict:
            prefixXorDict[currXor] = 1
        else:
            c = prefixXorDict[currXor]
            prefixXorDict[currXor] = c + 1

    return count


if __name__ == "__main__":
    arr = [1, 3, 3, 3, 5]
    b = 6
    print(subarraysWithSumK(arr, b))
