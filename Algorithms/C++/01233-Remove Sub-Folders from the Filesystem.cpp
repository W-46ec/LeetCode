
/*
# Remove Sub-Folders from the Filesystem

Given a list of folders `folder`, return *the folders after removing all **sub-folders** in those folders*. You may return the answer in **any order**.

If a `folder[i]` is located within another `folder[j]`, it is called a **sub-folder** of it. A sub-folder of `folder[j]` must start with `folder[j]`, followed by a `"/"`. For example, `"/a/b"` is a sub-folder of `"/a"`, but `"/b"` is not a sub-folder of `"/a/b/c"`.

The format of a path is one or more concatenated strings of the form: `'/'` followed by one or more lowercase English letters.

- For example, `"/leetcode"` and `"/leetcode/problems"` are valid paths while an empty string and `"/"` are not.


**Example 1:** 
```
Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
Output: ["/a","/c/d","/c/f"]
Explanation: Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.
```

**Example 2:** 
```
Input: folder = ["/a","/a/b/c","/a/b/d"]
Output: ["/a"]
Explanation: Folders "/a/b/c" and "/a/b/d" will be removed because they are subfolders of "/a".
```

**Example 3:** 
```
Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
Output: ["/a/b/c","/a/b/ca","/a/b/d"]
```

**Constraints:** 
    - `1 <= folder.length <= 4 * 10^4` 
    - `2 <= folder[i].length <= 100` 
    - `folder[i]` contains only lowercase letters and `'/'`.
    - `folder[i]` always starts with the character `'/'`.
    - Each folder name is **unique**.
*/


#include <iostream>
#include <algorithm>
#include "util.h"

using namespace std;

class Solution {
private:
    bool isSubfolder(const string &folder1, const string &folder2) {
        unsigned i = 0;
        for (; i < folder1.size() && i < folder2.size(); i++) {
            if (folder1[i] != folder2[i]) {
                return false;
            }
        }
        return i < folder2.size() && folder2[i] == '/';
    }

public:
    vector<string> removeSubfolders(vector<string>& folder) {
        sort(folder.begin(), folder.end());
        unsigned i = 0;
        while (i < folder.size() - 1) {
            if (isSubfolder(folder[i], folder[i + 1])) {
                folder.erase(folder.begin() + i + 1);
            } else {
                i++;
            }
        }
        return folder;
    }
};


int main(int argc, char *argv[]) {
    Solution obj;

    vector<string> folder = {"/a", "/a/b", "/c/d", "/c/d/e", "/c/f"};
    // {"/a", "/c/d", "/c/f"}
    print<string>(obj.removeSubfolders(folder), "\n", '"');

    folder = vector<string>{"/a", "/a/b/c", "/a/b/d"};
    // {"/a"}
    print<string>(obj.removeSubfolders(folder), "\n", '"');

    folder = vector<string>{"/a/b/c", "/a/b/ca", "/a/b/d"};
    // {"/a/b/c", "/a/b/ca", "/a/b/d"}
    print<string>(obj.removeSubfolders(folder), "\n", '"');

    folder = vector<string>{"/a", "/a/b", "/a/b/c/d"};
    // {"/a"}
    print<string>(obj.removeSubfolders(folder), "\n", '"');

    return 0;
}
