
from typing import List

class Solution:
	def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
		words = [sorted(w) for w in words]
		letters = sorted(letters)
		all_sores = [0] * len(words)

		def computeScore(word):
			pass


