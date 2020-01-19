class Solution:
	def numTrees(self, n: int) -> int:
		results = {}
		def t(n):
			if n <= 1:
				if n not in results:
					results[n] = 1
				return 1
			if n in results:
				return results[n]

			tn = 0
			for i in range(n):
				if i not in results:
					results[i] = t(i)
				if (n - i - 1) not in results:
					results[n - i - 1] = t(n - i - 1)
				tn += results[i] * results[n - i - 1]
			results[n] = tn
			return tn
		return t(n)

for i in range(20):
	print(Solution().numTrees(i))

# print(Solution().numTrees(19))