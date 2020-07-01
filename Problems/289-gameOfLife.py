class Solution:
	def getNumOfLiveNeighbors(self, board, pos):
		x, y = pos[0], pos[1]
		counter = 0
		if x - 1 >= 0 and y - 1 >= 0 and board[x - 1][y - 1] == 1:
			counter += 1
		if x - 1 >= 0 and board[x - 1][y] == 1:
			counter += 1
		if x - 1 >= 0 and y + 1 < len(board[0]) and board[x - 1][y + 1] == 1:
			counter += 1
		if y - 1 >= 0 and board[x][y - 1] == 1:
			counter += 1
		if y + 1 < len(board[0]) and board[x][y + 1] == 1:
			counter += 1
		if x + 1 < len(board) and y - 1 >= 0 and board[x + 1][y - 1] == 1:
			counter += 1
		if x + 1 < len(board) and board[x + 1][y] == 1:
			counter += 1
		if x + 1 < len(board) and y + 1 < len(board[0]) and board[x + 1][y + 1] == 1:
			counter += 1
		return counter
	def gameOfLife(self, board):
		"""
		:type board: List[List[int]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		queue = []
		for i in range(len(board)):
			for j in range(len(board[0])):
				num = self.getNumOfLiveNeighbors(board, (i, j))
				if (num < 2 or num > 3) and board[i][j] == 1:
					queue.append((i, j, 0))
				elif num == 3 and board[i][j] == 0:
					queue.append((i, j, 1))
		for pos in queue:
			board[pos[0]][pos[1]] = pos[2]


board = [
	[0,1,0],
	[0,0,1],
	[1,1,1],
	[0,0,0]
]
print(board)
Solution().gameOfLife(board)
print(board)