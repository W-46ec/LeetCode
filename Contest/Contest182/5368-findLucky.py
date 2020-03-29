
from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lst = sorted(list(set(arr)), reverse = True)
        for i in lst:
            if i == arr.count(i):
                return i
        return -1

print(Solution().findLucky([2, 2, 3, 4]))
print(Solution().findLucky([1, 2, 2, 3, 3, 3]))
print(Solution().findLucky([5]))
