def searchInsert(nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: int
	"""
	for i in range(len(nums)):
		if target <= nums[i]:
			return i
	return len(nums)

	# # faster way
	# return len([i for i in nums if i < target])

print(searchInsert([1, 3, 5, 6], 7))