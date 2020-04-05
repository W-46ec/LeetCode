
class Solution:
	def numSteps(self, s: str) -> int:
		dec, exp, count = 0, 0, 0
		for i in range(len(s))[::-1]:
			dec += int(s[i]) * (2 ** exp)
			exp += 1
		# print(dec)
		while dec > 1:
			if dec % 2 == 0:
				dec //= 2
			else:
				dec += 1
			count += 1
		return count

print(Solution().numSteps("1101"))
print(Solution().numSteps("10"))
print(Solution().numSteps("1"))
print(Solution().numSteps("0"))
