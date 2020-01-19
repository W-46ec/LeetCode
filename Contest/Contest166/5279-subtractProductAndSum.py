
class Solution:
	def subtractProductAndSum(self, n: int) -> int:
		digit = [int(i) for i in str(n)]
		product = 1
		for i in range(len(digit)):
			product *= digit[i]
		return product - sum(digit)

print(Solution().subtractProductAndSum(234))
print(Solution().subtractProductAndSum(4421))
