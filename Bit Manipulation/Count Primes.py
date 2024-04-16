class Solution:
    
    # def __init__(self) -> None:
    #     max_lim = (5*(10**6)+1)
    #     self.is_prime = [1] * max_lim
    #     self.is_prime[0] = self.is_prime[1] = 0
    #     i = 2
    #     while i * i < max_lim:
    #         if self.is_prime[i] == 1:
    #             j = i * i
    #             while j < max_lim:
    #                 self.is_prime[j] = 0
    #                 j+=i
    #         i += 1
    
    def precompute_arr(self, n):
        lim = 3 if n < 2 else n
        max_lim = lim
        self.is_prime = [1] * max_lim
        self.is_prime[0] = self.is_prime[1] = 0
        i = 2
        while i * i < max_lim:
            if self.is_prime[i] == 1:
                j = i * i
                while j < max_lim:
                    self.is_prime[j] = 0
                    j+=i
            i += 1

    def countPrimes(self, n: int) -> int:
        self.precompute_arr(n)
        count = 0
        for i in range(n):
            if self.is_prime[i] == 1:
                count += 1
        return count

if __name__ == "__main__":
    s = Solution()
    print(s.countPrimes(10))