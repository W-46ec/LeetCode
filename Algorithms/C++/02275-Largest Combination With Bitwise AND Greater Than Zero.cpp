
/*
# Largest Combination With Bitwise AND Greater Than Zero

The **bitwise AND** of an array `nums` is the bitwise AND of all integers in `nums`.
    - For example, for `nums = [1, 5, 3]`, the bitwise AND is equal to `1 & 5 & 3 = 1`.
    - Also, for `nums = [7]`, the bitwise AND is `7`.

You are given an array of positive integers `candidates`. Evaluate the **bitwise AND** of every **combination** of numbers of `candidates`. Each number in `candidates` may only be used **once** in each combination.

Return *the size of the **largest** combination of `candidates` with a bitwise AND **greater** than `0`*.


**Example 1:** 
```
Input: candidates = [16,17,71,62,12,24,14]
Output: 4
Explanation: The combination [16,17,62,24] has a bitwise AND of 16 & 17 & 62 & 24 = 16 > 0.
The size of the combination is 4.
It can be shown that no combination with a size greater than 4 has a bitwise AND greater than 0.
Note that more than one combination may have the largest size.
For example, the combination [62,12,24,14] has a bitwise AND of 62 & 12 & 24 & 14 = 8 > 0.
```

**Example 2:** 
```
Input: candidates = [8,8]
Output: 2
Explanation: The largest combination [8,8] has a bitwise AND of 8 & 8 = 8 > 0.
The size of the combination is 2, so we return 2.
```

**Constraints:** 
    - `1 <= candidates.length <= 10^5` 
    - `1 <= candidates[i] <= 10^7` 
*/

#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

class Solution {
public:
    int largestCombination(vector<int>& candidates) {
        /*
        Explanations:
        Let's write an arbitrary n-bit binary number b in the following form:
        (b_{n - 1}, b_{n - 2}, ..., b_0), where
        - b_i is either 0 or 1 for all i = 0, 1, ..., n - 1
        - b_0 is the least significant bit
        - and b_{n - 1} is the most significant bit.

        Recall one of the properties for bitwise AND operation:
        If any of the operands is 0, the result will be 0.
        So if we want the bitwise AND of a subset of candidates to 
        be non-zero, there must be some index j, such that b_j is 1 
        for all elements in that subset.

        Let bit_count[j] be the number of elements in candidates such 
        that b_j is non-zero. Out goal will be finding the max value 
        of bit_count[j] for j = 0, 1, ..., bit_count(max(candidates)).
        */
        int bit_count[32], max_count = 0;
        memset(bit_count, 0, sizeof(int) * 32);
        for (unsigned i = 0; i < candidates.size(); i++) {
            int x = candidates[i], bit_idx = 0;
            while (x) {
                bit_count[bit_idx] += x & 0x1;
                max_count = max(max_count, bit_count[bit_idx]);
                x = x >> 1;
                bit_idx++;
            }
        }
        return max_count;
    }
};


int main(int argc, char *argv[]) {
    Solution obj;

    vector<int> nums = {16, 17, 71, 62, 12, 24, 14};
    cout << obj.largestCombination(nums) << endl;       // 4

    nums = {8, 8};
    cout << obj.largestCombination(nums) << endl;       // 2

    nums = {1};
    cout << obj.largestCombination(nums) << endl;       // 1

    return 0;
}
