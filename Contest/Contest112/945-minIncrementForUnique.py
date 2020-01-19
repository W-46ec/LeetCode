class Solution:
	def minIncrementForUnique(self, A):
		"""
		:type A: List[int]
		:rtype: int
		"""
		count = 0
		A = sorted(A)
		for i in range(len(A) - 1):
			if A[i] == A[i + 1]:
				count += 1
				A[i + 1] += 1
			elif A[i] > A[i + 1]:
				count += (A[i] - A[i + 1] + 1)
				A[i + 1] += (A[i] - A[i + 1] + 1)
		return count

print(Solution().minIncrementForUnique([3, 2, 1, 2, 1, 7]))
print(Solution().minIncrementForUnique([1, 2, 2, 2, 4]))