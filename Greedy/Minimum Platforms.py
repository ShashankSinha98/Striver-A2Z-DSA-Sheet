class Solution:    
    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        # code here
        arr.sort()
        dep.sort()

        ai, di, n = 0, 0, len(arr)
        platformsInUse, maxPlatformsUses = 0, 0

        while ai<n and di<n:
            arrival_time = arr[ai]
            departure_time = dep[di]

            # Train arrives, need platform
            if arrival_time <= departure_time:
                platformsInUse+=1
                maxPlatformsUses = max(maxPlatformsUses, platformsInUse)
                ai+=1
            else:
            # Train departs, one platform empty
                platformsInUse-=1
                di+=1
        
        return maxPlatformsUses


if __name__ == "__main__":
    s = Solution()
    arr = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]

    print(s.minimumPlatform(arr, dep))


