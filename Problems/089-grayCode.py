class Solution:
	def xor(self, b1, b2):
		b1, b2 = int(b1), int(b2)
		if b1 == b2:
			return '0'
		else:
			return '1'
	def binToGray(self, b):
		b = '0' + b
		g = ''
		for i in range(len(b) - 1):
			g += self.xor(b[i], b[i + 1])
		return g
	def decToBin(self, dec, bitSize):
		b = ''
		for i in range(bitSize):
			if (dec != 0):
				b = str(dec % 2) + b
				dec = dec // 2
			else:
				l = len(b)
				for i in range(l, bitSize):
					b = '0' + b
		return b
	def BinToDec(self, b):
		l = len(b)
		n = 0
		for i in range(l):
			n += int(b[l - i - 1]) * (2 ** i)
		return n
	def grayCode(self, n):
		"""
		:type n: int
		:rtype: List[int]
		"""
		l = []
		if n == 0:
			return [0]
		for i in range(2 ** n):
			l.append(self.BinToDec(self.binToGray(self.decToBin(i, n))))
		return l

print(Solution().grayCode(3))

# # Another way
# class Solution:
# 	def grayCode(self, n):
# 		"""
# 		:type n: int
# 		:rtype: List[int]
# 		"""
# 		l = []
# 		for i in range(2 ** n):
# 			l.append(i ^ (i >> 1))
# 		return l