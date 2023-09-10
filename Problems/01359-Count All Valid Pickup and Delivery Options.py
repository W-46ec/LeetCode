
"""
# Count All Valid Pickup and Delivery Options

Given `n` orders, each order consist in pickup and delivery services. 

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 

Since the answer may be too large, return it modulo 10^9 + 7.


**Example 1:** 
```
Input: n = 1
Output: 1
Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.
```

**Example 2:** 
```
Input: n = 2
Output: 6
Explanation: All possible orders: 
(P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.
```

**Example 3:** 
```
Input: n = 3
Output: 90
```

Constraints:
	- `1 <= n <= 500` 
"""

class Solution:
    def countOrders(self, n: int) -> int:
        """
        Dynamic programming approach

        Let S_k be the solution for n = k, where k = 1, 2, 3, ...

        Assume we already have the solution for n = k - 1 (i.e., S_{k - 1}), by definitions, 
        there are (k - 1) pairs of pickup and delivery services (add up to 2(k - 1) items in total).

        Now, let's consider adding the kth pair (i.e., (P_k, D_k)).
        Among the existing 2(k - 1) items, there are (2k - 1) slots where we may insert P_k.

        Example for inserting a new pair into 2 items:
        . | . | . 

        '|' represents the existing items, '.' represents the slot where we can insert P_k into.

        Since D_k can only be inserted after P_k, we have the following properties:
        - If P_k is inserted into the first slot, there are (2k - 1) slots where we can insert D_k;
        - If P_k is inserted into the second slot, there are (2k - 2) slots where we can insert D_k;
        - ...
        - If P_k is inserted into the last slot, there is only 1 slot where we can insert D_k;

        So in total, there are [(2k - 1) + (2k - 2) + (2k - 3) + ... + 2 + 1] ways to add the kth
        pair into the existing solution for the previous (k - 1)th pairs.

        Note that: [(2k - 1) + (2k - 2) + (2k - 3) + ... + 2 + 1] = [2k(2k - 1)] / 2 = 2k^2 - k
        
        So we have the following recurrence equation: S_k = S_{k - 1} * (2k^2 - k).
        The base case is given by S_1 = 1.
        """

        S = 1
        for k in range(2, n + 1):
            S *= (2 * k ** 2 - k)
            S %= 1000000007
        return S

# 1
print(Solution().countOrders(1))

# 6
print(Solution().countOrders(2))

# 90
print(Solution().countOrders(3))

# 2520
print(Solution().countOrders(4))

# 113400
print(Solution().countOrders(5))

# 7484400
print(Solution().countOrders(6))

# 681080400
print(Solution().countOrders(7))

# 729647433
print(Solution().countOrders(8))
