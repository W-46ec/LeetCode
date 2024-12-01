
/*
# Check If N and Its Double Exist

Given an array `arr` of integers, check if there exist two indices `i` and `j` such that:
- `i != j` 
- `0 <= i, j < arr.length` 
- `arr[i] == 2 * arr[j]` 
 

**Example 1:** 
```
Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
```

**Example 2:** 
```
Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
```

**Constraints:** 
    - `2 <= arr.length <= 500` 
    - `-10^3 <= arr[i] <= 10^3` 
*/

#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        unordered_set<int> seen;
        for (unsigned i = 0; i < arr.size(); i++) {
            if (seen.find(2 * arr[i]) != seen.end() 
                    || ((arr[i] / 2) * 2 == arr[i] && seen.find(arr[i] / 2) != seen.end())) {
                return true;
            }
            seen.insert(arr[i]);
        }
        return false;
    }
};


int main(int argc, char *argv[]) {
    Solution obj;
    vector<int> arr = {10, 2, 5, 3};
    cout << obj.checkIfExist(arr) << endl;  // 1
    arr = vector<int>{3, 1, 7, 11};
    cout << obj.checkIfExist(arr) << endl;  // 0
    return 0;
}

