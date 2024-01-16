
"""
# Insert Delete GetRandom O(1)

Implement the `RandomizedSet` class:
    - `RandomizedSet()` Initializes the `RandomizedSet` object.
    - `bool insert(int val)` Inserts an item `val` into the set if not present. Returns `true` if the item was not present, `false` otherwise.
    - `bool remove(int val)` Removes an item `val` from the set if present. Returns `true` if the item was present, `false` otherwise.
    - `int getRandom()` Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the **same probability** of being returned.

You must implement the functions of the class such that each function works in **average** `O(1)` time complexity.


**Example 1:** 
```
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
```

**Constraints:** 
    - `-2^31 <= val <= 2^31 - 1` 
    - At most `2 * 10^5` calls will be made to `insert`, `remove`, and `getRandom`.
    - There will be **at least one** element in the data structure when `getRandom` is called.
"""

import unittest
import random

class RandomizedSet:
    def __init__(self):
        # self.arr stores the actual data
        self.arr = []
        # self.val2idx maps from values to indices in the array
        self.val2idx = {}

    def insert(self, val: int) -> bool:
        # O(1)
        # Append element to the end of the array
        if val not in self.val2idx:
            self.arr += [val]
            self.val2idx[val] = len(self.arr) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        # O(1)
        # If we pop an element from the middle of the array,
        # we move the last inserted element to this empty spot.
        if val in self.val2idx:
            last_element = self.arr[-1]
            self.arr[self.val2idx[val]] = last_element
            self.val2idx[last_element] = self.val2idx[val]
            self.val2idx.pop(val)
            self.arr.pop(-1)
            return True
        return False

    def getRandom(self) -> int:
        # O(1)
        return random.choice(self.arr)


class Test(unittest.TestCase):
    def setUp(self):
        self.obj = RandomizedSet()

    def testcase1(self):
        operations = ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
        inputs = [[], [1], [2], [2], [], [1], [2], []]
        answers = [None, True, False, True, 2, True, False, 2]
        assert len(operations) == len(inputs) == len(answers)
        for i in range(1, len(operations)):
            res = getattr(self.obj, operations[i])(*inputs[i])
            if operations[i] == "getRandom":
                self.assertIn(res, self.obj.arr)
            else:
                self.assertEqual(res, answers[i])


if __name__ == '__main__':
    unittest.main()
