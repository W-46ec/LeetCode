
"""
# Split Linked List in Parts

Given the `head` of a singly linked list and an integer `k`, split the linked list into `k` consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return *an array of the `k` parts*.


**Example 1:** 
![725_split1-lc](./img/725_split1-lc)
```
Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].
```

**Example 2:** 
![725_split2-lc](./img/725_split2-lc)
```
Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
```

**Constraints:** 
    - The number of nodes in the list is in the range `[0, 1000]`.
    - `0 <= Node.val <= 1000` 
    - `1 <= k <= 50` 
"""

import sys
sys.path += ['.', '../', '../../']

from util import ListNode, serializeList, deserializeList
from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Find out the total length of the linked-list
        total_length, curr = 0, head
        while curr:
            total_length, curr = total_length + 1, curr.next

        # Find out how long each part should be
        parts_length = [total_length // k] * k
        for i in range(total_length - k * (total_length // k)):
            parts_length[i] += 1

        # Split the linked-list
        parts, curr = [], head
        for l in parts_length:
            prev, curr_head = ListNode(-1, curr), curr
            for i in range(l):
                prev, curr = curr, curr.next
            prev.next = None
            parts += [curr_head]
        return parts

# [[1, 2, 3]]
print(list(map(lambda x: eval(serializeList(x)), Solution().splitListToParts(deserializeList("[1, 2, 3]"), 1))))

# [[1, 2], [3]]
print(list(map(lambda x: eval(serializeList(x)), Solution().splitListToParts(deserializeList("[1, 2, 3]"), 2))))

# [[1], [2], [3]]
print(list(map(lambda x: eval(serializeList(x)), Solution().splitListToParts(deserializeList("[1, 2, 3]"), 3))))

# [[1], [2], [3], []]
print(list(map(lambda x: eval(serializeList(x)), Solution().splitListToParts(deserializeList("[1, 2, 3]"), 4))))

# [[1], [2], [3], [], []]
print(list(map(lambda x: eval(serializeList(x)), Solution().splitListToParts(deserializeList("[1, 2, 3]"), 5))))

# [[1], [2], [3], [], [], []]
print(list(map(lambda x: eval(serializeList(x)), Solution().splitListToParts(deserializeList("[1, 2, 3]"), 6))))

# [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
print(list(map(lambda x: eval(serializeList(x)), Solution().splitListToParts(deserializeList("[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"), 3))))
