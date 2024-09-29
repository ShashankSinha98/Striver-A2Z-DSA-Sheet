import sys

class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        res = 0

        prefix_sum = []
        for i in range(n):
            ch = s[i]
            if i == 0:
                c_arr = [0] * 26
            else:
                c_arr = list(prefix_sum[-1])
            c_arr[ord(ch) - ord('a')] += 1
            prefix_sum.append(c_arr)

        for i in range(n):
            for j in range(i, n):
                start, end = None, prefix_sum[j]
                if i==0:
                    start = [0]*26
                else:
                    start = prefix_sum[i-1]
                
                diff = [end[k] - start[k] for k in range(26)]
                maxima = max(diff)
                minima = sys.maxsize
                for k in diff:
                    if k != 0:
                        minima = min(minima, k)
                
                res += (maxima - minima)

        return res
    
    # def calculate_beauty(self, s: str) -> int:
    #     c_arr = [0]*26
    #     for i in s:
    #         idx = ord(i)-ord('a')
    #         c_arr[idx] += 1

    #     minima = sys.maxsize
    #     for i in c_arr:
    #         if i != 0:
    #             minima = min(minima, i)
        
    #     return max(c_arr) - minima


if __name__ == "__main__":
    s = "aabcb"
    print(Solution().beautySum(s))