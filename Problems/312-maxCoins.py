
from typing import List

class Solution:
	def maxCoins(self, nums: List[int]) -> int:
		length = len(nums)
		dp = [[1] * (length + 2)]
		dp += [([1] + [0] * length + [1]) for i in range(length)]
		dp += [[1] * (length + 2)]
		print(dp)
		for i in range(1, length + 1):
			for j in range(i, length + 1):
				for k in range(i, j + 1):
					coins = dp[i][k] + nums[i - 1] * nums[k - 1] * nums[j - 1] + dp[k][j]
					if coins > dp[i][j]:
						dp[i][j] = coins
		print(dp)
		return dp[1][length]

print(Solution().maxCoins([3, 1, 5, 8]))
