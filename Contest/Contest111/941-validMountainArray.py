class Solution:
	def validMountainArray(self, A):
		"""
		:type A: List[int]
		:rtype: bool
		"""
		length = len(A)
		if length < 3:
			return False
		increasing = True
		for i in range(length - 1):
			if i == 0:
				if A[i + 1] <= A[i]:
					return False
			else:
				if increasing and A[i + 1] < A[i]:
					increasing = False
				if increasing:
					if A[i + 1] <= A[i]:
						return False
				else:
					if A[i + 1] >= A[i]:
						return False
		if not increasing:
			return True
		else:
			return False

print(Solution().validMountainArray([1, 2, 3, 2]))