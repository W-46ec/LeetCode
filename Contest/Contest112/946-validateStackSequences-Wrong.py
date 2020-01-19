class Solution:
	def validateStackSequences(self, pushed, popped):
		"""
		:type pushed: List[int]
		:type popped: List[int]
		:rtype: bool
		"""
		popIdx = [pushed.index(i) for i in popped]
		print(popIdx)
		if len(popIdx) == 0:
			return True
		currMaxIdx, currMinIdx = popIdx[0], popIdx[0]
		for i in range(len(popIdx) - 1):
			if popIdx[i + 1] > popIdx[i]:
				currMaxIdx = max(currMaxIdx, popIdx[i + 1])
			else:
				if currMinIdx != currMaxIdx:
					if popIdx[i + 1] < popIdx[i] - (currMaxIdx - currMinIdx + 1) - 1:
						return False
					else:
						currMinIdx = min(currMinIdx, popIdx[i + 1])
				else:
					if popIdx[i + 1] < popIdx[i] - (currMaxIdx - currMinIdx + 1):
						return False
					else:
						currMinIdx = min(currMinIdx, popIdx[i + 1])
		return True

print(Solution().validateStackSequences([1, 0, 2], [2, 1, 0]))
print(Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
print(Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
print(Solution().validateStackSequences([1, 2, 3, 4, 5], []))