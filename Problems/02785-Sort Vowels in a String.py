
"""
# Sort Vowels in a String

Given a **0-indexed** string `s`, **permute** `s` to get a new string `t` such that:
    - All consonants remain in their original places. More formally, if there is an index `i` with `0 <= i < s.length` such that `s[i]` is a consonant, then `t[i] = s[i]`.
    - The vowels must be sorted in the **nondecreasing** order of their **ASCII** values. More formally, for pairs of indices `i`, `j` with `0 <= i < j < s.length` such that `s[i]` and `s[j]` are vowels, then `t[i]` must not have a higher ASCII value than `t[j]`.

Return *the resulting string*.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in lowercase or uppercase. Consonants comprise all letters that are not vowels.


**Example 1:** 
```
Input: s = "lEetcOde"
Output: "lEOtcede"
Explanation: 'E', 'O', and 'e' are the vowels in s; 'l', 't', 'c', and 'd' are all consonants. The vowels are sorted according to their ASCII values, and the consonants remain in the same places.
```

**Example 2:** 
```
Input: s = "lYmpH"
Output: "lYmpH"
Explanation: There are no vowels in s (all characters in s are consonants), so we return "lYmpH".
```

**Constraints:** 
    - `1 <= s.length <= 10^5` 
    - `s` consists only of letters of the English alphabet in **uppercase and lowercase**.
"""

import unittest
from random import randint, sample, choices

class Solution:
    def sortVowels(self, s: str) -> str:
        # Split s into characters
        t = list(s)

        # Record indices of all vowels in s
        vowel_idx = [i for i, c in enumerate(s) if c in "AEIOUaeiou"]

        # Extract all vowels in s and sort them in nondecreasing order
        vowels = sorted([c for c in s if c in "AEIOUaeiou"])

        # Replace each vowel in s by vowel in the sorted order
        for i in range(len(vowel_idx)):
            t[vowel_idx[i]] = vowels[i]

        # Merge characters into string and return
        return "".join(t)


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.sortVowels("lEetcOde"), "lEOtcede")

    def testcase2(self):
        self.assertEqual(self.soln_obj.sortVowels("lYmpH"), "lYmpH")

    def test_random(self):
        num_tests = 20
        for _ in range(num_tests):
            # consonants & vowels
            alphabet_vowels = "AEIOUaeiou"
            alphabet_consonants = "".join([chr(a) for a in range(65, 91)]) + "".join([chr(a) for a in range(97, 123)])
            for c in alphabet_vowels:
                alphabet_consonants = alphabet_consonants.replace(c, '')

            # Generate random strings
            length = randint(1, 10 ** 5)
            rand_char_lst = choices(alphabet_consonants, k = length)
            rand_vowel_indices = sorted(sample(range(length), k = randint(1, length)))
            rand_vowels = choices(alphabet_vowels, k = len(rand_vowel_indices))
            rand_vowels_sorted = sorted(rand_vowels)
            assert len(rand_vowel_indices) == len(rand_vowels) == len(rand_vowels_sorted)

            # Construct s
            for i in range(len(rand_vowel_indices)):
                rand_char_lst[rand_vowel_indices[i]] = rand_vowels[i]
            s = "".join(rand_char_lst)

            # Construct t
            for i in range(len(rand_vowel_indices)):
                rand_char_lst[rand_vowel_indices[i]] = rand_vowels_sorted[i]
            t = "".join(rand_char_lst)

            self.assertEqual(self.soln_obj.sortVowels(s), t)


if __name__ == '__main__':
    unittest.main()
