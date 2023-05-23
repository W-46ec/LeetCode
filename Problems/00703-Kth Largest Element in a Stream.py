
"""
# Kth Largest Element in a Stream

Design a class to find the `kth` largest element in a stream. Note that it is the `kth` largest element in the sorted order, not the `kth` distinct element.

Implement `KthLargest` class:
    - `KthLargest(int k, int[] nums)` Initializes the object with the integer `k` and the stream of integers `nums`.
    - `int add(int val)` Appends the integer `val` to the stream and returns the element representing the `kth` largest element in the stream.


**Example 1:** 
```
Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
```

**Constraints:** 
    - `1 <= k <= 10^4` 
    - `0 <= nums.length <= 10^4` 
    - `-10^4 <= nums[i] <= 10^4` 
    - `-10^4 <= val <= 10^4` 
    - At most `10^4` calls will be made to `add`.
    - It is guaranteed that there will be at least `k` elements in the array when you search for the `kth` element.
"""

from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.lst = sorted(nums)

    def add(self, val: int) -> int:
        lo, hi = 0, len(self.lst) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.lst[mid] == val:
                lo = mid
                break
            lo = mid + 1 if val > self.lst[mid] else lo
            hi = mid - 1 if val < self.lst[mid] else hi
        self.lst.insert(lo, val)
        return self.lst[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# Testcases:
# ["KthLargest","add","add","add","add","add"]
# [[3,[4,5,8,2]],[3],[5],[10],[9],[4]]
# ["KthLargest","add","add","add","add","add"]
# [[3,[5,-1]],[2],[1],[-1],[3],[4]]

# Expected:
# [null,4,5,5,8,8]
# [null,-1,1,1,2,3]

