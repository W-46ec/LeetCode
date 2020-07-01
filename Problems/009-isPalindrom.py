def isPalindrome(x):
	"""
	:type x: int
	:rtype: bool
	"""

	if x < 0:
		return False
	elif x == 0:
		return True

	l = list(str(x))
	l.reverse()

	if "".join(l) == str(x):
		return True
	else:
		return False
	

print(isPalindrome(12321))