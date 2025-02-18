# Problem Statement

Flatten a Multilevel Doubly Linked List You are given a doubly linked list which in addition to the
next and previous pointers, it could have a child pointer which may or may not point to a separate doubly linked list.
These child lists may have one or more children of their own, and
so on, to produce a multilevel data structure, as shown in the
example below. Flatten the list so that all the nodes appear in a single-level doubly linked list. You are given the head of the first level of the list.


## Example 1:

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]

Output:[1,2,3,7,8,11,12,9,10,4,5,6]

# Solution

To flatten a multilevel doubly linked list, we can use a Depth-First Search (DFS) approach iteratively using a stack or recursively.

## Approach:
Start from the head of the list.
If a node has a child:
Store the next node (if it exists) onto a stack.
Make the child the next node of the current node.
Set the previous pointer of the child to the current node.
Remove the child pointer.
If there is no next node and the stack is not empty:
Pop a node from the stack and attach it as the next node.
Set its previous pointer correctly.
Continue until the entire list is processed.
'''
1 - 2 - 3 - 4 - 5 - 6
            |
            7 - 8 - 9 - 10
                |
               11 - 12
'''
1 - 2 - 3 - 7 - 8 - 11 - 12 - 9 - 10 - 4 - 5 - 6
