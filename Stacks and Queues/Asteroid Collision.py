from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)

        st = []
        for i in range(n):
            if len(st)==0 or st[-1]<0 or (st[-1]>0 and asteroids[i]>0):
                st.append(asteroids[i])
            else:
                while len(st) > 0 and st[-1] > 0 and abs(asteroids[i]) > abs(st[-1]):
                    st.pop()
                
                
                if len(st) > 0 and st[-1] > 0 and abs(asteroids[i]) == abs(st[-1]):
                    st.pop()
                elif len(st) == 0 or st[-1] < 0:
                    st.append(asteroids[i])

        return st
    

if __name__ == "__main__":
    s = Solution()
    asteroids = [-2,-1,1,-2]
    print(s.asteroidCollision(asteroids))
