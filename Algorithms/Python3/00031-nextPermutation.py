class Solution:
	def nextPermutation(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		for i in range(len(nums) - 1, -1, -1):
			if i == 0:
				nums.reverse()
				return
			else:
				if nums[i] > nums[i - 1]:
					target = i - 1
					break

		# Make it ascending
		i, j = target + 1, len(nums) - 1
		while i < j:
			if nums[i] > nums[j]:
				nums[i], nums[j] = nums[j], nums[i]
			i, j = i + 1, j - 1

		# Find the first number which is bigger than nums[target]
		for i in range(target + 1, len(nums)):
			if nums[i] > nums[target]:
				nums[target], nums[i] = nums[i], nums[target]
				return

l = [2, 3, 1, 3, 3]
print(l)
Solution().nextPermutation(l)
print(l)


# # Time limit exceeded
# class Solution:
# 	def nextPermutation(self, nums):
# 		"""
# 		:type nums: List[int]
# 		:rtype: void Do not return anything, modify nums in-place instead.
# 		"""
# 		l = []
# 		def permutation(U, curr, targetLength):
# 			if len(curr) == targetLength and curr not in l:
# 				l.append(curr)
# 			elif len(curr) > targetLength:
# 				return
# 			else:
# 				for i in U:
# 					if curr.count(i) < U.count(i):
# 						permutation(U, curr + [i], targetLength)
# 		permutation(sorted(nums), [], len(nums))
# 		idx = (l.index(nums) + 1) % len(l)
# 		for i in range(len(nums)):
# 			nums[i] = l[idx][i]