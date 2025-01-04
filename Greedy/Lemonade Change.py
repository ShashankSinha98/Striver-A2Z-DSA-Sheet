from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        wallet = {5:0, 10:0, 20:0}

        for bi in bills:
            wallet[bi]+=1
            change = bi - 5
            if change==15:
                if wallet[5]>=1 and wallet[10]>=1:
                    wallet[5]-=1
                    wallet[10]-=1
                elif wallet[5]>=3:
                    wallet[5]-=3
                else:
                    return False
            elif change==5:
                if wallet[5]>=1:
                    wallet[5]-=1
                else:
                    return False
        return True


if __name__ == "__main__":
    s = Solution()
    bills = [5,5,10,10,20]
    print(s.lemonadeChange(bills))
