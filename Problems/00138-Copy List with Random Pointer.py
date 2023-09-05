
"""
# Copy List with Random Pointer

A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`.

Construct a [deep copy](https://en.wikipedia.org/wiki/Object_copying#Deep_copy) of the list. The deep copy should consist of exactly `n` **brand new** nodes, where each new node has its value set to the value of its corresponding original node. Both the `next` and `random` pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. **None of the pointers in the new list should point to nodes in the original list**.

For example, if there are two nodes `X` and `Y` in the original list, where `X.random --> Y`, then for the corresponding two nodes `x` and `y` in the copied list, `x.random --> y`.

Return *the head of the copied linked list*.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of `[val, random_index]` where:
    - `val`: an integer representing `Node.val` 
    - `random_index`: the index of the node (range from `0` to `n-1`) that the `random` pointer points to, or `null` if it does not point to any node.

Your code will **only** be given the `head` of the original linked list.

**Example 1:** 
![138_e1](./img/138_e1.png)
```
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

**Example 2:** 
![138_e2](./img/138_e2.png)
```
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
```

**Example 3:** 
![138_e3](./img/138_e3.png)
```
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
```

**Constraints:** 
    - `0 <= n <= 1000` 
    - `-10^4 <= Node.val <= 10^4` 
    - `Node.random` is `null` or is pointing to some node in the linked list.
"""

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        prev, curr = Node(-1, head), head
        # Create a HashMap that maps nodes from 
        # the old list to nodes in the new list.
        mapping = { prev: Node(-1, head) }
        # Dummy head for the new list.
        dummy_new_head = mapping[prev]

        # Create nodes for the new list and link 
        # all the 'next' pointers correctly.
        while curr:
            mapping[curr] = Node(curr.val)
            mapping[prev].next = mapping[curr]
            prev, curr = curr, curr.next

        # Go through the old list again and link 
        # all the 'random' pointers in the new list correctly.
        curr = head
        while curr:
            if curr.random:
                mapping[curr].random = mapping[curr.random]
            curr = curr.next

        return dummy_new_head.next

