
"""
# Remove Sub-Folders from the Filesystem

Given a list of folders `folder`, return *the folders after removing all **sub-folders** in those folders*. You may return the answer in **any order**.

If a `folder[i]` is located within another `folder[j]`, it is called a **sub-folder** of it. A sub-folder of `folder[j]` must start with `folder[j]`, followed by a `"/"`. For example, `"/a/b"` is a sub-folder of `"/a"`, but `"/b"` is not a sub-folder of `"/a/b/c"`.

The format of a path is one or more concatenated strings of the form: `'/'` followed by one or more lowercase English letters.

- For example, `"/leetcode"` and `"/leetcode/problems"` are valid paths while an empty string and `"/"` are not.


**Example 1:** 
```
Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
Output: ["/a","/c/d","/c/f"]
Explanation: Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.
```

**Example 2:** 
```
Input: folder = ["/a","/a/b/c","/a/b/d"]
Output: ["/a"]
Explanation: Folders "/a/b/c" and "/a/b/d" will be removed because they are subfolders of "/a".
```

**Example 3:** 
```
Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
Output: ["/a/b/c","/a/b/ca","/a/b/d"]
```

**Constraints:** 
    - `1 <= folder.length <= 4 * 10^4` 
    - `2 <= folder[i].length <= 100` 
    - `folder[i]` contains only lowercase letters and `'/'`.
    - `folder[i]` always starts with the character `'/'`.
    - Each folder name is **unique**.
"""

import unittest
from typing import List

class Solution:
    def isSubfolder(self, folder1: str, folder2: str) -> bool:
        """
        Return True if folder2 is a sub-folder of folder1
        """
        dirs1 = folder1.split('/')[1 : ]
        dirs2 = folder2.split('/')[1 : ]
        return len(dirs1) < len(dirs2) and all([dirs1[i] == dirs2[i] for i in range(len(dirs1))])

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder = sorted(folder)
        i = 0
        while i < len(folder) - 1:
            if self.isSubfolder(folder[i], folder[i + 1]):
                folder.pop(i + 1)
            else:
                i += 1
        return folder


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(
            sorted(self.soln_obj.removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"])), 
            sorted(["/a", "/c/d", "/c/f"])
        )

    def testcase2(self):
        self.assertEqual(
            sorted(self.soln_obj.removeSubfolders(["/a", "/a/b/c", "/a/b/d"])), 
            sorted(["/a"])
        )

    def testcase3(self):
        self.assertEqual(
            sorted(self.soln_obj.removeSubfolders(["/a/b/c", "/a/b/ca", "/a/b/d"])), 
            sorted(["/a/b/c", "/a/b/ca", "/a/b/d"])
        )

    def testcase4(self):
        self.assertEqual(
            sorted(self.soln_obj.removeSubfolders(["/a", "/a/b", "/a/b/c/d"])), 
            sorted(["/a"])
        )


if __name__ == '__main__':
    unittest.main()
