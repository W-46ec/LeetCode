class Solution:
	def adjust(self, words, s, maxWidth, last):
		string = ""
		spaces = maxWidth
		count = len(s)
		idx = 0
		for i in s:
			spaces -= len(words[i])
		isFirst = True
		if not last:
			while len(string) < maxWidth:
				if isFirst:
					string = words[s[count - idx - 1]] + string
					idx += 1
					isFirst = False
				else:
					if idx < count - 1:
						string = ' ' * (spaces // (count - idx)) + string
						spaces -= (spaces // (count - idx))
						string = words[s[count - idx - 1]] + string
						idx += 1
					elif idx == count - 1:
						string = ' ' * spaces + string
						string = words[s[count - idx - 1]] + string
					else:
						while len(string) < maxWidth:
						 	string += ' '
		else:
			while len(string) < maxWidth:
				if isFirst:
					string += words[s[idx]]
					idx += 1
					isFirst = False
				else:
					if idx <= count - 1:
						string += ' '
						string += words[s[idx]]
						idx += 1
					else:
						while len(string) < maxWidth:
						 	string += ' '
		return string
	def fullJustify(self, words, maxWidth):
		"""
		:type words: List[str]
		:type maxWidth: int
		:rtype: List[str]
		"""
		l = []
		idx = 0
		while idx < len(words):
			s = []
			first = True
			currentLen = 0
			while currentLen <= maxWidth:
				if first:
					s.append(idx)
					first = False
					currentLen += len(words[idx])
					idx += 1
				else:
					if idx < len(words):
						if currentLen + 1 + len(words[idx]) <= maxWidth:
							s.append(idx)
							currentLen += (1 + len(words[idx]))
							idx += 1
						else:
							l.append(self.adjust(words, s, maxWidth, False))
							break
					else:
						if len(s) > 0:
							l.append(self.adjust(words, s, maxWidth, True))
							break
		return l




print(
	Solution().fullJustify(
		["What", "must", "be", "acknowledgment", "shall", "be"], 
		16
	)
)