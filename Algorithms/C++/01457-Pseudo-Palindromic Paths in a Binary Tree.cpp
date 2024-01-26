
/*
# Pseudo-Palindromic Paths in a Binary Tree

Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be **pseudo-palindromic** if at least one permutation of the node values in the path is a palindrome.

Return *the number of **pseudo-palindromic** paths going from the root node to leaf nodes*.


**Example 1:** 
![1457_palindromic_paths_1](./img/1457_palindromic_paths_1.png)
```
Input: root = [2,3,1,3,1,null,1]
Output: 2 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).
```

**Example 2:** 
![1457_palindromic_paths_2](./img/1457_palindromic_paths_2.png)
```
Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).
```

**Example 3:** 
```
Input: root = [9]
Output: 1
```

**Constraints:** 
    - The number of nodes in the tree is in the range `[1, 10^5]`.
    - `1 <= Node.val <= 9` 
*/

#include <iostream>
#include <stack>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int pseudoPalindromicPaths(TreeNode* root) {
        stack<pair<TreeNode *, int>> S;
        S.push(pair<TreeNode *, int>{root, 0});
        int count = 0;
        while (!S.empty()) {
            TreeNode *node = S.top().first;
            int path = S.top().second;
            S.pop();
            path ^= (1 << node -> val);
            if (node -> left == nullptr and node -> right == nullptr) {
                count += (path & (path - 1)) == 0 ? 1 : 0;
            } else {
                if (node -> left) {
                    S.push(pair<TreeNode *, int>{node -> left, path});
                }
                if (node -> right) {
                    S.push(pair<TreeNode *, int>{node -> right, path});
                }
            }
        }
        return count;
    }
};

int main(int argc, char *argv[]) {
    Solution obj;
    TreeNode t(9);
    cout << obj.pseudoPalindromicPaths(&t) << endl; // 1
    return 0;
}
