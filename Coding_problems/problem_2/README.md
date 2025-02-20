# Hackerrank problem

For this challenge, you are given two complex numbers, and you have to print the result of their addition, subtraction, multiplication, division and modulus operations.

The real and imaginary precision part should be correct up to two decimal places.

Input Format

One line of input: The real and imaginary part of a number separated by a space.

Output Format

For two complex numbers  and , the output should be in the following sequence on separate lines:


For complex numbers with non-zero real and complex part, the output should be in the following format:

Replace the plus symbol  with a minus symbol  when .

For complex numbers with a zero complex part i.e. real numbers, the output should be:

For complex numbers where the real part is zero and the complex part is non-zero, the output should be:

Sample Input

2 1
5 6
Sample Output

7.00+7.00i
-3.00-5.00i
4.00+17.00i
0.26-0.11i
2.24+0.00i
7.81+0.00i
Concept

Python is a fully object-oriented language like C++, Java, etc. For reading about classes, refer here.

Methods with a double underscore before and after their name are considered as built-in methods. They are used by interpreters and are generally used in the implementation of overloaded operators or other built-in functionality.

__add__-> Can be overloaded for + operation

__sub__ -> Can be overloaded for - operation

__mul__ -> Can be overloaded for * operation

# Solution 

Explanation of the Code
This Python class, Complex, implements basic arithmetic operations for complex numbers, including addition, subtraction, multiplication, division, and modulus. It also includes a string representation method for displaying complex numbers in a formatted way.

## Constructor (__init__ Method)

def __init__(self, real, imaginary):
    self.real = real
    self.imaginary = imaginary
This initializes a complex number with a real part (self.real) and an imaginary part (self.imaginary).
self refers to the instance of the class, allowing each object to have its own real and imaginary values.


## Addition (__add__ Method)

def __add__(self, no):
    return Complex(self.real + no.real, self.imaginary + no.imaginary)
Adds two complex numbers by separately adding their real and imaginary parts.
Returns a new Complex object with the computed values.


## Subtraction (__sub__ Method)

def __sub__(self, no):
    return Complex(self.real - no.real, self.imaginary - no.imaginary)
Subtracts two complex numbers by separately subtracting their real and imaginary parts.


## Multiplication (__mul__ Method)

def __mul__(self, no):
    real_part = self.real * no.real - self.imaginary * no.imaginary
    imaginary_part = self.real * no.imaginary + self.imaginary * no.real
    return Complex(real_part, imaginary_part)
Uses the distributive property:
(a+bi)×(c+di)=(ac−bd)+(ad+bc)i
The real part is computed as ac−bd, and the imaginary part as ad+bc.


5. Division (__truediv__ Method)

def __truediv__(self, no):
    denominator = no.real**2 + no.imaginary**2
    real_part = (self.real * no.real + self.imaginary * no.imaginary) / denominator
    imaginary_part = (self.imaginary * no.real - self.real * no.imaginary) / denominator
    return Complex(real_part, imaginary_part)
Uses the formula: (c+di) * (a+bi) = (ac+bd)+(bc−ad)i
​
 The denominator is computed as (c**2 + d**2) to normalize the division.

6. Modulus (mod Method)

def mod(self):
    return Complex((self.real**2 + self.imaginary**2) ** 0.5, 0)
The modulus (or magnitude) of a complex number a+bi is: ∣a+bi∣ = sqrt(a**2 + b**2)

Returns a new Complex object with the magnitude as the real part and 0 as the imaginary part.


7. String Representation (__str__ Method)

def __str__(self):
    if self.imaginary == 0:
        result = "%.2f+0.00i" % (self.real)
    elif self.real == 0:
        if self.imaginary >= 0:
            result = "0.00+%.2fi" % (self.imaginary)
        else:
            result = "0.00-%.2fi" % (abs(self.imaginary))
    elif self.imaginary > 0:
        result = "%.2f+%.2fi" % (self.real, self.imaginary)
    else:
        result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
    return result
This ensures proper formatting of the complex number:
3+4i → "3.00+4.00i"
-3-4i → "-3.00-4.00i"
Handles edge cases where the real or imaginary part is zero.
