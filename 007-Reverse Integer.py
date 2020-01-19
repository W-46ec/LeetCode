
def reverse(x):
	"""
	:type x: int
	:rtype: int
	"""

	sign = 1
	if x < 0:
		sign *= -1
		x *= sign
	elif x == 0:
		return 0

	l = list(str(x))
	l.reverse()

	while l[0] == '0':
		l.pop(0)
		
	x = int("".join(l)) * sign
	if x > 2 ** 31 - 1 or x < -(2 ** 31):
		return 0
	return x

print(reverse(1534236469))