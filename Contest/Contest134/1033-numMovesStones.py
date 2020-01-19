class Solution:
	def numMovesStones(self, a: 'int', b: 'int', c: 'int') -> 'List[int]':
		stones = sorted([a, b, c])
		dist = [
			abs(stones[0] - stones[1]) - 1, 
			abs(stones[1] - stones[2]) - 1
		]
		if dist.count(0) == 1 or dist.count(1) != 0:
			return [1, sum(dist)]
		elif dist.count(0) == 0:
			return [2, sum(dist)]
		else:
			return [0, 0]

print(Solution().numMovesStones(1, 2, 5))
print(Solution().numMovesStones(4, 3, 2))
print(Solution().numMovesStones(1, 4, 8))
print(Solution().numMovesStones(3, 5, 1))
