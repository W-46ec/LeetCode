def searchRange(nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: List[int]
	"""
	l, r = 0, len(nums) - 1
	find = -1

	if l == r:
		if nums[l] == target:
			find = l

	while l < r:
		mid = (l + r) // 2
		if nums[mid] == target:
			find = mid
			break
		if nums[l] == target:
			find = l
			break
		if nums[r] == target:
			find = r
			break
		if target < nums[mid]:
			r = mid - 1
		else:
			l = mid + 1

	if find == -1:
		return [-1, -1]
	else:
		l = r = find

		while (l - 1 >= 0 and nums[l - 1] == nums[find]) or \
			(r + 1 <= len(nums) - 1 and nums[r + 1] == nums[find]):
			if l - 1 >= 0 and nums[l - 1] == nums[find]:
				l -= 1
			if r + 1 <= len(nums) - 1 and nums[r + 1] == nums[find]:
				r += 1
	return [l, r]

print(searchRange([2, 2], 2))