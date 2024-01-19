
/*
# Minimum Falling Path Sum

Given an `n x n` array of integers `matrix`, return *the **minimum sum** of any **falling path** through `matrix`*.

A **falling path** starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position `(row, col)` will be `(row + 1, col - 1)`, `(row + 1, col)`, or `(row + 1, col + 1)`.


**Example 1:** 
![931_failing1-grid](./img/931_failing1-grid.jpg)
```
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.
```

**Example 2:** 
![931_failing2-grid](./img/931_failing2-grid.jpg)
```
Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.
```

**Constraints:** 
    - `n == matrix.length == matrix[i].length` 
    - `1 <= n <= 100` 
    - `-100 <= matrix[i][j] <= 100` 
*/

#include <iostream>
#include <vector>
#include <climits>
#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        /*
        Dynamic programming approach
        dp[i][j] <- the minimum sum of falling path from the first row to cell matrix[i][j].
        Base case: dp[0][j] <- matrix[0][j] for all j = 0, 1, ..., n - 1.

        By definition, if we want to reach matrix[i][j], we must first reach one of the
        following cells: matrix[i - 1][j - 1], matrix[i - 1][j], or matrix[i - 1][j + 1].

        Therefore, we have the following recurrence equation:
        dp[i][j] = matrix[i][j] + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1]), 
        for i = 1, 2, ..., n - 1. And let dp[i - 1][k] be infinity if k is not in range [0, n).

        Eventually, we return the minimum value on the last row of dp.
        */
        int n = matrix.size();
        vector<vector<int>> dp;
        for (int i = 0; i < n; i++) {
            if (i == 0) {
                dp.push_back(matrix[i]);
            } else {
                vector<int> row(n);
                dp.push_back(row);
            }
        }

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int val = dp[i - 1][j];
                val = min(val, j >= 1 ? dp[i - 1][j - 1] : INT_MAX);
                val = min(val, j < n - 1 ? dp[i - 1][j + 1] : INT_MAX);
                dp[i][j] = matrix[i][j] + val;
            }
        }

        return *min_element(dp[n - 1].begin(), dp[n - 1].end());
    }
};


int main(int argc, char *argv[]) {
	Solution obj;
	vector<vector<int>> matrix = {{2, 1, 3}, {6, 5, 4}, {7, 8, 9}};
	cout << obj.minFallingPathSum(matrix) << endl;	// 13

	return 0;
}
