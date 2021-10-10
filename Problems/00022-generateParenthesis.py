class Solution:
	def generateParenthesis(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		arr = []
		def generate(s = '', l = 0, r = 0):
			if len(s) == 2 * n:
				arr.append(s)
			if l < n:
				generate(s + '(', l + 1, r)
			if r < l:
				generate(s + ')', l, r + 1)
		generate()
		return arr

print(Solution().generateParenthesis(4))