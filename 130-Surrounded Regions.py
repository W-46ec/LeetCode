class Solution:
	def solve(self, board: 'List[List[str]]') -> 'None':
		"""
		Do not return anything, modify board in-place instead.
		"""
		if len(board) == 0:
			return

		def setBorder(x, y):
			if x >= 0 and x < len(board) and y >= 0 and y < len(board[0]):
				if board[x][y] == 'O':
					board[x][y] = 'B'
					setBorder(x - 1, y)
					setBorder(x + 1, y)
					setBorder(x, y - 1)
					setBorder(x, y + 1)

		for i in range(len(board)):
			if board[i][0] == 'O':
				setBorder(i, 0)
			if board[i][len(board[0]) - 1] == 'O':
				setBorder(i, len(board[0]) - 1)

		for j in range(len(board[0])):
			if board[0][j] == 'O':
				setBorder(0, j)
			if board[len(board) - 1][j] == 'O':
				setBorder(len(board) - 1, j)

		for i in range(len(board)):
			for j in range(len(board[0])):
				board[i][j] = 'O' if board[i][j] == 'B' else 'X'

board = [
	["X","X","X","X"], 
	["X","O","O","X"], 
	["X","X","O","X"], 
	["X","O","X","X"]
]

board = [
	["X","O","X","O","X","O"], 
	["O","X","O","X","O","X"], 
	["X","O","X","O","X","O"], 
	["O","X","O","X","O","X"]
]

for i in board:
	print(i)
print('\n')

Solution().solve(board)

for i in board:
	print(i)
print('\n')