
from typing import List
from math import factorial

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        for i in range(len(rating) - 2):
            for j in range(i + 1, len(rating) - 1):
                for k in range(j + 1, len(rating)):
                    if rating[i] < rating[j] and rating [j] < rating[k]:
                        count += 1
                    if rating[i] > rating[j] and rating [j] > rating[k]:
                        count += 1
        return count

print(Solution().numTeams([2, 5, 3, 4, 1]))
print(Solution().numTeams([2, 1, 3]))
print(Solution().numTeams([1, 2, 3, 4]))
