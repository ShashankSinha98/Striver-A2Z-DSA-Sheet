def aggressiveCows(stalls, k):
    stalls.sort()
    n = len(stalls)
    ans = 1

    l, r = 1, (stalls[n-1]-stalls[0])
    while l <= r:
        dist = l + (r-l) // 2
        cows_placed, dist_sum = 1, 0
        for i in range(1, n):
            dist_sum += stalls[i] - stalls[i-1]
            if dist_sum >= dist:
                cows_placed += 1
                dist_sum = 0

        if cows_placed >= k:
            ans = max(ans, dist)
            l = dist + 1
        else:
            r = dist - 1
    return ans
