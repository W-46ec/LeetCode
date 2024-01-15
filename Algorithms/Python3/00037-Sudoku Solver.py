class Solution:
	def next(self, board, pos):
		if board[pos[0]][pos[1]] == '.':
			return pos
		else:
			i, j, count = pos[0], pos[1], 1
			while board[i][j].isdigit():
				if count == 81:
					return False
				i += (j + 1) // 9
				i %= 9
				j = (j + 1) % 9
				count += 1
			return (i, j)

	def isValidSudoku(self, board, pos, val):
		if board[pos[0]][pos[1]].isdigit():
			return False
		if val in "".join(board[pos[0]]):
			return False
		if val in [board[j][pos[1]] for j in range(9)]:
			return False
		row, column = pos[0] - pos[0] % 3, pos[1] - pos[1] % 3
		for i in range(3):
			for j in range(3):
				if val == board[row + i][column + j]:
					return False
		return True

	def fill(self, board, pos):
		if pos == False:
			return True
		i, j = pos[0], pos[1]
		if board[i][j] == '.':
			for c in "123456789":
				if self.isValidSudoku(board, (i, j), c):
					board[i][j] = c
					if self.fill(board, self.next(board, (i, j))):
						return True
					else:
						board[i][j] = '.'
			return False

	def solveSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		pos = self.next(board, (0, 0))
		if pos != False:
			self.fill(board, pos)
		else:
			return
		
sudoku = [
			[".",".","9","7","4","8",".",".","."], 
			["7",".",".",".",".",".",".",".","."], 
			[".","2",".","1",".","9",".",".","."], 
			[".",".","7",".",".",".","2","4","."], 
			[".","6","4",".","1",".","5","9","."], 
			[".","9","8",".",".",".","3",".","."], 
			[".",".",".","8",".","3",".","2","."], 
			[".",".",".",".",".",".",".",".","6"], 
			[".",".",".","2","7","5","9",".","."]
		]

sudoku = [
			[".",".",".",".",".",".",".",".","."], 
			[".",".",".",".",".",".",".",".","."], 
			[".",".",".",".",".",".",".",".","."], 
			[".",".",".",".",".",".",".",".","."], 
			[".",".",".",".",".",".",".",".","."], 
			[".",".",".",".",".",".",".",".","."], 
			[".",".",".",".",".",".",".",".","."], 
			[".",".",".",".",".",".",".",".","."], 
			[".",".",".",".",".",".",".",".","."]
		]

Solution().solveSudoku(sudoku)
print(sudoku)