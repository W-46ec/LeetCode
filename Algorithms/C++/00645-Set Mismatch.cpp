
/*
# Set Mismatch

You have a set of integers `s`, which originally contains all the numbers from `1` to `n`. Unfortunately, due to some error, one of the numbers in `s` got duplicated to another number in the set, which results in **repetition of one** number and **loss of another** number.

You are given an integer array `nums` representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return *them in the form of an array*.


**Example 1:** 
```
Input: nums = [1,2,2,4]
Output: [2,3]
```

**Example 2:** 
```
Input: nums = [1,1]
Output: [1,2]
```

**Constraints:** 
    - `2 <= nums.length <= 10^4` 
    - `1 <= nums[i] <= 10^4` 
*/

#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        unordered_set<int> s;
        int repeated = 0, nums_sum = 0;
        for (unsigned i = 0; i < nums.size(); i++) {
            repeated = s.find(nums[i]) != s.end() ? nums[i] : repeated;
            s.insert(nums[i]);
            nums_sum += nums[i];
        }

        int target_sum = (1 + nums.size()) * nums.size() / 2;
        vector<int> ans = {repeated, target_sum - (nums_sum - repeated)};
        return ans;
    }
};

int main(int argc, char *argv[]) {
    Solution obj;
    vector<int> nums = {1, 2, 2, 4};
    vector<int> ans = obj.findErrorNums(nums);
    cout << ans[0] << ", " << ans[1] << endl;

    return 0;
}

