# Regular Expressions in Python

## Introduction
Regular expressions (regex) are a powerful tool in Python for pattern matching and text processing. The `re` module in Python provides support for working with regular expressions.

## Importing the `re` Module
```python
import re
```

## Basic Functions in `re`

### 1. `re.match()`
Attempts to match a pattern at the beginning of a string.
```python
pattern = r'hello'
string = 'hello world'
match = re.match(pattern, string)
if match:
    print("Match found:", match.group())
```

### 2. `re.search()`
Searches the entire string for a pattern match.
```python
pattern = r'world'
string = 'hello world'
match = re.search(pattern, string)
if match:
    print("Match found:", match.group())
```

### 3. `re.findall()`
Finds all occurrences of a pattern in a string and returns a list.
```python
pattern = r'\d+'
string = 'There are 3 cats, 4 dogs, and 5 birds.'
numbers = re.findall(pattern, string)
print("Numbers found:", numbers)
```

### 4. `re.finditer()`
Finds all occurrences of a pattern and returns an iterator of match objects.
```python
pattern = r'\b\w{3}\b'
string = 'The cat sat on the mat.'
matches = re.finditer(pattern, string)
for match in matches:
    print("Match found:", match.group())
```

### 5. `re.sub()`
Replaces occurrences of a pattern with a specified string.
```python
pattern = r'cat'
replacement = 'dog'
string = 'The cat sat on the cat.'
new_string = re.sub(pattern, replacement, string)
print("Modified string:", new_string)
```

### 6. `re.split()`
Splits a string based on a regex pattern.
```python
pattern = r'[,;\s]+'
string = 'apple, orange; banana grape'
tokens = re.split(pattern, string)
print("Tokens:", tokens)
```

## Common Regular Expression Patterns

| Pattern | Description |
|---------|-------------|
| `\d` | Matches any digit (0-9) |
| `\D` | Matches any non-digit |
| `\w` | Matches any word character (alphanumeric + underscore) |
| `\W` | Matches any non-word character |
| `\s` | Matches any whitespace character |
| `\S` | Matches any non-whitespace character |
| `^` | Matches the start of a string |
| `$` | Matches the end of a string |
| `.` | Matches any character except newline |
| `*` | Matches 0 or more repetitions |
| `+` | Matches 1 or more repetitions |
| `?` | Matches 0 or 1 occurrence |
| `{n,m}` | Matches between n and m repetitions |
| `(group)` | Captures a group |
| `(?:group)` | Non-capturing group |
| `|` | OR operator |

## Compiling Regular Expressions
Using `re.compile()` to compile regex patterns for better performance.
```python
pattern = re.compile(r'\d+')
string = 'I have 12 apples and 34 oranges.'
print(pattern.findall(string))
```

## Using Flags in Regular Expressions
Flags modify the behavior of regex functions.

### 1. `re.IGNORECASE (re.I)`
Case-insensitive matching.
```python
pattern = re.compile(r'hello', re.I)
print(pattern.findall('Hello HELLO hello'))
```

### 2. `re.MULTILINE (re.M)`
Enables multi-line matching.
```python
pattern = re.compile(r'^start', re.M)
string = 'start of line\nAnother line\nstart again'
print(pattern.findall(string))
```

### 3. `re.DOTALL (re.S)`
Allows `.` to match newline characters.
```python
pattern = re.compile(r'.+', re.S)
string = 'Hello\nWorld'
print(pattern.findall(string))
```

## Conclusion
Regular expressions in Python are a powerful tool for pattern matching and text processing. Mastering `re` functions and patterns allows for efficient string manipulation.
