def findMedianSortedArrays(nums1, nums2):
	"""
	:type nums1: List[int]
	:type nums2: List[int]
	:rtype: float
	"""

	index = 0
	l = []

	if len(nums1) == 0 and len(nums2) == 0:
		return 0.0
	elif len(nums1) == 0:
		l = nums2
	elif len(nums2) == 0:
		l = nums1
	else:
		l = nums1
		i = 0
		while i < len(nums2):
			if index < len(l):
				if nums2[i] < l[index]:
					l.insert(index, nums2[i])
					i += 1
				else:
					index += 1
			else:
				l.insert(index, nums2[i])
				i += 1
				index += 1

	if len(l) % 2 == 0:
		return (l[int(len(l) / 2)] + l[int(len(l) / 2) - 1]) / 2
	else:
		return float(l[int(len(l) / 2)])

print(findMedianSortedArrays([1, 3], [2, 4]))