class Solution:
	def exist(self, board, word):
		"""
		:type board: List[List[str]]
		:type word: str
		:rtype: bool
		"""
		if len(board) == 0:
			return False

		counted_pos = []
		row, col = len(board), len(board[0])

		def search(word, prev_pos):
			if len(word) == 0:
				return True
			stat = True
			if prev_pos[0] > 0:
				if word[0] == board[prev_pos[0] - 1][prev_pos[1]] and \
					(prev_pos[0] - 1, prev_pos[1]) not in counted_pos:
					counted_pos.append((prev_pos[0] - 1, prev_pos[1]))
					if search(word[1:], (prev_pos[0] - 1, prev_pos[1])):
						return True
					else:
						counted_pos.pop(len(counted_pos) - 1)
			if prev_pos[0] < row - 1:
				if word[0] == board[prev_pos[0] + 1][prev_pos[1]] and \
					(prev_pos[0] + 1, prev_pos[1]) not in counted_pos:
					counted_pos.append((prev_pos[0] + 1, prev_pos[1]))
					if search(word[1:], (prev_pos[0] + 1, prev_pos[1])):
						return True
					else:
						counted_pos.pop(len(counted_pos) - 1)
			if prev_pos[1] > 0:
				if word[0] == board[prev_pos[0]][prev_pos[1] - 1] and \
					(prev_pos[0], prev_pos[1] - 1) not in counted_pos:
					counted_pos.append((prev_pos[0], prev_pos[1] - 1))
					if search(word[1:], (prev_pos[0], prev_pos[1] - 1)):
						return True
					else:
						counted_pos.pop(len(counted_pos) - 1)
			if prev_pos[1] < col - 1:
				if word[0] == board[prev_pos[0]][prev_pos[1] + 1] and \
					(prev_pos[0], prev_pos[1] + 1) not in counted_pos:
					counted_pos.append((prev_pos[0], prev_pos[1] + 1))
					if search(word[1:], (prev_pos[0], prev_pos[1] + 1)):
						return True
					else:
						counted_pos.pop(len(counted_pos) - 1)
			return False

		for i in range(row):
			idx = -1
			while word[0] in board[i][idx + 1:]:
				idx = board[i].index(word[0], idx + 1)
				curr_pos = (i, idx)
				counted_pos.append(curr_pos)
				if search(word[1:], curr_pos):
					return True
				else:
					counted_pos.pop(len(counted_pos) - 1)
		return False

board = [
	["C","A","A"], 
	["A","A","A"], 
	["B","C","D"]
]

print(Solution().exist(board, "AAB"))