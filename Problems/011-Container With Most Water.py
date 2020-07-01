def maxArea(height):
	"""
	:type height: List[int]
	:rtype: int
	"""

	# # Time limit exceeded
	# maxarea = 0
	# if len(height) == 1:
	# 	return maxarea
	# for i in range(0, len(height)):
	# 	for j in range(i + 1, len(height)):
	# 		s = min(height[i], height[j]) * (j - i)
	# 		if s > maxarea:
	# 			maxarea = s
	# return maxarea
	
	maxarea, l, r = 0, 0, len(height) - 1
	if r == 0:
		return maxarea
	while l < r:
		s = min(height[r], height[l]) * (r - l)
		if s > maxarea:
			maxarea = s
		if height[l] < height[r]:
			l += 1
		else:
			r -= 1
	return maxarea


print(maxArea([1, 1]))