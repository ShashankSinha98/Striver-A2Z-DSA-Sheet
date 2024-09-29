class Solution:
    def sumSubarrayMins(self, N, fruits):
        num_idx_dict = {}
        l, r = 0, 0
        max_len = 0
        
        while l < N and r < N:
            fruit_type = fruits[r]

            if (fruit_type not in num_idx_dict and len(num_idx_dict) < 2) or (fruit_type in num_idx_dict):
                num_idx_dict[fruit_type] = r
                max_len = max(max_len, r-l+1)
                r+=1
            else:
                min_idx = N
                min_key = None

                for k, v in num_idx_dict.items():
                    if v < min_idx:
                        min_idx = v
                        min_key = k
                
                l = min_idx + 1
                num_idx_dict.pop(min_key)

        return max_len
    

if __name__ == "__main__":
    s = Solution()
    fruits = [0,1,2,2,1,1,3,3,1,1,1,2,0]
    N = len(fruits)

    print(s.sumSubarrayMins(N, fruits))