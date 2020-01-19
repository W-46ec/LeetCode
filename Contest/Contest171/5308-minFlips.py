
class Solution:
	def minFlips(self, a: int, b: int, c: int) -> int:
		count = 0
		while a or b or c:
			x, y, z = a & 0x1, b & 0x1, c & 0x1
			if z == 1:
				if x + y == 0:
					count += 1
			else:
				count += 1 if x else 0
				count += 1 if y else 0
			a >>= 1
			b >>= 1
			c >>= 1
		return count

print(Solution().minFlips(2, 6, 5))
print(Solution().minFlips(4, 2, 7))
print(Solution().minFlips(1, 2, 3))
