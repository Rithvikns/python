# Difference between using Regex and Normal Loops

## problem statement 
ABCXYZ company has up to  employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:
```console
It must contain at least  uppercase English alphabet characters.
It must contain at least  digits ( - ).
It should only contain alphanumeric characters ( - ,  -  &  - ).
No character should repeat.
There must be exactly 10 characters in a valid UID.
```

Input Format

The first line contains an integer , the number of test cases.
The next  lines contains an employee's UID.

Output Format

For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.

Sample Input

2
B1CD102354
B1CDEF2354
Sample Output

Invalid
Valid
Explanation

B1CD102354:  is repeating → Invalid
B1CDEF2354: Valid

## Solution1 : Using Loops

```python
def check_valid(inp_str):
  if (len(inp_str) != 10) or (len(set(inp_str)) != len(inp_str) or (not(inp_str.isalnum()):
    return "invalid"
  num_count = 0
  upper_count = 0
  for i in inp_str:
    if i.isupper():
      upper_count += 1
    if i.isdigit():
      num_count += 1
  if num_count >= 3 and upper_count >= 2:
    return "valid
  return "invalid"
```

##Solution2 : Using Regex
```
pattern = r'^(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})(?!.*(.).*\1)[A-Za-z0-9]{10}$'
```

^ → Start of the string
(?=(?:.*[A-Z]){2,}) → Ensures at least 2 uppercase letters
(?=(?:.*\d){3,}) → Ensures at least 3 digits
(?!.*(.).*\1) → Ensures all characters are unique (negative lookahead for duplicates)
[A-Za-z0-9]{10} → Ensures exactly 10 alphanumeric characters
$ → End of the string

### 1. (?=...) → Positive Lookahead
A lookahead (?=...) ensures that a certain pattern exists ahead in the string without consuming characters.
This means the pattern must be found, but it does not actually match as part of the final result.
### 2. (?: ... ) → Non-Capturing Group
The (?: ... ) creates a group but does not capture it for back-referencing.
This is used to group patterns while improving efficiency.
### 3. .*[A-Z] → Match Any Characters Followed by an Uppercase Letter
.* → Matches any number of characters (including zero) before an uppercase letter.
[A-Z] → Ensures at least one uppercase letter appears somewhere.
### 4. {2,} → At Least 2 Occurrences
{2,} means that the entire non-capturing group (.*[A-Z]) must occur at least 2 times.
This ensures there are at least 2 uppercase letters in the string.
