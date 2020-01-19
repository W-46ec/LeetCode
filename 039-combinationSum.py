class Solution:	
	def combinationSum(self, candidates, target):
		"""
		:type candidates: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		candidates = sorted(candidates)
		outcome = []

		def calculate(arr, candidates, target):
			if sum(arr) > target:
				return
			if sum(arr) == target:
				if sorted(arr) not in outcome:
					outcome.append(sorted(arr))
				return
			for i in candidates:
				if sum(arr) + i > target:
					break
				calculate(arr + [i], candidates, target)

		calculate([], candidates, target)
		return outcome

print(Solution().combinationSum([1, 2], 4))