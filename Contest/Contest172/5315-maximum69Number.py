
class Solution:
	def maximum69Number(self, num: int) -> int:
		s = str(num)
		if '6' not in s:
			return num
		else:
			l = list(s)
			l[s.index('6')] = '9'
			return int("".join(l))

print(Solution().maximum69Number(9669))
print(Solution().maximum69Number(9996))
print(Solution().maximum69Number(9999))
