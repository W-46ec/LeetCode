
class CustomStack:

	def __init__(self, maxSize: int):
		self.maxSize = maxSize
		self.S = []
		

	def push(self, x: int) -> None:
		if len(self.S) < self.maxSize:
			self.S.append(x)
		

	def pop(self) -> int:
		if len(self.S) > 0:
			return self.S.pop(-1)
		else:
			return -1
		

	def increment(self, k: int, val: int) -> None:
		length = len(self.S)
		if length > k:
			self.S = [i + val for i in self.S[ : k]] + self.S[k : ]
		else:
			self.S = [i + val for i in self.S]
		


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

obj = CustomStack(10)
obj.push(1)
obj.push(2)
obj.push(3)
param_2 = obj.pop()
obj.increment(4, 10)
print(obj.S)
