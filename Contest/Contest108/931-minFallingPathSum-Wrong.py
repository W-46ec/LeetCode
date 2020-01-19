class Solution:
	def minFallingPathSum(self, A):
		"""
		:type A: List[List[int]]
		:rtype: int
		"""
		return sum([min(i) for i in A])

print(Solution().minFallingPathSum([
	[-80, -13, 22], 
	[83, 94, -5], 
	[73, -48, 61]
]))