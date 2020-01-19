
from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        if n <= 1:
            return [0]
        if n % 2 == 0:
            for i in range(1, n // 2 + 1):
                ans.append(i)
                ans.append(i * -1)
        else:
            for i in range(1, n // 2):
                ans.append(i)
                ans.append(i * -1)
            ans.append(n)
            ans.append(n + 1)
            ans.append(-2 * n - 1)
        return ans

print(Solution().sumZero(5))
print(Solution().sumZero(3))
print(Solution().sumZero(1))
