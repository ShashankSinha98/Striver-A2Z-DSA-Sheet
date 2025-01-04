class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, val, wt, capacity):
        val_wt = []
        n = len(val)

        for i in range(n):
            r = (val[i]*1.0)/wt[i]
            val_wt.append((r, i))

        val_wt.sort(key=lambda v: v[0], reverse=True)
        tot_val = 0

        while len(val_wt)>0 and capacity > 0:
            r, i = val_wt.pop(0)
            _val = val[i]
            _wt = wt[i]
            #print(_val, _wt, capacity, tot_val, r)
            if _wt <= capacity:
                capacity -= _wt
                tot_val += _val
            else:
                pVal = r * capacity
                tot_val += pVal
                capacity = 0
        
        return round(tot_val*1.0, 6)


if __name__ == "__main__":
    s = Solution()
    val = [10, 20,30]
    wt = [5,10, 15]
    c = 100
    ans = s.fractionalknapsack(val, wt, c)
    print(ans)
