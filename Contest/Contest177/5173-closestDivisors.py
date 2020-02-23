
from typing import List
from math import sqrt

class Solution:
	def closestDivisors(self, num: int) -> List[int]:
		d1, d2 = int(sqrt(num + 1)), int(sqrt(num + 2))
		while (num + 1) % d1 != 0:
			d1 -= 1
		while (num + 2) % d2 != 0:
			d2 -= 1
		diff1, diff2 = abs(d1 - (num + 1) // d1), abs(d2 - (num + 2) // d2)
		return [d1, (num + 1) // d1] if diff1 < diff2 else [d2, (num + 2) // d2]


print(Solution().closestDivisors(8))
print(Solution().closestDivisors(123))
print(Solution().closestDivisors(999))
print(Solution().closestDivisors(1))
