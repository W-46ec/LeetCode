
"""
# Minimum Deletions to Make Character Frequencies Unique

A string `s` is called **good** if there are no two different characters in `s` that have the same **frequency**.

Given a string `s`, return *the **minimum** number of characters you need to delete to make `s` **good***.

The **frequency** of a character in a string is the number of times it appears in the string. For example, in the string `"aab"`, the **frequency of** `'a'` is `2`, while the frequency of `'b'` is `1`.


**Example 1:** 
```
Input: s = "aab"
Output: 0
Explanation: s is already good.
```

**Example 2:** 
```
Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
```

**Example 3:** 
```
Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).
```

**Constraints:** 
    - `1 <= s.length <= 10^5` 
    - `s` contains only lowercase English letters.
"""

from collections import Counter, defaultdict

class Solution:
    def minDeletions(self, s: str) -> int:
        # char_freq[c] <- Number of occurrences of character c in s
        char_freq = Counter(s)

        # freq_count[f] <- Number of different characters in char_freq
        # that are associated with frequency f.
        freq_count = defaultdict(int)
        for c in char_freq:
            freq_count[char_freq[c]] += 1

        # Scan from the max frequency to min frequency.
        freq_sorted = sorted(freq_count.keys(), reverse = True)
        num_deletion = 0
        for f in freq_sorted:
            # If any frequency f is associated with more than 1 character, find a frequency
            # (e.g., f_available) such that f_available is smaller than f and it is not 
            # associated with any other character.
            # Delete (f - f_available) copies of that character and mark the new 
            # frequency (f - f_available) as being associated with this character.
            # Repeat until f is only associated with 1 character.
            while freq_count[f] > 1:
                curr_available = f
                while curr_available > 0 and curr_available in freq_count:
                    curr_available -= 1
                if curr_available >= 1:
                    freq_count[curr_available] += 1
                num_deletion += f - curr_available
                freq_count[f] -= 1

        return num_deletion

# 0
print(Solution().minDeletions("abb"))

# 2
print(Solution().minDeletions("aaabbbcc"))

# 2
print(Solution().minDeletions("ceabaacb"))

# 5
print(Solution().minDeletions("aabbccdd"))

# 0
print(Solution().minDeletions("a"))

# 3
print(Solution().minDeletions("abbcccddd"))
