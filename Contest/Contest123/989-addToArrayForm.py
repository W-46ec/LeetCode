class Solution:
	def addToArrayForm(self, A: 'List[int]', K: 'int') -> 'List[int]':
		return [int(j) for j in list(str(int("".join([str(i) for i in A])) + K))]
		

print(Solution().addToArrayForm([9, 9, 9], 1))