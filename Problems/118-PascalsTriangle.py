
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            if i == 0:
                ans.append([1])
                continue
            row = []
            for j in range(len(ans[-1])):
                if j == 0:
                    row.append(1)
                else:
                    row.append(ans[-1][j - 1] + ans[-1][j])
            row.append(1)
            ans.append(row)
        return ans

print(Solution().generate(5))
