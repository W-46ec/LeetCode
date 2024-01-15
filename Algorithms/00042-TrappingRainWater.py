class Solution:
	def trap(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		length = len(height)
		if length == 0:
			return 0
		ans, lptr, rptr = 0, 0, length - 1
		lmax, rmax = 0, 0
		while lptr < rptr:
			if height[lptr] < height[rptr]:
				if height[lptr] > lmax:
					lmax = height[lptr]
				else:
					ans += lmax - height[lptr]
				lptr += 1
			else:
				if height[rptr] > rmax:
					rmax = height[rptr]
				else:
					ans += rmax - height[rptr]
				rptr -= 1
		return ans

print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

# # Time limit exceeded
# class Solution:
# 	def trap(self, height):
# 		"""
# 		:type height: List[int]
# 		:rtype: int
# 		"""
# 		count = 0
# 		if len(height) == 0:
# 			return 0
# 		while sum(height) > 0:
# 			l = [i for i in height if i >= 0]
# 			while len(l) > 0 and l[0] == 0:
# 				l.pop(0)
# 			while len(l) > 0 and l[len(l) - 1] == 0:
# 				l.pop(len(l) - 1)
# 			count += l.count(0)
# 			for i in range(len(height)):
# 				if height[i] > 0:
# 					height[i] -= 1
# 		return count