def threeSum(nums):
	"""
	:type nums: List[int]
	:rtype: List[List[int]]
	"""
	solutions = []
	nums.sort()
	length = len(nums)
	for i in range(length - 2):
		if i > 0 and nums[i] == nums[i - 1]:
			continue
		j, k = i + 1, length - 1
		while(j < k):
			s = nums[i] + nums[j] + nums[k]
			if s == 0:
				solutions.append([nums[i], nums[j], nums[k]])
				while j < k and nums[j] == nums[j + 1]:
					j += 1
				while j < k and nums[k] == nums[k - 1]:
					k -= 1
				j += 1
				k -= 1
			elif s < 0:
				j += 1
			elif s > 0:
				k -= 1
	return solutions

print(threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))

# # Time Limit Exceeded Version
# def threeSum(nums):
# 	"""
# 	:type nums: List[int]
# 	:rtype: List[List[int]]
# 	"""
# 	positive = []
# 	negative = []
# 	zero = []
# 	solutions = []
# 	hasZero = False

# 	if len(nums) == 0:
# 		return []

# 	for i in nums:
# 		if i > 0:
# 			positive.append(i)
# 		elif i < 0:
# 			negative.append(i)
# 		elif i == 0:
# 			hasZero = True
# 			zero.append(i)

# 	if len(zero) >= 3:
# 			solutions.append([0, 0, 0])
# 	if len(positive) == 0 or len(negative) == 0:
# 		return solutions

# 	if hasZero:
# 		for i in positive:
# 			for j in negative:
# 				if i + j == 0:
# 					if [j, 0, i] not in solutions:
# 						solutions.append([j, 0, i])

# 	for i in range(0, len(positive)):
# 		for j in range(i + 1, len(positive)):
# 			for k in range(0, len(negative)):
# 				if positive[i] + positive[j] + negative[k] == 0:
# 					if sorted([positive[i], positive[j], negative[k]]) not in solutions:
# 						solutions.append(sorted([positive[i], positive[j], negative[k]]))

# 	for i in range(0, len(negative)):
# 		for j in range(i + 1, len(negative)):
# 			for k in range(0, len(positive)):
# 				if negative[i] + negative[j] + positive[k] == 0:
# 					if sorted([negative[i], negative[j], positive[k]]) not in solutions:
# 						solutions.append(sorted([negative[i], negative[j], positive[k]]))

# 	return solutions