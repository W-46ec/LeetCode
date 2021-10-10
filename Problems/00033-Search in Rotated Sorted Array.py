def find(nums, target, left, right):
	if left == right:
		if nums[left] == target:
			return left
		else:
			return -1
	elif left == right - 1:
		if nums[left] == target:
			return left
		elif nums[right] == target:
			return right
		else:
			return -1
	if target < nums[(right - left) // 2 + left]:
		return find(nums, target, left, (right - left) // 2 - 1 + left)
	elif target > nums[(right - left) // 2 + left]:
		return find(nums, target, (right - left) // 2 + 1 + left, right)
	elif target == nums[(right - left) // 2 + left]:
		return left + (right - left) // 2

def search(nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: int
	"""
	length = len(nums)
	if length == 0:
		return -1
	# elif length == 1:
	# 	if nums[0] == target:
	# 		return 0
	# 	else:
	# 		return -1

	copy = []
	start = nums.index(min(nums))
	i = start
	while True:
		copy.append(nums[i])
		if i == (start - 1) % length:
			break
		i += 1
		i %= length

	l, r = 0, length - 1
	index = find(copy, target, l, r)
	if index == -1:
		return -1
	else:
		return (index + start) % length


# def search(nums, target):
# 	"""
# 	:type nums: List[int]
# 	:type target: int
# 	:rtype: int
# 	"""
# 	length = len(nums)
# 	if length == 0:
# 		return -1
# 	elif length == 1:
# 		if nums[0] == target:
# 			return 0
# 		else:
# 			return -1

# 	start = nums.index(min(nums))
# 	subLenght = length
# 	l, r = start, (start + length - 1) % length

# 	while (l + 1) % length != r:
# 		if target == nums[(subLenght // 2 + l) % length]:
# 			return (subLenght // 2 + l) % length
# 		elif nums[l] == target:
# 			return l
# 		elif nums[r] == target:
# 			return r
# 		elif target < nums[(subLenght // 2 + l) % length]:
# 			r = (subLenght // 2 + l) % length
# 			subLenght = subLenght // 2 + 1
# 		elif target > nums[(subLenght // 2 + l) % length]:
# 			l = (subLenght // 2 + l) % length
# 			if subLenght % 2 == 1:
# 				subLenght = subLenght // 2 + 1
# 			else:
# 				subLenght = subLenght // 2
# 	return -1

print(search([4,5,6,7,0,1,2], 6))