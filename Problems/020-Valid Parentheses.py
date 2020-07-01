def isValid(s):
	"""
	:type s: str
	:rtype: bool
	"""

	lParenthese = []

	parentheseTabel = {
		'(': ')', 
		'[': ']', 
		'{': '}'
	}

	if len(s) == 0:
		return True

	for i in range(0, len(s)):
		if s[i] in "([{":
			lParenthese.append(s[i])
		elif s[i] in ")]}":
			if len(lParenthese) == 0:
				return False
			if parentheseTabel[lParenthese.pop(len(lParenthese) - 1)] != s[i]:
				return False
	if len(lParenthese) != 0:
		return False

	return True

print(isValid("["))