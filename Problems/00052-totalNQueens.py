class Solution:
	def isValid(self, m, pos, n):
		i, j = pos[0], pos[1]
		if m[i].count('Q') > 0:
			return False
		for row in range(n):
			if m[row][j] == 'Q':
				return False
		tmpR = i - 1
		tmpC = j - 1
		while tmpR >= 0 and tmpC >= 0:
			if m[tmpR][tmpC] == 'Q':
				return False
			tmpR -= 1
			tmpC -= 1
		tmpR = i + 1
		tmpC = j + 1
		while tmpR < n and tmpC < n:
			if m[tmpR][tmpC] == 'Q':
				return False
			tmpR += 1
			tmpC += 1
		tmpR = i - 1
		tmpC = j + 1
		while tmpR >= 0 and tmpC < n:
			if m[tmpR][tmpC] == 'Q':
				return False
			tmpR -= 1
			tmpC += 1
		tmpR = i + 1
		tmpC = j - 1
		while tmpR < n and tmpC >= 0:
			if m[tmpR][tmpC] == 'Q':
				return False
			tmpR += 1
			tmpC -= 1
		return True
	def solve(self, ans, m, pos, n):
		i, j = pos[0], pos[1]
		if m[i].count('Q') == 0:
			for k in range(n):
				if self.isValid(m, (i, k), n):
					row = '.' * k + 'Q' + '.' * (n - k - 1)
					m[i] = row
					if self.solve(ans, m, (i, k), n):
						ans.append("-".join(m))
					m[i] = '.' * n
			return False
		else:
			if i < n - 1:
				return self.solve(ans, m, (i + 1, 0), n)
			else:
				return True
	def totalNQueens(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		ans = []
		tmp = []
		m = []
		for i in range(n):
			m.append('.' * n)
		self.solve(tmp, m, (0, 0), n)
		for i in range(len(tmp)):
			ans.append(tmp[i].split('-'))
		return len(ans)

print(Solution().totalNQueens(5))