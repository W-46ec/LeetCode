
"""
Group Anagrams

Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
- All inputs will be in lowercase.
- The order of your output does not matter.
"""

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for w in strs:
            key = "".join(sorted(w))
            if key in d:
                d[key].append(w)
            else:
                d[key] = [w]
        # return [d[key] for key in d]
        return d.values()

print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

