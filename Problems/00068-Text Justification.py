
"""
# Text Justification

Given an array of strings `words` and a width `maxWidth`, format the text such that each line has exactly `maxWidth` characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces `' '` when necessary so that each line has exactly `maxWidth` characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

**Note:** 
    - A word is defined as a character sequence consisting of non-space characters only.
    - Each word's length is guaranteed to be greater than `0` and not exceed `maxWidth`.
    - The input array `words` contains at least one word.


**Example 1:** 
```
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
```

**Example 2:** 
```
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
```

**Example 3:** 
```
Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
```

**Constraints:** 
    - `1 <= words.length <= 300` 
    - `1 <= words[i].length <= 20` 
    - `words[i]` consists of only English letters and symbols.
    - `1 <= maxWidth <= 100` 
    - `words[i].length <= maxWidth` 
"""

from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines, buffer, buffer_len = [], [], 0
        for idx, w in enumerate(words):
            # If w is the first word of the current line, add w to buffer directly.
            # If w is not the first word, we need to make sure that w and at least 
            # one space in front of w can fit into the current buffer.
            if buffer_len == 0 or buffer_len + len(w) + 1 <= maxWidth:
                buffer += [w]
                buffer_len += len(w) if buffer_len == 0 else len(w) + 1
            else:   # Buffer is full
                # Total number of spaces
                total_space_len = maxWidth - sum(map(len, buffer))

                # Total number of gaps between the words
                # Note that if there is only one word, num_gaps is also 1.
                num_gaps = max(len(buffer) - 1, 1)

                # Distribute spaces evenly
                spaces = [' ' * (total_space_len // num_gaps) for _ in range(num_gaps)]
                # If the number of spaces on a line does not divide evenly between words, 
                # the empty slots on the left will be assigned more spaces than the slots on the right.
                for i in range(total_space_len - num_gaps * (total_space_len // num_gaps)):
                    spaces[i] += ' '

                # Add gaps between words and add the line to 'lines'.
                line = ''
                for i in range(len(buffer)):
                    line += buffer[i]
                    line += spaces[i] if i < len(spaces) else ''
                lines += [line]

                # Add current word to a new buffer
                buffer, buffer_len = [w], len(w)

            # If all words have been processed, add the last line to 'lines'.
            if idx == len(words) - 1:
                line = ' '.join(buffer)
                line += ' ' * (maxWidth - len(line))
                lines += [line]
        return lines

# ['This    is    an', 'example  of text', 'justification.  ']
print(Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))

# ['What   must   be', 'acknowledgment  ', 'shall be        ']
print(Solution().fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16))

# ['Science  is  what we', 'understand      well', 'enough to explain to', 'a  computer.  Art is', 'everything  else  we', 'do                  ']
print(Solution().fullJustify(["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20))

# ['Science  is  what we', 'understand      well', 'enough to explain to', 'a  computer.  Art is', 'everything  else  we', 'do !!!              ']
print(Solution().fullJustify(["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do", "!!!"], 20))

# ['Listen', 'to    ', 'many, ', 'speak ', 'to   a', 'few.  ']
print(Solution().fullJustify(["Listen", "to", "many,", "speak", "to", "a", "few."], 6))
