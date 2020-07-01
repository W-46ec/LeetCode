class Solution:
	def combinationSum2(self, candidates, target):
		"""
		:type candidates: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		if len(candidates) == 0:
			return []
		ans = []
		candidates = sorted(candidates)

		def calculate(idxArr, candidates, target):
			arr = sorted([candidates[i] for i in idxArr])
			if sum(arr) > target:
				return
			if sum(arr) == target:
				idxArr = sorted(idxArr)
				if arr not in ans:
					ans.append(arr)
				return
			for i in range(len(candidates)):
				if i not in idxArr:
					if sum(arr) + candidates[i] > target:
						break
					calculate(idxArr + [i], candidates, target)

		calculate([], candidates, target)
		return ans

print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))