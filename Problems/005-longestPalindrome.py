class Solution:
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		start, end = 0, 0
		for i, char in enumerate(s):
			l1 = self.expand(s, i, i)
			l2 = self.expand(s, i, i + 1)
			l = max(l1, l2)
			if l > end - start:
				start = i - (l - 1) // 2
				end = i + l // 2
		return s[start: end + 1]

	def expand(self, s, l, r):
		while l >= 0 and r < len(s) and s[l] == s[r]:
			l -= 1
			r += 1
		return r - l - 1

print(Solution().longestPalindrome('cbbd'))



# # Time limit exceeded
# class Solution:
# 	def longestPalindrome(self, s):
# 		"""
# 		:type s: str
# 		:rtype: str
# 		"""

# 		if len(s) == 0:
# 			return ""
# 		elif len(s) == 1:
# 			return s

# 		maxLenght = 1
# 		maxL = maxR = 0

# 		for i, char in enumerate(s):
# 			last = len(s)
# 			while s.rfind(char, 0, last) > i:
# 				if self.isPalindrome(s[i: s.rfind(char, 0, last) + 1]):
# 					if (s.rfind(char, 0, last) - i + 1) > maxLenght:
# 						maxL = i
# 						maxR = s.rfind(char, 0, last)
# 						maxLenght = s.rfind(char, 0, last) - i + 1
# 					break
# 				else:
# 					last -= 1
# 			if maxLenght == len(s):
# 				break

# 		return s[maxL: maxR + 1]

# 	def isPalindrome(self, s):
# 		l, r = 0, len(s) - 1
# 		while l < r:
# 			if s[l] != s[r]:
# 				return False
# 			l += 1
# 			r -= 1
# 		return True