
"""
# Find First Palindromic String in the Array

Given an array of strings `words`, return *the first **palindromic** string in the array*. If there is no such string, return *an **empty string** `""`*.

A string is **palindromic** if it reads the same forward and backward.


**Example 1:** 
```
Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.
```

**Example 2:** 
```
Input: words = ["notapalindrome","racecar"]
Output: "racecar"
Explanation: The first and only string that is palindromic is "racecar".
```

**Example 3:** 
```
Input: words = ["def","ghi"]
Output: ""
Explanation: There are no palindromic strings, so the empty string is returned.
```

**Constraints:** 
    - `1 <= words.length <= 100` 
    - `1 <= words[i].length <= 100` 
    - `words[i]` consists only of lowercase English letters.
"""

import unittest
from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            if w == w[::-1]:
                return w
        return ""


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.firstPalindrome(["abc", "car", "ada", "racecar", "cool"]), "ada")

    def testcase2(self):
        self.assertEqual(self.soln_obj.firstPalindrome(["notapalindrome", "racecar"]), "racecar")

    def testcase3(self):
        self.assertEqual(self.soln_obj.firstPalindrome(["def", "ghi"]), "")

    def testcase4(self):
        self.assertEqual(self.soln_obj.firstPalindrome(["xngla", "e", "itrn", "y", "s", "pfp", "rfd"]), "e")

    def testcase5(self):
        self.assertEqual(self.soln_obj.firstPalindrome(['umicrszeaswtfmctwvoogehszwdjrwdcgyxxetbzevxrqphubyqbgpfetguyv', 'vzdzfwyevkvqhmvqssnvpayihawydzcovzmh', 'drvqqepesvornphmikbimxennygxisdysssmxjmaaecaqiwdgfxitoopigxauoojsebjmbcrymvpnnfomlkg', 'vvszfvtykdyfiywxgxmjpcawzdaovbujmexggwczovhspkrdsskxzrpgfaspnbncdspktcyfkkshpyojwwlysizd', 'epdtgfhgninnwqzztwm', 'dmhynaogcxyaxsghzjwzyqfuwyinstxoqcdkxeobinpqeplw', 'ruhxgdrzfyqyqmxclfqosyczqapiizxlzgixdxthhrv', 'dwcblqnxtrwtqmtqenidhxnifdbmdvobwmcvwjxgbyjzgvrqzlskjbfirauguhyyjhlotuckssrkqzppzbqd', 'gxdq', 'paesyowqeguvxozbixjqppeagycjx', 'glstauwugkidegnllapgzbzchckepmhbameuigsiqywbilwolxuwzzjwzouqknhlkbjzejxtponmkqjlojurxnryxyqy', 'inyhioiwanafuhsprudtkqztoakxhbmqcmibsxlhycbmqrvtfabsncmiymthcxwkwkq', 'djknenppuleedpptrfjgqfejcoghnxjlvjalxkyvnujgiiwdbtvgqvgsivkzqcrbfcvooyhqmrlacyiozytmampjwpknrj', 'zzrpjoogwkdmdxdkdwgwugqtmzryrgtelnvydyqewpdzzptqzvffppgnhhcaiqotmyslntlwjajzuzbawidpxjtyxryg', 'xmegifttkamzbpjqbghgwdrkvtnuwfmjdmwehdqiyvgpxxlbkcvkemjbmhbyeqyfssytuwaeysvgnidhcgpncxdxxzhrkbvyqfrs', 'wgljaiyhyfdijjgihseciabfcoqfojhswewpkpartzmaaglvdfifpptycyonigwcgyklapzojivgojcrevugspejmwanolg', 'oceurgzgvvctgydqexhghwcochhmtoxjugreqfdnsshffngchetrwedhinosdhwlgviohpkjowr', 'dyl', 'vjxkcihfmnmmz', 'aheg', 'dwsomlqmaqifihkwahvywzqamgominhxfsgrgbgvoiopnikhxonpetelfsguvhxgiujrij', 'pdrjgfqzyqczpwdsfzypgkmsvnpboutmcffqrwuzkchaufymmczrdwulbvbanungpxqk', 'eudbizaabgfzqytowifsuovmxmkjgajtliyfycbrkxeaarakapqoihawmdzmglfnglpwqnfd', 'txdclnfwxevu', 'kslqrafjshhadqszeljcekrpnpxqgppbnadmzmpufvadcghxqdqmafpbnutifigstxyilmgx', 'yhhvhyoolv', 'sjtubggxcla', 'vydf']), "")


if __name__ == '__main__':
    unittest.main()

