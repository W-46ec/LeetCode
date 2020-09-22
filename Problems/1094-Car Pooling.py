
"""
# Car Pooling

You are driving a vehicle that has `capacity` empty seats initially available for passengers. The vehicle **only** drives east (ie. it **cannot** turn around and drive west.)

Given a list of `trips`, `trip[i] = [num_passengers, start_location, end_location]` contains information about the `i`-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off. The locations are given as the number of kilometers due east from your vehicle's initial location.

Return `true` if and only if it is possible to pick up and drop off all passengers for all the given trips. 


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

**Example 3:** 
```
Input: trips = [[2,1,5],[3,5,7]], capacity = 3
Output: true
```

**Example 4:** 
```
Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
Output: true
```

**Constraints:** 
    1. `trips.length <= 1000` 
    2. `trips[i].length == 3` 
    3. `1 <= trips[i][0] <= 100` 
    4. `0 <= trips[i][1] < trips[i][2] <= 1000` 
    5. `1 <= capacity <= 100000` 

**Hint #1** 
Sort the pickup and dropoff events by location, then process them in order.
"""

from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        time = [0] * 1001
        for cap, start, end in trips:
            for i in range(start, end):
                time[i] += cap
                if time[i] > capacity:
                    return False
        return True

print(Solution().carPooling([[2, 1, 5], [3, 3, 7]], 4))             # False
print(Solution().carPooling([[2, 1, 5], [3, 3, 7]], 5))             # True
print(Solution().carPooling([[2, 1, 5], [3, 5, 7]], 3))             # True
print(Solution().carPooling([[3, 2, 7], [3, 7, 9], [8, 3, 9]], 11)) # True

