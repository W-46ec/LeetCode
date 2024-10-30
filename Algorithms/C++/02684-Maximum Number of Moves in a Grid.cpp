
/*
# Maximum Number of Moves in a Grid

You are given a **0-indexed** `m x n` matrix `grid` consisting of **positive** integers.

You can start at **any** cell in the first column of the matrix, and traverse the grid in the following way:
- From a cell `(row, col)`, you can move to any of the cells: `(row - 1, col + 1)`, `(row, col + 1)` and `(row + 1, col + 1)` such that the value of the cell you move to, should be **strictly** bigger than the value of the current cell.

Return *the **maximum** number of **moves** that you can perform*.


**Example 1:**
![2684_yetgriddrawio-10](./img/2684_yetgriddrawio-10.png)
```
Input: grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
Output: 3
Explanation: We can start at the cell (0, 0) and make the following moves:
- (0, 0) -> (0, 1).
- (0, 1) -> (1, 2).
- (1, 2) -> (2, 3).
It can be shown that it is the maximum number of moves that can be made.
```

**Example 2:** 
![2684_yetgrid4drawio](./img/2684_yetgrid4drawio.png)
```
Input: grid = [[3,2,4],[2,1,9],[1,1,7]]
Output: 0
Explanation: Starting from any cell in the first column we cannot perform any moves.
```

**Constraints:** 
    - `m == grid.length` 
    - `n == grid[i].length` 
    - `2 <= m, n <= 1000` 
    - `4 <= m * n <= 10^5` 
    - `1 <= grid[i][j] <= 10^6` 
*/

#include <iostream>
#include <vector>
#include <cstring>
#include <math.h>

using namespace std;

class Solution {
public:
    int maxMoves(vector<vector<int>>& grid) {
        unsigned m = grid.size(), n = grid[0].size();
        int ans = 0;
        int **dp = new int*[m];
        for (unsigned i = 0; i < m; i++) {
            dp[i] = new int[n];
            memset(dp[i], 0, sizeof(int) * n);
        }
        for (unsigned j = n - 1; j > 0; j--) {
            for (unsigned i = 0; i < m; i++) {
                if (i >= 1 && grid[i - 1][j] > grid[i][j - 1]) {
                    dp[i][j - 1] = max(dp[i][j - 1], 1 + dp[i - 1][j]);
                }
                if (grid[i][j] > grid[i][j - 1]) {
                    dp[i][j - 1] = max(dp[i][j - 1], 1 + dp[i][j]);
                }
                if (i < m - 1 and grid[i + 1][j] > grid[i][j - 1]) {
                    dp[i][j - 1] = max(dp[i][j - 1], 1 + dp[i + 1][j]);
                }
                if (j == 1) {
                    ans = max(ans, dp[i][j - 1]);
                }
            }
        }
        for (unsigned i = 0; i < m; i++) {
            delete [] dp[i];
        }
        delete [] dp;
        return ans;
    }
};


int main(int argc, char *argv[]) {
    Solution obj;

    vector<vector<int>> grid = {{2, 4, 3, 5}, {5, 4, 9, 3}, {3, 4, 2, 11}, {10, 9, 13, 15}};
    cout << obj.maxMoves(grid) << endl;     // 3

    return 0;
}
