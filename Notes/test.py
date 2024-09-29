from typing import List, Tuple
from bisect import bisect_left
from collections import Counter

def cmp(a: Tuple[int, int], b: Tuple[int, int]) -> bool:
    # Sort primarily by sweetness descending, then by time ascending
    return a[0] > b[0] or (a[0] == b[0] and a[1] < b[1])

def make_sweets(time: List[int], sweetness: List[int], daytime: List[int]) -> Tuple[int, int]:
    n = len(time)
    sweets = [(sweetness[i], time[i]) for i in range(n)]

    # Sort sweets using the custom comparator
    sweets.sort(key=lambda x: (-x[0], x[1]))

    # Use a Counter to track available days
    available_days = Counter(daytime)
    
    cnt_sweets = 0
    total_sweetness = 0

    for sweet in sweets:
        sweetness_value = sweet[0]
        time_required = sweet[1]

        # Find the first available day with enough time
        suitable_days = [day for day in available_days if day >= time_required]
        if suitable_days:
            day_to_use = min(suitable_days)

            # Decrease the count of that available day
            available_days[day_to_use] -= 1
            if available_days[day_to_use] == 0:
                del available_days[day_to_use]
            
            cnt_sweets += 1
            total_sweetness += sweetness_value

    return cnt_sweets, total_sweetness


if __name__ == "__main__":
    n, m = 3, 3
    A = [10, 2, 5]
    B = [40, 90, 20]
    C = [4,7,4]

    print(make_sweets(A,B,C))