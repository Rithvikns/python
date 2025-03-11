# Explanation of Trie Implementation

A **Trie** (also known as a prefix tree) is a tree-like data structure used for storing strings in a way that allows for efficient prefix-based searching. This implementation consists of three primary methods:

1. **insert(word)** - Adds a word to the Trie.
2. **search(word)** - Checks if a word exists in the Trie.
3. **startsWith(prefix)** - Checks if any word in the Trie starts with the given prefix.

---
## **Understanding TrieNode and Trie Structure**
### **TrieNode Class**
Each node in the Trie represents a single character and contains:
- A dictionary `children` to store its child nodes.
- A boolean flag `is_end_of_word` to indicate if a word ends at this node.

### **Trie Class**
- The Trie class starts with an empty root node.
- Each word is inserted character by character into the tree.
- The `is_end_of_word` flag is set at the last character of an inserted word.

---
## **How Each Method Works**
### **Insertion (`insert(word)`)**
- Traverse through each character in the word.
- If the character does not exist in the current node’s children, create a new TrieNode.
- Move to the next character’s node.
- Mark the last node of the word as `is_end_of_word = True`.

#### **Example:**
Inserting "apple" into an empty Trie:
```
Root → a → p → p → l → e*
(* denotes end of word)
```
Inserting "app" afterward:
```
Root → a → p → p* → l → e*
```

### **Search (`search(word)`)**
- Traverse through each character in the word.
- If any character is missing, return `False`.
- If all characters exist and `is_end_of_word = True` at the last character, return `True`.

#### **Example:**
```
trie.search("apple") → True
trie.search("app") → False (since "app" is not marked as a word)
```

### **Prefix Search (`startsWith(prefix)`)**
- Similar to `search()`, but does not check `is_end_of_word`.
- Returns `True` if all characters of the prefix exist in sequence.

#### **Example:**
```
trie.startsWith("app") → True (since "apple" and "app" exist in Trie)
trie.startsWith("apz") → False (no word starts with "apz")
```

---
## **Complexity Analysis**
- **Insertion**: O(n), where n is the length of the word.
- **Search**: O(n), where n is the length of the word.
- **Prefix Search**: O(n), where n is the length of the prefix.

Since Trie operations do not involve sorting or comparisons, they are significantly faster than other data structures for prefix-based searching.

---
## **Use Cases of Tries**
- **Autocomplete systems** (e.g., search engines, typing suggestions)
- **Spell checkers**
- **IP Routing**
- **DNA sequence storage**
- **Prefix-based searching in large datasets**

This Trie implementation provides an efficient way to store and retrieve words with prefix-based searching in O(n) time complexity, making it highly useful for real-world applications like search engines and autocomplete systems.

# **Using Data Classes in Trie Implementation**
### **Why Use Data Classes?**
Data classes in Python (`@dataclass` from the `dataclasses` module) help improve readability and reduce boilerplate code by automatically generating methods like `__init__` and `__repr__`.

## **Rewriting Trie with Data Classes**
Instead of defining a separate `__init__` method, we use `@dataclass` for automatic initialization.

## **How Each Method Works with Data Classes**
### **Insertion (`insert(word)`)**
- Traverse through each character in the word.
- If the character does not exist in the current node’s children, create a new `TrieNode`.
- Move to the next character’s node.
- Mark the last node of the word as `is_end_of_word = True`.

#### **Example:**
Inserting "apple" into an empty Trie:
```
Root → a → p → p → l → e*
(* denotes end of word)
```
Inserting "app" afterward:
```
Root → a → p → p* → l → e*
```

### **Search (`search(word)`)**
- Traverse through each character in the word.
- If any character is missing, return `False`.
- If all characters exist and `is_end_of_word = True` at the last character, return `True`.

#### **Example:**
```
trie.search("apple") → True
trie.search("app") → False (since "app" is not marked as a word)
```

### **Prefix Search (`startsWith(prefix)`)**
- Similar to `search()`, but does not check `is_end_of_word`.
- Returns `True` if all characters of the prefix exist in sequence.

#### **Example:**
```
trie.startsWith("app") → True (since "apple" and "app" exist in Trie)
trie.startsWith("apz") → False (no word starts with "apz")
```

---
## **Complexity Analysis**
- **Insertion**: O(n), where n is the length of the word.
- **Search**: O(n), where n is the length of the word.
- **Prefix Search**: O(n), where n is the length of the prefix.

Using data classes provides a clean and structured approach to implementing a Trie, making the code more readable and maintainable.


