
/*
# Sequential Digits

An integer has *sequential digits* if and only if each digit in the number is one more than the previous digit.

Return a **sorted** list of all the integers in the range `[low, high]` inclusive that have sequential digits.


**Example 1:** 
```
Input: low = 100, high = 300
Output: [123,234]
```

**Example 2:** 
```
Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
```

**Constraints:** 
    - `10 <= low <= high <= 10^9` 
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include "util.h"

using namespace std;

class Solution {
public:
    vector<int> sequentialDigits(int low, int high) {
        vector<int> nums;
        for (int start_digit = 1; start_digit <= 9; start_digit++) {
            int curr_num = 0;
            for (int end_digit = start_digit; end_digit <= 9; end_digit++) {
                curr_num = curr_num * 10 + end_digit;
                if (low <= curr_num && curr_num <= high) {
                    nums.push_back(curr_num);
                } else if (curr_num > high) {
                    break;
                }
            }
        }
        sort(nums.begin(), nums.end());
        return nums;
    }
};

int main(int argc, char *argv[]) {
    Solution obj;

    // {123, 234}
    print<int>(obj.sequentialDigits(100, 300));

    // {1234, 2345, 3456, 4567, 5678, 6789, 12345}
    print<int>(obj.sequentialDigits(1000, 13000));

    return 0;
}
