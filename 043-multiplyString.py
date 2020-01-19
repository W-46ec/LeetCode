class Solution:
	def multiply(self, num1, num2):
		"""
		:type num1: str
		:type num2: str
		:rtype: str
		"""
		return str(int(num1) * int(num2))

s1 = "88994039749630997005046990281879989302276369350"
s2 = "7107597799709428413456141937460470149011183145188544168453129168495306617"

print(Solution().multiply(s1, s2))

# Time limit exceeded
class Solution:
	def convert(self, e):
		s2i = {
			'0': 0, 
			'1': 1, 
			'2': 2, 
			'3': 3, 
			'4': 4, 
			'5': 5, 
			'6': 6, 
			'7': 7, 
			'8': 8, 
			'9': 9
		}
		i2s = {
			0: '0', 
			1: '1', 
			2: '2', 
			3: '3', 
			4: '4', 
			5: '5', 
			6: '6', 
			7: '7', 
			8: '8', 
			9: '9'
		}
		if type(e) == int:
			return i2s[e]
		elif type(e) == str:
			return s2i[e]
	def addition(self, num1, num2):
		l1 = len(num1)
		l2 = len(num2)
		l = l1
		if l1 > l2:
			num2 = '0' * (l1 - l2) + num2
			l = l1
		elif l1 < l2:
			num1 = '0' * (l2 - l1) + num1
			l = l2
		carry = 0
		ans = ""
		for i in range(l - 1, -1, -1):
			ans = self.convert((self.convert(num1[i]) + self.convert(num2[i]) + carry) % 10) + ans
			carry = (self.convert(num1[i]) + self.convert(num2[i]) + carry) // 10
		if carry >= 1:
			ans = self.convert(carry) + ans
		return ans
	def multiply(self, num1, num2):
		"""
		:type num1: str
		:type num2: str
		:rtype: str
		"""
		# for i in range(len(num2)):
		# 	print(integer[num2[len(num2) - 1 - i]])
		ans = ""
		for i in range(len(num2) - 1, -1, -1):
			curr = ""
			carry = 0
			for j in range(len(num1) - 1, -1, -1):
				curr = self.convert((self.convert(num1[j]) * self.convert(num2[i]) + carry) % 10) + curr
				carry = (self.convert(num1[j]) * self.convert(num2[i]) + carry) // 10
			if carry >= 1:
				curr = self.convert(carry) + curr
			curr += '0' * (len(num2) - i - 1)
			ans = self.addition(ans, curr)
		if ans.replace('0', '') == "":
			return '0'
		return ans