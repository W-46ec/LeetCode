
"""
# Car Pooling

There is a car with `capacity` empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer `capacity` and an array `trips` where `trip[i] = [numPassengers_i, from_i, to_i]` indicates that the `ith` trip has `numPassengers_i` passengers and the locations to pick them up and drop them off are `from_i` and `to_i` respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return *`true` if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise*.


**Example 1:** 
```
Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
```

**Example 2:** 
```
Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
```

**Constraints:** 
    - `1 <= trips.length <= 1000` 
    - `trips[i].length == 3` 
    - `1 <= numPassengers_i <= 100` 
    - `0 <= from_i < to_i <= 1000` 
    - `1 <= capacity <= 10^5` 

**Hint #1** 
Sort the pickup and dropoff events by location, then process them in order.
"""

from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # # Brute force
        # time = [0] * 1001
        # for cap, start, end in trips:
        #     for i in range(start, end):
        #         time[i] += cap
        #         if time[i] > capacity:
        #             return False
        # return True

        # Time stamp
        # Break the (numPassengers, from, to) tuple into two pairs:
        #    - (from, +numPassengers)
        #    - (to,   -numPassengers)
        # They indicate the change of the number of 
        # passengers at each timestamp.
        timestamp = sorted([(start, n) for n, start, end in trips] 
                           + [(end, -n) for n, start, end in trips])

        # At any timestamp, the number of passengers must not exceed
        # capacity. Otherwise, return False.
        curr_psg_num = 0
        for t, change in timestamp:
            curr_psg_num += change
            if curr_psg_num > capacity:
                return False
        return True

# False
print(Solution().carPooling([[2, 1, 5], [3, 3, 7]], 4))

# True
print(Solution().carPooling([[2, 1, 5], [3, 3, 7]], 5))

# True
print(Solution().carPooling([[2, 1, 5], [3, 5, 7]], 3))

# True
print(Solution().carPooling([[3, 2, 7], [3, 7, 9], [8, 3, 9]], 11))

# True
print(Solution().carPooling([[9, 3, 4], [9, 1, 7], [4, 2, 4], [7, 4, 5]], 23))

