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

Breakdown:
M{0,3} → Matches 0 to 3 M's (1000, 2000, 3000).
(CM|CD|D?C{0,3}) → Matches:
CM → 900
CD → 400
D?C{0,3} → Up to 300 (D = 500, C = 100).
(XC|XL|L?X{0,3}) → Matches:
XC → 90
XL → 40
L?X{0,3} → Up to 30 (L = 50, X = 10).
(IX|IV|V?I{0,3}) → Matches:
IX → 9
IV → 4
V?I{0,3} → Up to 3 (V = 5, I = 1).
This ensures that the given string follows standard Roman numeral rules.

Understanding D?C{0,3}
This part of the regex handles numbers between 100 and 900:

D? → D (500) is optional.
C{0,3} → C (100) can appear 0 to 3 times.
Examples:
Roman	Meaning	Valid?
C	100	✅ Yes
CC	200	✅ Yes
CCC	300	✅ Yes
D	500	✅ Yes
DC	600	✅ Yes
DCC	700	✅ Yes
DCCC	800	✅ Yes
CD	400	❌ Not matched here (handled elsewhere)
DCCCC	900	❌ Invalid (should be CM)
Subtractive Notation: CM and CD
CM (900) → 1000 (M) - 100 (C) = 900
CD (400) → 500 (D) - 100 (C) = 400
These are examples of subtractive notation, where a smaller numeral before a larger numeral means subtraction.

Valid Range of Roman Numerals
In standard Roman numerals, numbers typically range from 1 to 3999. This is why:

M{0,3} allows at most 3 M’s.
Numbers above 3999 require special overline notation (not covered in this regex).
