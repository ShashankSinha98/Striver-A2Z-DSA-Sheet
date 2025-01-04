class Solution:
    def solve(self, bt):
        bt.sort()
        tot_waiting_time = 0
        time_elapsed = 0
        for i in range(len(bt)):
            tot_waiting_time+=time_elapsed
            time_elapsed+=bt[i]

        return tot_waiting_time//len(bt)
    
if __name__ == "__main__":
    s = Solution()
    bt = [4,3,7,1,2]
    print(s.solve(bt))