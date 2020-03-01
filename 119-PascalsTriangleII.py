
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        while rowIndex + 1:
            for j in range(len(ans) - 1):
                ans[j] = ans[j] + ans[j + 1]
            ans = [1] + ans
            rowIndex -= 1
        return ans

print(Solution().getRow(3))
