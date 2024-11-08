
"""
# Add Two Numbers

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


**Example 1:** 
![002_addtwonumber1](./img/002_addtwonumber1.jpg)
```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

**Example 2:** 
```
Input: l1 = [0], l2 = [0]
Output: [0]
```

**Example 3:** 
```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

**Constraints:** 
    - The number of nodes in each linked list is in the range `[1, 100]`.
    - `0 <= Node.val <= 9` 
    - It is guaranteed that the list represents a number that does not have leading zeros.
"""

import unittest
from random import randint
from util import ListNode, serializeList, deserializeList

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val = 0, next = None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head, carry = ListNode(), 0
        curr_node = dummy_head
        while l1 or l2 or carry:
            d1, d2 = l1.val if l1 else 0, l2.val if l2 else 0
            curr_node.next = ListNode((d1 + d2 + carry) % 10)
            carry = (d1 + d2 + carry) // 10
            l1, l2 = l1.next if l1 else l1, l2.next if l2 else l2
            curr_node = curr_node.next
        return dummy_head.next


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        ans = serializeList(self.soln_obj.addTwoNumbers(deserializeList("[2, 4, 3]"), deserializeList("[5, 6, 4]")))
        self.assertEqual(ans, "[7, 0, 8]")

    def testcase2(self):
        ans = serializeList(self.soln_obj.addTwoNumbers(deserializeList("[0]"), deserializeList("[0]")))
        self.assertEqual(ans, "[0]")

    def testcase3(self):
        ans = serializeList(self.soln_obj.addTwoNumbers(deserializeList("[9, 9, 9, 9, 9, 9, 9]"), deserializeList("[9, 9, 9, 9]")))
        self.assertEqual(ans, "[8, 9, 9, 9, 0, 0, 0, 1]")

    def testcase4(self):
        ans = serializeList(self.soln_obj.addTwoNumbers(deserializeList("[5]"), deserializeList("[5]")))
        self.assertEqual(ans, "[0, 1]")

    def testcase5(self):
        ans = serializeList(self.soln_obj.addTwoNumbers(deserializeList("[1, 8]"), deserializeList("[0]")))
        self.assertEqual(ans, "[1, 8]")

    def testcase6(self):
        ans = serializeList(self.soln_obj.addTwoNumbers(deserializeList("[9, 9, 9]"), deserializeList("[1]")))
        self.assertEqual(ans, "[0, 0, 0, 1]")

    def test_random(self):
        num_tests = 10000
        for _ in range(num_tests):
            num1, num2 = randint(0, 2 ** 31), randint(0, 2 ** 31)
            lst1, lst2 = list(map(int, str(num1)[::-1])), list(map(int, str(num2)[::-1]))
            expected = str(list(map(int, str(num1 + num2)[::-1])))
            ans = serializeList(self.soln_obj.addTwoNumbers(
                deserializeList(str(lst1)), 
                deserializeList(str(lst2)))
            )
            self.assertEqual(ans, expected)


if __name__ == '__main__':
    unittest.main()
