
"""
# Implement Stack using Queues

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (`push`, `top`, `pop`, and `empty`).

Implement the `MyStack` class:
    - `void push(int x)` Pushes element x to the top of the stack.
    - `int pop()` Removes the element on the top of the stack and returns it.
    - `int top()` Returns the element on the top of the stack.
    - `boolean empty()` Returns `true` if the stack is empty, `false` otherwise.

**Notes**:
    - You must use **only** standard operations of a queue, which means that only `push to back`, `peek/pop from front`, `size` and `is empty` operations are valid.
    - Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.


**Example 1:** 
```
Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
```

**Constraints:** 
    - `1 <= x <= 9` 
    - At most `100` calls will be made to `push`, `pop`, `top`, and `empty`.
    - All the calls to `pop` and `top` are valid.


**Follow-up**: Can you implement the stack using only one queue?
"""

# # Two-queue solution
# class MyStack:
#     def __init__(self):
#         # Number of elements in the queue
#         self.size = 0

#         # Queue1 is the main queue to store data
#         # Queue2 is the auxiliary queue
#         self.queue1, self.queue2 = [], []

#         # Keep track of the top element value so that
#         # the `top` operation can be done in O(1) time.
#         self.curr_top_val = None

#     # O(1) time operation
#     def push(self, x: int) -> None:
#         self.queue1.append(x)
#         self.curr_top_val = x
#         self.size += 1

#     # O(n) time operation
#     def pop(self) -> int:
#         self.curr_top_val = None
#         for i in range(self.size - 1):
#             # Update the value of `curr_top_val`
#             if i == self.size - 2:
#                 self.curr_top_val = self.queue1[0]
#             # Dequeue (size - 1) elements from queue1 
#             # and enqueue them to queue2.
#             self.queue2.append(self.queue1.pop(0))
#         # Top element
#         res = self.queue1.pop(0)
#         # Swap queue1 and queue2
#         self.queue1, self.queue2 = self.queue2, self.queue1
#         self.size -= 1
#         return res

#     # O(1) time operation
#     def top(self) -> int:
#         return self.curr_top_val

#     # O(1) time operation
#     def empty(self) -> bool:
#         return self.size == 0

# One-queue solution
class MyStack:
    def __init__(self):
        # Number of elements in the queue
        self.size = 0

        # Queue
        self.queue = []

        # Keep track of the top element value so that
        # the `top` operation can be done in O(1) time.
        self.curr_top_val = None

    # O(1) time operation
    def push(self, x: int) -> None:
        self.queue.append(x)
        self.curr_top_val = x
        self.size += 1

    # O(n) time operation
    def pop(self) -> int:
        self.curr_top_val = None
        for i in range(self.size - 1):
            # Update the value of `curr_top_val`
            if i == self.size - 2:
                self.curr_top_val = self.queue[0]
            # Dequeue (size - 1) elements from the queue
            # and enqueue them back to queue.
            self.queue.append(self.queue.pop(0))
        # Top element
        res = self.queue.pop(0)
        # Update size
        self.size -= 1
        return res

    # O(1) time operation
    def top(self) -> int:
        return self.curr_top_val

    # O(1) time operation
    def empty(self) -> bool:
        return self.size == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
