from typing import *

def getLongestZeroSumSubarrayLength(arr : List[int]) -> int:
        prefixSumDict = {}

        currSum = 0
        maxLen = 0
        for i in range(len(arr)):
            currSum += arr[i]

            if currSum == 0:
                maxLen = max(maxLen, i+1)
            else:
                target = currSum
                if target in prefixSumDict:
                    ti = prefixSumDict[target]
                    maxLen = max(maxLen, i-ti)
                
                if currSum not in prefixSumDict:
                    prefixSumDict[currSum] = i

        return maxLen

if __name__ == "__main__":
     nums = [1, 3, -5, 6, -2]
     print(getLongestZeroSumSubarrayLength(nums))  