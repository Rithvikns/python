# Set Operations in Python

## Introduction
Python provides a built-in `set` data structure that allows performing various mathematical set operations efficiently. Below are the key set operations available in Python.

## Set Operations

### 1. **Union (`|` or `union()`)**
Combines all unique elements from both sets.
```python
A | B
A.union(B)
```
**Example:**
```python
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)  # Output: {1, 2, 3, 4, 5}
```

### 2. **Intersection (`&` or `intersection()`)**
Finds common elements between two sets.
```python
A & B
A.intersection(B)
```
**Example:**
```python
print(A & B)  # Output: {3}
```

### 3. **Difference (`-` or `difference()`)**
Finds elements in one set but not in the other.
```python
A - B
A.difference(B)
```
**Example:**
```python
print(A - B)  # Output: {1, 2}
```

### 4. **Symmetric Difference (`^` or `symmetric_difference()`)**
Finds elements in either set but not in both.
```python
A ^ B
A.symmetric_difference(B)
```
**Example:**
```python
print(A ^ B)  # Output: {1, 2, 4, 5}
```

### 5. **Subset (`<=` or `issubset()`)**
Checks if one set is a subset of another.
```python
A <= B
A.issubset(B)
```
**Example:**
```python
print({1, 2}.issubset(A))  # Output: True
```

### 6. **Superset (`>=` or `issuperset()`)**
Checks if one set is a superset of another.
```python
A >= B
A.issuperset(B)
```
**Example:**
```python
print(A.issuperset({1, 2}))  # Output: True
```

### 7. **Disjoint (`isdisjoint()`)**
Checks if two sets have no elements in common.
```python
A.isdisjoint(B)
```
**Example:**
```python
C = {6, 7, 8}
print(A.isdisjoint(C))  # Output: True
```

## Conclusion
Python's set operations provide a powerful way to manipulate collections of unique elements. Understanding these operations helps in efficiently managing data in various programming scenarios.

