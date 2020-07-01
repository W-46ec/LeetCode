def twoSum(nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: List[int]
	"""
	if len(nums) == 1:
		return [0]

	for i in range(0, len(nums) - 1):
		for j in range(i + 1, len(nums)):
			if nums[i] + nums[j] == target:
				return [i, j]

print(twoSum([22, 72, 82, 34, 1, 8], 9))