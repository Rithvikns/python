# Roman Numeral Validation and Regular Expression Explanation

## Roman Numeral System

Roman numerals use specific letters to represent numbers:

| Roman | Value  |
|--------|--------|
| **I**  | 1      |
| **V**  | 5      |
| **X**  | 10     |
| **L**  | 50     |
| **C**  | 100    |
| **D**  | 500    |
| **M**  | 1000   |

## Explanation of the Regular Expression for Valid Roman Numerals

The following regular expression is used to validate a Roman numeral:

```regex
^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$

