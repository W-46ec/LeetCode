
from typing import List

class Solution:
	def getNoZeroIntegers(self, n: int) -> List[int]:
		def noZero(x):
			return True if '0' not in str(x) else False
		for i in range(1, n):
			if noZero(i) and noZero(n - i):
				return [i, n - i]

print(Solution().getNoZeroIntegers(11))
print(Solution().getNoZeroIntegers(10000))
print(Solution().getNoZeroIntegers(69))
print(Solution().getNoZeroIntegers(1010))
