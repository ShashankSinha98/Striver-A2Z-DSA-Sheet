class Solution:
    def XOR(self, n, m):
        return n ^ m
    
    def check(self, a, b):
        return 1 if(1<<(a-1)) & b > 0 else 0
    
    def setBit(self, c, d):
        return (1<<c) | d
    

if __name__ == "__main__":
    s = Solution()
    print(s.XOR(1,2))
    print(s.check(3,4))
    print(s.setBit(5,6))