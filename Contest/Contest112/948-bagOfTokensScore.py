class Solution:
	def bagOfTokensScore(self, tokens, P):
		"""
		:type tokens: List[int]
		:type P: int
		:rtype: int
		"""
		points = 0
		tokens = sorted(tokens)
		while len(tokens) > 0:
			if points == 0 and P < tokens[0]:
				break
			while len(tokens) > 0 and P >= tokens[0]:
				points += 1
				P -= tokens[0]
				tokens.pop(0)
			if len(tokens) == 1:
				break
			if len(tokens) > 0 and points > 0:
				points -= 1
				P += tokens[len(tokens) - 1]
				tokens.pop(len(tokens) - 1)
		return points

print(Solution().bagOfTokensScore([39, 71, 27, 81], 85))