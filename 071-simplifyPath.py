class Solution:
	def simplifyPath(self, path):
		"""
		:type path: str
		:rtype: str
		"""
		stack = []
		l = path.split('/')
		for i in l:
			if i == '' or i == '.':
				continue
			elif i == '..':
				if len(stack) > 0:
					stack.pop(len(stack) - 1)
			else:
				stack.append(i)
		return '/' + "/".join(stack)
		
print(Solution().simplifyPath("/a//b////c/d//././/.."))
print(Solution().simplifyPath("/home//foo"))