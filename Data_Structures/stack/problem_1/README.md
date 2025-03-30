# Problem Statement

### Title: **Valid Parentheses Matching**

In this problem, you are tasked with determining if a given string containing various types of parentheses is **valid**. A string is considered valid if:
1. Each opening parenthesis `(` must have a corresponding closing parenthesis `)`.
2. Each opening square bracket `[` must have a corresponding closing square bracket `]`.
3. Each opening curly brace `{` must have a corresponding closing curly brace `}`.
4. The parentheses must be properly nested. That is, each parenthesis, bracket, or brace must close in the correct order.

For example:
- `()`, `[]`, and `{[]}` are valid.
- `([)]` and `((()` are not valid.

### Objective

Your task is to implement a solution that determines whether the parentheses in the given string are valid. This can be efficiently solved using a **stack** data structure.

### Requirements
1. You are given a string `s` containing only the characters `(`, `)`, `{`, `}`, `[`, `]`.
2. Your solution should return `true` if the string is valid and `false` otherwise.

### Example

```text
Input: s = "()"  
Output: true

Input: s = "()[]{}"  
Output: true

Input: s = "(]"  
Output: false

Input: s = "([)]"  
Output: false

Input: s = "{[]}"  
Output: true

