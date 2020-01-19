class Solution:
	def reorderLogFiles(self, logs):
		"""
		:type logs: List[str]
		:rtype: List[str]
		"""
		letter_logs = [i for i in logs if i.split(' ')[1].isalpha()]
		letter_logs = sorted(letter_logs, key = lambda e: " ".join(e.split(' ')[1:]))
		digit_logs = [i for i in logs if i.split(' ')[1].isdigit()]
		return letter_logs + digit_logs

print(Solution().reorderLogFiles(
	["j mo", "5 m w", "g 07", "o 2 0", "t q h"]
))