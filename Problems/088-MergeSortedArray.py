class Solution:
	def insert(self, nums1, m, idx, target):
		tmp = nums1[m]
		for i in range(m, idx, -1):
			nums1[i] = nums1[i - 1]
		nums1[idx] = target

	def merge(self, nums1, m, nums2, n):
		"""
		:type nums1: List[int]
		:type m: int
		:type nums2: List[int]
		:type n: int
		:rtype: void Do not return anything, modify nums1 in-place instead.
		"""
		if len(nums1) == 0 or len(nums2) == 0:
			return
		idx = 0
		i = 0
		while i < n:
			if nums2[i] <= nums1[idx]:
				self.insert(nums1, m, idx, nums2[i])
				m += 1
				i += 1
			elif idx >= m and nums1[idx] == 0:
				nums1[idx] = nums2[i]
				m += 1
				i += 1
			idx += 1


nums1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
nums2 = [1, 2, 2]
Solution().merge(nums1, 6, nums2, 3)
print(nums1)