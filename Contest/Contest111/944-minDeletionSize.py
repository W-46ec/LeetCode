class Solution:
	def minDeletionSize(self, A):
		"""
		:type A: List[str]
		:rtype: int
		"""
		count = 0
		for i in range(len(A[0])):
			s = "".join([row[i] for row in A])
			if s != "".join(sorted(s)):
				count += 1
		return count

print(Solution().minDeletionSize(["zyx","wvu","tsr"]))