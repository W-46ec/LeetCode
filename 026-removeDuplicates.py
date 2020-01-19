def removeDuplicates(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	if len(nums) <= 1:
		return len(nums)

	pivot = 0

	for i in range(1, len(nums)):
		if nums[pivot] != nums[i]:
			pivot += 1
			nums[pivot] = nums[i]
	return pivot + 1

print(removeDuplicates([0, 0, 1, 1, 2, 3]))