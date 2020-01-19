class Solution:
	def numSubarraysWithSum(self, A, S):
		"""
		:type A: List[int]
		:type S: int
		:rtype: int
		"""
		ans, length = 0, len(A)
		if A.count(1) == 0 and S == 0:
			return int(length * (length + 1) / 2)
		for i in range(length):
			count = 0
			for j in range(i, length):
				count += A[j]
				if count == S:
					ans += 1
				if count > S:
					break
			if count < S:
				break;
		return ans

l = [0, 1, 1, 0, 0, 1]

print(Solution().numSubarraysWithSum(l, 3))