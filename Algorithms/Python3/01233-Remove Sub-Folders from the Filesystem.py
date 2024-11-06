
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
        return len(folder1) < len(folder2) and folder2[len(folder1)] == '/' and folder1 == folder2[ : len(folder1)]

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder = sorted(folder)
        ans = [folder[0]]
        for i in range(1, len(folder)):
            if not self.isSubfolder(ans[-1], folder[i]):
                ans += [folder[i]]
        return ans


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

    def testcase5(self):
        self.assertEqual(
            sorted(["/aaaa/aaab/aaac","/aaaa/aaab/acap","/aaaa/aaab/aebc/aebd/aebe/aebf/aebg","/aaaa/aaab/aebc/aebd/aebe/aebf/aebl/aebn","/aaaa/aaab/aebc/aebd/aebe/aebf/aebv/aeby","/aaaa/aaab/aebc/aebd/aebe/aeca/aecb/aecc","/aaaa/aaab/aebc/aebd/aebe/aeca/aecb/aecd","/aaaa/aaab/aebc/aebd/aebe/aeca/aecg","/aaaa/aaab/aebc/aebd/aebe/aeca/aecq/aecs","/aaaa/aaab/aebc/aebd/aebe/aecv","/aaaa/aaab/aebc/aebd/aebe/aedq","/aaaa/aaab/aebc/aebd/aeel/aeem/aeen","/aaaa/aaab/aebc/aebd/aeel/aeem/aees","/aaaa/aaab/aebc/aebd/aeel/aefh/aefi/aefk","/aaaa/aaab/aebc/aebd/aeel/aefh/aefi/aefm","/aaaa/aaab/aebc/aebd/aeel/aefh/aefn","/aaaa/aaab/aebc/aebd/aeel/aefh/aefs","/aaaa/aaab/aebc/aebd/aeel/aefh/aefx/aefy","/aaaa/aaab/aebc/aebd/aeel/aefh/aefx/aegb","/aaaa/aaab/aebc/aebd/aeel/aegc/aegd","/aaaa/aaab/aebc/aebd/aeel/aegc/aegi","/aaaa/aaab/aebc/aebd/aeel/aegc/aegn","/aaaa/aaab/aebc/aebd/aeel/aegc/aegs/aegw","/aaaa/aaab/aebc/aebd/aeel/aegx/aegy","/aaaa/aaab/aebc/aebd/aeel/aegx/aehi/aehj","/aaaa/aaab/aebc/aebd/aeel/aegx/aehi/aehk","/aaaa/aaab/aebc/aebd/aeel/aegx/aehi/aehl","/aaaa/aaab/aebc/aebd/aeel/aegx/aehn","/aaaa/aaab/aebc/aebd/aehs/aeht","/aaaa/aaab/aebc/aebd/aehs/aeio/aeip/aeiq","/aaaa/aaab/aebc/aebd/aehs/aeio/aeip/aeir","/aaaa/aaab/aebc/aebd/aehs/aeio/aeip/aeis","/aaaa/aaab/aebc/aebd/aehs/aeio/aeiu/aeiy","/aaaa/aaab/aebc/aebd/aehs/aeio/aeiz","/aaaa/aaab/aebc/aebd/aehs/aeio/aeje/aejf","/aaaa/aaab/aebc/aebd/aehs/aeio/aeje/aejg","/aaaa/aaab/aebc/aebd/aehs/aeio/aeje/aeji","/aaaa/aaab/aebc/aebd/aehs/aejj/aejk/aejl","/aaaa/aaab/aebc/aebd/aehs/aejj/aejk/aejm","/aaaa/aaab/aebc/aebd/aehs/aejj/aejk/aejn","/aaaa/aaab/aebc/aebd/aehs/aejj/aejk/aejo","/aaaa/aaab/aebc/aebd/aehs/aejj/aejp/aejr","/aaaa/aaab/aebc/aebd/aehs/aejj/aejp/aejt","/aaaa/aaab/aebc/aebd/aehs/aejj/aeju","/aaaa/aaab/aebc/aebd/aehs/aejj/aejz","/aaaa/aaab/aebc/aebd/aehs/aeke/aekf","/aaaa/aaab/aebc/aebd/aehs/aeke/aekk","/aaaa/aaab/aebc/aebd/aehs/aeke/aekp/aekq","/aaaa/aaab/aebc/aebd/aehs/aeke/aekp/aekr","/aaaa/aaab/aebc/aebd/aehs/aeke/aeku","/aaaa/aaab/aebc/aebd/aekz","/aaaa/aaab/aebc/aeog","/aaaa/aaab/aebc/afbj","/aaaa/aaab/aebc/afom","/aaaa/aaab/agbp/agbq/agbr/agbs/agbt/agbu","/aaaa/aaab/agbp/agbq/agbr/agbs/agby/agcb","/aaaa/aaab/agbp/agbq/agbr/agbs/agby/agcc","/aaaa/aaab/agbp/agbq/agbr/agbs/agcd/agcf","/aaaa/aaab/agbp/agbq/agbr/agbs/agci/agcm","/aaaa/aaab/agbp/agbq/agbr/agcn/agco","/aaaa/aaab/agbp/agbq/agbr/agcn/agct","/aaaa/aaab/agbp/agbq/agbr/agcn/agcy","/aaaa/aaab/agbp/agbq/agbr/agcn/agdd","/aaaa/aaab/agbp/agbq/agbr/agdi/agdj","/aaaa/aaab/agbp/agbq/agbr/agdi/agdo","/aaaa/aaab/agbp/agbq/agbr/agdi/agdy","/aaaa/aaab/agbp/agbq/agbr/aged/agee/agef","/aaaa/aaab/agbp/agbq/agbr/aged/agej","/aaaa/aaab/agbp/agbq/agbr/aged/ageo","/aaaa/aaab/agbp/agbq/agbr/aged/aget/ageu","/aaaa/aaab/agbp/agbq/agbr/aged/aget/agew","/aaaa/aaab/agbp/agbq/agbr/aged/aget/agex","/aaaa/aaab/agbp/agbq/agey","/aaaa/aaab/agbp/agbq/agif","/aaaa/aaab/agbp/agbq/aglm","/aaaa/aaab/agbp/agot","/aaaa/aaab/agbp/ahbw","/aaaa/aaab/agbp/ahoz","/aaaa/aicc","/aaaa/aqed/aqee/aqef","/aaaa/aqed/aqee/aqri","/aaaa/aqed/aqee/arel/arem/aren/areo/areq","/aaaa/aqed/aqee/arel/arem/aren/aret","/aaaa/aqed/aqee/arel/arem/aren/arey/arfa","/aaaa/aqed/aqee/arel/arem/aren/arfd","/aaaa/aqed/aqee/arel/arem/arfi/arfj","/aaaa/aqed/aqee/arel/arem/arfi/arfo/arfq","/aaaa/aqed/aqee/arel/arem/arfi/arfo/arfs","/aaaa/aqed/aqee/arel/arem/arfi/arft","/aaaa/aqed/aqee/arel/arem/arfi/arfy/argb","/aaaa/aqed/aqee/arel/arem/argd/arge","/aaaa/aqed/aqee/arel/arem/argd/argj/argl","/aaaa/aqed/aqee/arel/arem/argd/argo","/aaaa/aqed/aqee/arel/arem/argd/argt/argw","/aaaa/aqed/aqee/arel/arem/argy/argz","/aaaa/aqed/aqee/arel/arem/argy/arhe/arhf","/aaaa/aqed/aqee/arel/arem/argy/arhe/arhg","/aaaa/aqed/aqee/arel/arem/argy/arhj/arhn","/aaaa/aqed/aqee/arel/arem/argy/arho/arhs","/aaaa/aqed/aqee/arel/arht/arhu/arhv/arhw","/aaaa/aqed/aqee/arel/arht/arhu/arhv/arhz","/aaaa/aqed/aqee/arel/arht/arhu/aria","/aaaa/aqed/aqee/arel/arht/arhu/arif","/aaaa/aqed/aqee/arel/arht/arhu/arik","/aaaa/aqed/aqee/arel/arht/arip","/aaaa/aqed/aqee/arel/arht/arjk","/aaaa/aqed/aqee/arel/arht/arkf/arkg","/aaaa/aqed/aqee/arel/arht/arkf/arkl","/aaaa/aqed/aqee/arel/arht/arkf/arkq","/aaaa/aqed/aqee/arel/arht/arkf/arkv","/aaaa/aqed/aqee/arel/arla","/aaaa/aqed/aqee/arel/aroh/aroi","/aaaa/aqed/aqee/arel/aroh/arpd","/aaaa/aqed/aqee/arel/aroh/arpy/arpz","/aaaa/aqed/aqee/arel/aroh/arpy/arqe","/aaaa/aqed/aqee/arel/aroh/arpy/arqj/arql","/aaaa/aqed/aqee/arel/aroh/arpy/arqj/arqm","/aaaa/aqed/aqee/arel/aroh/arpy/arqj/arqn","/aaaa/aqed/aqee/arel/aroh/arpy/arqo","/aaaa/aqed/aqee/arel/aroh/arqt","/aaaa/aqed/aqee/arro/arrp/arrq/arrr/arrs","/aaaa/aqed/aqee/arro/arrp/arrq/arrw/arrz","/aaaa/aqed/aqee/arro/arrp/arrq/arsb/arsc","/aaaa/aqed/aqee/arro/arrp/arrq/arsb/arse","/aaaa/aqed/aqee/arro/arrp/arrq/arsg","/aaaa/aqed/aqee/arro/arrp/arsl/arsm/arsp","/aaaa/aqed/aqee/arro/arrp/arsl/arsr","/aaaa/aqed/aqee/arro/arrp/arsl/arsw","/aaaa/aqed/aqee/arro/arrp/arsl/artb/artc","/aaaa/aqed/aqee/arro/arrp/arsl/artb/arte","/aaaa/aqed/aqee/arro/arrp/arsl/artb/artf","/aaaa/aqed/aqee/arro/arrp/artg/arth","/aaaa/aqed/aqee/arro/arrp/artg/artm/artn","/aaaa/aqed/aqee/arro/arrp/artg/artm/arto","/aaaa/aqed/aqee/arro/arrp/artg/artm/artp","/aaaa/aqed/aqee/arro/arrp/artg/artr","/aaaa/aqed/aqee/arro/arrp/arub/aruc","/aaaa/aqed/aqee/arro/arrp/arub/aruh","/aaaa/aqed/aqee/arro/arrp/arub/arum","/aaaa/aqed/aqee/arro/arrp/arub/arur","/aaaa/aqed/aqee/arro/aruw","/aaaa/aqed/aqee/arro/aryd","/aaaa/aqed/aqee/arro/asbk","/aaaa/aqed/aser","/aaaa/aqed/aufe/auff","/aaaa/aqed/aufe/ausi","/aaaa/aqed/aufe/avfl","/aaaa/aqed/aufe/avso","/aaaa/aqed/awfr","/aaaa/ayge","/bgif","/cmqk","/dsyp/dsyq","/dsyp/ebar","/dsyp/ejcs","/dsyp/eret/ereu","/dsyp/eret/etfh","/dsyp/eret/evfu/evfv","/dsyp/eret/evfu/evsy/evsz","/dsyp/eret/evfu/evsy/evwg","/dsyp/eret/evfu/evsy/evzn/evzo/evzp","/dsyp/eret/evfu/evsy/evzn/evzo/evzu","/dsyp/eret/evfu/evsy/evzn/evzo/evzz","/dsyp/eret/evfu/evsy/evzn/evzo/ewae","/dsyp/eret/evfu/evsy/evzn/ewaj/ewak","/dsyp/eret/evfu/evsy/evzn/ewaj/ewap","/dsyp/eret/evfu/evsy/evzn/ewaj/ewau/eway","/dsyp/eret/evfu/evsy/evzn/ewaj/ewaz/ewbb","/dsyp/eret/evfu/evsy/evzn/ewaj/ewaz/ewbd","/dsyp/eret/evfu/evsy/evzn/ewbe/ewbf","/dsyp/eret/evfu/evsy/evzn/ewbe/ewbk/ewbl","/dsyp/eret/evfu/evsy/evzn/ewbe/ewbk/ewbo","/dsyp/eret/evfu/evsy/evzn/ewbe/ewbp","/dsyp/eret/evfu/evsy/evzn/ewbe/ewbu/ewbv","/dsyp/eret/evfu/evsy/evzn/ewbe/ewbu/ewby","/dsyp/eret/evfu/evsy/evzn/ewbz","/dsyp/eret/evfu/evsy/ewcu","/dsyp/eret/evfu/ewgb/ewgc","/dsyp/eret/evfu/ewgb/ewjj","/dsyp/eret/evfu/ewgb/ewmq/ewmr","/dsyp/eret/evfu/ewgb/ewmq/ewnm","/dsyp/eret/evfu/ewgb/ewmq/ewoh","/dsyp/eret/evfu/ewgb/ewmq/ewpc","/dsyp/eret/evfu/ewgb/ewpx/ewpy","/dsyp/eret/evfu/ewgb/ewpx/ewqt","/dsyp/eret/evfu/ewgb/ewpx/ewro","/dsyp/eret/evfu/ewgb/ewpx/ewsj","/dsyp/eret/evfu/ewte/ewtf/ewtg/ewth/ewtj","/dsyp/eret/evfu/ewte/ewtf/ewtg/ewth/ewtl","/dsyp/eret/evfu/ewte/ewtf/ewtg/ewtm/ewtn","/dsyp/eret/evfu/ewte/ewtf/ewtg/ewtm/ewto","/dsyp/eret/evfu/ewte/ewtf/ewtg/ewtm/ewtp","/dsyp/eret/evfu/ewte/ewtf/ewtg/ewtr/ewtt","/dsyp/eret/evfu/ewte/ewtf/ewtg/ewtr/ewtu","/dsyp/eret/evfu/ewte/ewtf/ewtg/ewtw","/dsyp/eret/evfu/ewte/ewtf/ewub","/dsyp/eret/evfu/ewte/ewtf/ewuw","/dsyp/eret/evfu/ewte/ewtf/ewvr","/dsyp/eret/evfu/ewte/ewwm","/dsyp/eret/evfu/ewte/ewzt/ewzu/ewzv/ewzw","/dsyp/eret/evfu/ewte/ewzt/ewzu/exaa/exab","/dsyp/eret/evfu/ewte/ewzt/ewzu/exaa/exad","/dsyp/eret/evfu/ewte/ewzt/ewzu/exaf","/dsyp/eret/evfu/ewte/ewzt/ewzu/exak","/dsyp/eret/evfu/ewte/ewzt/exap","/dsyp/eret/evfu/ewte/ewzt/exbk","/dsyp/eret/evfu/ewte/ewzt/excf","/dsyp/eret/evfu/ewte/exda/exdb/exdc/exdd","/dsyp/eret/evfu/ewte/exda/exdb/exdh/exdl","/dsyp/eret/evfu/ewte/exda/exdb/exdm","/dsyp/eret/evfu/ewte/exda/exdb/exdr","/dsyp/eret/evfu/ewte/exda/exdw","/dsyp/eret/evfu/ewte/exda/exer/exes/exet","/dsyp/eret/evfu/ewte/exda/exer/exes/exev","/dsyp/eret/evfu/ewte/exda/exer/exes/exew","/dsyp/eret/evfu/ewte/exda/exer/exex/exey","/dsyp/eret/evfu/ewte/exda/exer/exfc","/dsyp/eret/evfu/ewte/exda/exer/exfh","/dsyp/eret/evfu/ewte/exda/exfm","/dsyp/eret/exgh"])
        )


if __name__ == '__main__':
    unittest.main()