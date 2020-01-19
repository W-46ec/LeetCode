class Solution:
	def brokenCalc(self, X: 'int', Y: 'int') -> 'int':
		def solve(X, Y):
			# print(X, Y)
			if X >= Y:
				return (X - Y)
			if 2 * X == Y:
				return 1
			elif 2 * X > Y:
				return 1 + min(X - (Y // 2), 2 * X - Y)
			else:
				if Y % 2 == 1:
					return 2 + solve(X, Y // 2 + 1)
				else:
					return 1 + solve(X, Y // 2)
		return solve(X, Y)

print(Solution().brokenCalc(2, 2))
print(Solution().brokenCalc(2, 3))
print(Solution().brokenCalc(5, 8))
print(Solution().brokenCalc(3, 10))
print(Solution().brokenCalc(1024, 24))
print(Solution().brokenCalc(1, 1000000000))