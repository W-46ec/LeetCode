
"""
# Assign Cookies

Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child `i` has a greed factor `g[i]`, which is the minimum size of a cookie that the child will be content with; and each cookie `j` has a size `s[j]`. If `s[j] >= g[i]`, we can assign the cookie `j` to the child `i`, and the child `i` will be content. Your goal is to maximize the number of your content children and output the maximum number.


**Example 1:** 
```
Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.
```

**Example 2:** 
```
Input: g = [1,2], s = [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.
```

**Constraints:** 
    - `1 <= g.length <= 3 * 10^4` 
    - `0 <= s.length <= 3 * 10^4` 
    - `1 <= g[i], s[j] <= 2^31 - 1` 
"""

import unittest
from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g, s = sorted(g), sorted(s)
        i, j, count = 0, 0, 0
        while i < len(g) and j < len(s):
            while j < len(s) and g[i] > s[j]:
                j = j + 1
            count += 1 if j < len(s) else 0
            i, j = i + 1, j + 1
        return count


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.findContentChildren([1, 2, 3], [1, 1]), 1)

    def testcase2(self):
        self.assertEqual(self.soln_obj.findContentChildren([1, 2], [1, 2, 3]), 2)

    def testcase3(self):
        self.assertEqual(self.soln_obj.findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]), 2)

    def testcase4(self):
        self.assertEqual(self.soln_obj.findContentChildren([1, 2, 3], [3]), 1)


if __name__ == '__main__':
    unittest.main()
