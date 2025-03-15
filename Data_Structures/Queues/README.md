# Stack Implementation Using Two Queues

## Overview
This project implements a stack data structure using two queues in Python. The stack follows the Last-In-First-Out (LIFO) principle, where the last element inserted is the first one to be removed. Since Python provides an efficient queue implementation through `collections.deque`, we use two deque objects to simulate stack operations.

## Approach
A stack typically supports the following operations:
1. **Push (x)** – Adds an element `x` to the stack.
2. **Pop ()** – Removes and returns the top element of the stack.
3. **Top ()** – Returns the top element without removing it.
4. **Is_Empty ()** – Checks whether the stack is empty.
5. **Size ()** – Returns the number of elements in the stack.

To simulate a stack using two queues:
- **Push Operation:** The element is simply added to `queue1`.
- **Pop Operation:** All elements except the last are transferred from `queue1` to `queue2`. The last element is removed, and then the queue references are swapped.
- **Top Operation:** The last element is retrieved using the same logic as `pop`, but it is reinserted into `queue2`.
- **Swapping Queues:** After each `pop` or `top`, `queue1` and `queue2` are swapped to maintain the correct order.

## Complexity Analysis
- **Push Operation:** \(O(1)\) – Directly enqueueing an element.
- **Pop Operation:** \(O(n)\) – Moving \(n-1\) elements to another queue before removing the last element.
- **Top Operation:** \(O(n)\) – Similar to `pop`, but the last element is retained.
- **Is_Empty & Size:** \(O(1)\) – Constant time operations.

## Example Usage
A simple test case could involve pushing values onto the stack, checking the top element, and popping elements while verifying LIFO behavior.

## Conclusion
Using two queues to implement a stack introduces some overhead in the `pop` and `top` operations. However, this approach helps reinforce queue and stack concepts, especially in constrained environments where only queue operations are allowed.


