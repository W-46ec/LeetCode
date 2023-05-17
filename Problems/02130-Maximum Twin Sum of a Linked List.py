
"""
# Maximum Twin Sum of a Linked List


In a linked list of size `n`, where `n` is even, the `ith` node (**0-indexed**) of the linked list is known as the **twin** of the `(n-1-i)th` node, if `0 <= i <= (n / 2) - 1`.

- For example, if `n = 4`, then node `0` is the twin of node `3`, and node `1` is the twin of node `2`. These are the only nodes with twins for `n = 4`.

The **twin sum** is defined as the sum of a node and its twin.

Given the `head` of a linked list with even length, return *the **maximum twin sum** of the linked list*.


**Example 1**:
![2130_eg1drawio](./img/2130_eg1drawio.png)
```
Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 
```

**Example 2**:
![2130_eg2drawio](./img/2130_eg2drawio.png)
```
Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 
```

**Example 3**:
![2130_eg3drawio](./img/2130_eg3drawio.png)
```
Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.
```

**Constraints**:
    - The number of nodes in the list is an even integer in the range `[2, 10^5]`.
    - `1 <= Node.val <= 10^5` 
"""

import sys
sys.path += ['.', '../', '../../']

from typing import Optional
from util import ListNode, initList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # # Store all elements in a list and calculate the max twin sum -- O(n) time & O(n) space
        # lst, curr = [], head
        # while curr:
        #     lst, curr = lst + [curr.val], curr.next
        # return max([lst[i] + lst[len(lst) - i - 1] for i in range(len(lst) // 2)])


        # Reverse the first half of the list and compute the max sum -- O(n) time & O(1) space

        # Maintain a fast pointer and a slow pointer where the fast pointer jumps
        # two node each iteration and the slow pointer jumps one node each iteration.
        # In the meanwhile, place the next node of `slow` to the front of the list
        # so that when `fast` reaches the end, exactly the first half of the original
        # list is reversed.
        slow, fast = head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            dummy_head = slow.next
            slow.next = slow.next.next
            dummy_head.next = head
            head = dummy_head

        # Iterate through the first half and the second half of the list 
        # using `head` and `slow` to compute the max sum.
        max_sum = float('-inf')
        while slow.next:
            max_sum = max(max_sum, head.val + slow.next.val)
            head, slow = head.next, slow.next
        return max_sum

# 6
print(Solution().pairSum(initList([5, 4, 2, 1])))

# 7
print(Solution().pairSum(initList([4, 2, 2, 3])))

# 100001
print(Solution().pairSum(initList([1, 100000])))
