class Solution:
	def minFlipsMonoIncr(self, S):
		"""
		:type S: str
		:rtype: int
		"""
		if S.count('0') == 0 or S.count('1') == 0:
			return 0
		numOfHead0 = len(S) - len(str(int(S)))
		numOfTail1 = 0
		while S[len(S) - 1 - numOfTail1] == '1':
			numOfTail1 += 1
		numOf1 = S[numOfHead0 : len(S) - numOfTail1].count('1')
		numOf0 = S[numOfHead0 : len(S) - numOfTail1].count('0')
		print(numOfHead0, numOfTail1, numOf1, numOf0)
		return min(numOf1, numOf0)

print(Solution().minFlipsMonoIncr("10011111110010111011"))