
from typing import List

class Solution:
	def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
		if len(list(filter(lambda x: x != -1, leftChild + rightChild))) != n - 1:
			return False
		inbound = [0] * n
		for i in range(n):
			if leftChild[i] != -1:
				inbound[leftChild[i]] += 1
			if rightChild[i] != -1:
				inbound[rightChild[i]] += 1
		if len(list(filter(lambda x: x > 1, inbound))) > 0:
			return False
		return True

print(Solution().validateBinaryTreeNodes(n = 4, leftChild = [1, -1, 3, -1], rightChild = [2, -1, -1, -1]))
print(Solution().validateBinaryTreeNodes(n = 4, leftChild = [1, -1, 3, -1], rightChild = [2, 3, -1, -1]))
print(Solution().validateBinaryTreeNodes(n = 2, leftChild = [1, 0], rightChild = [-1, -1]))
print(Solution().validateBinaryTreeNodes(n = 6, leftChild = [1, -1, -1, 4, -1, -1], rightChild = [2, -1, -1, 5, -1, -1]))
print(Solution().validateBinaryTreeNodes(n = 4, leftChild = [1, -1, 3, -1], rightChild = [-1, 3, -1, -1]))
