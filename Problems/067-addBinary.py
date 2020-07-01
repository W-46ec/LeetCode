class Solution:
	def addBinary(self, a, b):
		"""
		:type a: str
		:type b: str
		:rtype: str
		"""
		s = ""
		carry = 0

		if len(a) >= len(b):
			s1, s2 = a, b
		else:
			s1, s2 = b, a

		for i in range(len(s2)):
			s = str((int(s1[len(s1) - 1 - i]) + int(s2[len(s2) - 1 - i]) + carry) % 2) + s
			carry = (int(s1[len(s1) - 1 - i]) + int(s2[len(s2)- 1 - i]) + carry) // 2
		for i in range(len(s1) - len(s2)):
			s = str((int(s1[len(s1) - len(s2) - 1 - i]) + carry) % 2) + s
			carry = (int(s1[len(s1) - len(s2) - 1 - i]) + carry) // 2
		if carry == 1:
			s = '1' + s;
		return s



print(Solution().addBinary('1001', '0011'))