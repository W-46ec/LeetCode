
from typing import List

class Solution:
	def printVertically(self, s: str) -> List[str]:
		words = s.split(" ")
		ans = []
		for idx in range(max([len(j) for j in words])):
			l = [i[idx] if idx < len(i) else ' ' for i in words]
			ans.append("".join(l).rstrip())
		return ans

print(Solution().printVertically("HOW ARE YOU"))
print(Solution().printVertically("TO BE OR NOT TO BE"))
print(Solution().printVertically("CONTEST IS COMING"))
