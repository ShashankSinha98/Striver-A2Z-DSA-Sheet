class Solution:
    def splitArray(self, arr: list[int], k: int) -> int:
        def __is_possible(self, arr, max_sum, k) -> bool:
            curr_sum = 0
            curr_partn = 1

            for i in range(len(arr)):
                if curr_sum + arr[i] <= max_sum:
                    curr_sum += arr[i]
                else:
                    curr_sum = arr[i]
                    curr_partn += 1

                    if curr_partn > k:
                        return False
            return curr_partn == k
        low, high = max(arr), sum(arr)
        ans = high

        while low <= high:
            max_sum = (low + high) // 2

            if __is_possible(self, arr, max_sum, k):
                ans = min(ans, max_sum)
                high = max_sum - 1
            else:
                low = max_sum + 1
        
        return ans
    
if __name__ == "__main__":
    arr = [1,2,3,4,5]
    k = 2
    ans = Solution().splitArray(arr, k)
    print(ans)


        