from typing import List
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand)%groupSize!=0:
            return False

        num_map = {}
        for k in hand:
            if k in num_map:
                num_map[k] += 1
            else:
                num_map[k] = 1
        
        heap = []
        for k in num_map.keys():
            heapq.heappush(heap, k)
        

        for _ in range(len(hand)//groupSize):
            tmp = heap[0]
            for _ in range(groupSize):
                if tmp not in num_map or num_map[tmp]==0:
                    return False
                num_map[tmp]-=1
                if num_map[tmp]==0:
                    heapq.heappop(heap)
                tmp = tmp+1
        
        return True


if __name__ == "__main__":
    s = Solution()
    hand = [1,2,3,4,5]
    groupSize = 4
    ans = s.isNStraightHand(hand, groupSize)
    print(ans)
                
        