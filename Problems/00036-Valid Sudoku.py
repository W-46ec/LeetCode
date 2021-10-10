class Solution:
	def isValidSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: bool
		"""
		rows = []
		subBoxes = {
			0: "", 
			1: "", 
			2: "", 
			3: "", 
			4: "", 
			5: "", 
			6: "", 
			7: "", 
			8: ""
		}
		for i in board:
			s = "".join(i).replace('.', '')
			rows.append(s)
		for j in range(9):
			column = ""
			for i in range(9):
				if board[i][j].isdigit():
					if rows[i].count(board[i][j]) > 1:
						return False
					if board[i][j] in column:
						return False
					else:
						column += board[i][j]
					if board[i][j] in subBoxes[(i // 3) * 3 + (j // 3)]:
						return False
					else:
						subBoxes[(i // 3) * 3 + (j // 3)] += board[i][j]
		return True

# def isValidSudoku(board):
# 	"""
# 	:type board: List[List[str]]
# 	:rtype: bool
# 	"""
# 	subBox = dict()

# 	for i in board:
# 		s = "".join(i).replace('.', '')
# 		if len(s) != len(set(s)):
# 			return False

# 	for j in range(9):
# 		column = []
# 		if j % 3 == 0:
# 			subBox = {
# 				0: [], 
# 				1: [], 
# 				2: []
# 			}
# 		for i in range(9):
# 			if board[i][j].isdigit():
# 				if board[i][j] in column:
# 					return False
# 				else:
# 					column.append(board[i][j])

# 				if board[i][j] in subBox[int(i / 3)]:
# 					return False
# 				else:
# 					subBox[int(i / 3)].append(board[i][j])
# 	return True


sudoku = [[".",".",".",".",".",".","5",".","."], 
			[".",".",".",".",".",".",".",".","."], 
			[".",".",".",".",".",".",".",".","."], 
			["9","3",".",".","2",".","4",".","."], 
			[".",".","7",".",".",".","3",".","."], 
			[".",".",".",".",".",".",".",".","."], 
			[".",".",".","3","4",".",".",".","."], 
			[".",".",".",".",".","3",".",".","."], 
			[".",".",".",".",".","5","2",".","."]]

sudoku = [[".","8","7","6","5","4","3","2","1"], 
			["2",".",".",".",".",".",".",".","."], 
			["3",".",".",".",".",".",".",".","."], 
			["4",".",".",".",".",".",".",".","."], 
			["5",".",".",".",".",".",".",".","."], 
			["6",".",".",".",".",".",".",".","."], 
			["7",".",".",".",".",".",".",".","."], 
			["8",".",".",".",".",".",".",".","."], 
			["9",".",".",".",".",".",".",".","."]]

print(Solution().isValidSudoku(sudoku))