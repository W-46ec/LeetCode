
"""
# Prime Subtraction Operation

You are given a **0-indexed** integer array `nums` of length `n`.

You can perform the following operation as many times as you want:
- Pick an index `i` that you haven’t picked before, and pick a prime `p` **strictly less than** `nums[i]`, then subtract `p` from `nums[i]`.

Return *true if you can make `nums` a strictly increasing array using the above operation and false otherwise*.

A **strictly increasing array** is an array whose each element is strictly greater than its preceding element.


**Example 1:** 
```
Input: nums = [4,9,6,10]
Output: true
Explanation: In the first operation: Pick i = 0 and p = 3, and then subtract 3 from nums[0], so that nums becomes [1,9,6,10].
In the second operation: i = 1, p = 7, subtract 7 from nums[1], so nums becomes equal to [1,2,6,10].
After the second operation, nums is sorted in strictly increasing order, so the answer is true.
```

**Example 2:** 
```
Input: nums = [6,8,11,12]
Output: true
Explanation: Initially nums is sorted in strictly increasing order, so we don't need to make any operations.
```

**Example 3:** 
```
Input: nums = [5,8,3]
Output: false
Explanation: It can be proven that there is no way to perform operations to make nums sorted in strictly increasing order, so the answer is false.
```

**Constraints:** 
    - `1 <= nums.length <= 1000` 
    - `1 <= nums[i] <= 1000` 
    - `nums.length == n` 
"""

import unittest
from typing import List
import itertools

class Solution:
    # def prime_generator():
    #     """
    #     Sieve of Eratosthenes:
    #     1. Generate an infinite list of integers that are >= 2.
    #     2. Yield the first element p from the list, and then remove
    #     all elements that are divisible by p from the list.
    #     """
    #     def _not_divisible(n):
    #         return lambda x: x % n != 0

    #     nums = itertools.count(start = 2, step = 1)
    #     while True:
    #         p = next(nums)
    #         yield p
    #         nums = filter(_not_divisible(p), nums)

    def primeSubOperation(self, nums: List[int]) -> bool:
        # Hard-code the list of primes that are <= 1000
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
        prev = 0
        for x in nums:
            i = 0
            while i < len(primes) and prev < x - primes[i]:
                i += 1
            if i == 0 and x <= prev:
                return False
            prev = x - (primes[i - 1] if i > 0 else 0)
        return True


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.primeSubOperation([4, 9, 6, 10]), True)

    def testcase2(self):
        self.assertEqual(self.soln_obj.primeSubOperation([6, 8, 11, 12]), True)

    def testcase3(self):
        self.assertEqual(self.soln_obj.primeSubOperation([5, 8, 3]), False)

    def testcase4(self):
        self.assertEqual(self.soln_obj.primeSubOperation([998, 2]), True)

    def testcase5(self):
        self.assertEqual(self.soln_obj.primeSubOperation([998, 2, 3]), True)

    def testcase6(self):
        self.assertEqual(self.soln_obj.primeSubOperation([2, 3, 5]), True)

    def testcase7(self):
        self.assertEqual(self.soln_obj.primeSubOperation([1, 20, 7, 12, 4]), False)

    def testcase8(self):
        self.assertEqual(self.soln_obj.primeSubOperation([2, 2]), False)


if __name__ == '__main__':
    unittest.main()