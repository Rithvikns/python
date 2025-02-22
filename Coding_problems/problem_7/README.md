# Explanation of Maximum XOR using Trie

## Overview
This document explains how to construct a Trie to find the maximum XOR of two numbers in a given list. The approach optimizes the brute-force `O(n²)` method to `O(n log M)` using a **binary Trie**.

---

## **Trie Structure**
A **Trie (prefix tree)** is used to store numbers in **binary format**. Each node has two possible branches:
- `0` (left branch)
- `1` (right branch)

Each number is stored **bit by bit**, creating a path from the root to a leaf node.

### Example:
For numbers `[3, 10, 5, 25, 2, 8]`, their **5-bit binary representation** is:
```
3  ->  00011
10 ->  01010
5  ->  00101
25 ->  11001
2  ->  00010
8  ->  01000
```
The **Trie structure** will look like:
```
        (root)
        /    \
       0      1
      /  \     \
     0     1    1
    / \    |    |
   0   1   0    0
  /|   |  / \   |
 1 1   0 0   1  0
 | |   | |   |  |
 1 0   1 0   0  1
(3)(2)(5)(8)(10)(25)     
```
---
# How the Code Works

TrieNode Class:

Each node stores its children (binary 0 and 1).
A value field at the leaf node holds the final number.

Trie Class:

insert(num): Converts num to 5-bit binary and inserts it bit by bit.
find_max_xor(num):
Traverses the Trie, choosing opposite bits when possible for maximum XOR.
Returns the number that maximizes XOR and the XOR result.

Main Execution:

Numbers are inserted into the Trie.
The script finds the two numbers that produce the maximum XOR.

---
## **How the Trie Helps Find Maximum XOR**
For each number, we traverse the Trie trying to pick **opposite bits** to maximize XOR.

### Example: Finding XOR for `25 (11001)`
| **Bit Position** | **Bit in 25** | **Preferred Opposite** | **Exists in Trie?** | **Chosen Bit** |
|-----------------|--------------|----------------------|-----------------|--------------|
| **4** (MSB)    | `1`          | `0`                  | ✅ Yes          | `0`          |
| **3**          | `1`          | `0`                  | ✅ Yes          | `0`          |
| **2**          | `0`          | `1`                  | ✅ Yes          | `1`          |
| **1**          | `0`          | `1`                  | ✅ Yes          | `1`          |
| **0** (LSB)    | `1`          | `0`                  | ✅ Yes          | `0`          |

Final XOR Pair: `25 (11001) ⊕ 5 (00101) = 28 (11100)`

---

## **Final Output**
```
Max XOR is 28, achieved by 5 ⊕ 25
```

---

## **Key Takeaways**
1. **Trie stores numbers in binary for efficient XOR calculations.**
2. **Each number follows a unique path from root to leaf.**
3. **To maximize XOR, always prefer opposite bits when possible.**
4. **Efficient `O(n log M)` solution instead of `O(n²)` brute force.**

---

### 🚀 Let me know if you need further clarifications!
