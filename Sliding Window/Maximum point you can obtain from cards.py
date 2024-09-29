from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)

        if k >= n:
            return sum(cardPoints)

        lSum = sum(cardPoints[0:k])
        rSum  =  0
        l, r = k, n
        i = 0
        maxSum = lSum + rSum

        while i < k:
            l-=1
            lSum -= cardPoints[l]

            r-=1
            rSum += cardPoints[r]

            maxSum = max(maxSum, lSum + rSum)
            i+=1
        
        return maxSum
    

if __name__ == "__main__":
    s = Solution()
    cardPoints = [9,7,7,9,7,7,9]
    k = 7
    print(s.maxScore(cardPoints, k))


