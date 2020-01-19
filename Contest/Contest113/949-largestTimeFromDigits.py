from itertools import permutations
class Solution:
	def largestTimeFromDigits(self, A):
		"""
		:type A: List[int]
		:rtype: str
		"""
		def tranToSec(l):
			return (l[0] * 10 + l[1]) * 60 + l[2] * 10 + l[3]

		l = list(permutations(A))
		l = [i for i in l if 0 <= (i[0] * 10 + i[1]) <= 23 and 0 <= (i[2] * 10 + i[3]) <= 59]
		h1, h2, m1, m2 = -1, -1, -1, -1
		for i in l:
			if tranToSec(i) > tranToSec([h1, h2, m1, m2]):
				h1, h2, m1, m2 = i
		if h1 == -1:
			return ""
		return str(h1) + str(h2) + ':' + str(m1) + str(m2)


print(Solution().largestTimeFromDigits([1, 2, 3, 4]))
print(Solution().largestTimeFromDigits([1, 2, 2, 1]))
print(Solution().largestTimeFromDigits([5, 5, 5, 5]))
print(Solution().largestTimeFromDigits([0, 0, 0, 1]))