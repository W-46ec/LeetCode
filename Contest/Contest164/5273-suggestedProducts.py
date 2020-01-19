
from typing import List

class Solution:
	def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
		products = sorted(products)
		ans = []
		for i in range(len(searchWord)):
			typed = searchWord[ : i + 1]
			selected = []
			for word in products:
				if word[ : i + 1] == typed:
					if len(selected) < 3:
						selected.append(word)
					else:
						break
			ans.append(selected)
		return ans

print(Solution().suggestedProducts(
	["mobile","mouse","moneypot","monitor","mousepad"], 
	"mouse"
))

print(Solution().suggestedProducts(
	["havana"], 
	"havana"
))

print(Solution().suggestedProducts(
	["bags","baggage","banner","box","cloths"], 
	"bags"
))

print(Solution().suggestedProducts(
	["havana"], 
	"tatiana"
))