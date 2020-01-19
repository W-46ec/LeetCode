
from typing import List

class Solution:
	def canReach(self, arr: List[int], start: int) -> bool:
		length = len(arr)
		visited = [False] * length
		def solve(idx):
			if idx < 0 or idx >= length:
				return False
			if visited[idx]:
				return False
			if arr[idx] == 0:
				return True
			visited[idx] = True
			return solve(idx - arr[idx]) or solve(idx + arr[idx])
		return solve(start - arr[start]) or solve(start + arr[start])

print(Solution().canReach([4,2,3,0,3,1,2], 5))
print(Solution().canReach([4,2,3,0,3,1,2], 0))
print(Solution().canReach([3,0,2,1,2], 2))
