# Understanding self
The self keyword in Python is used within a class to refer to the instance of the object itself. It allows methods to access and modify the attributes of the instance.

For example, in the __init__ method:
```console
def __init__(self, real, imaginary):
    self.real = real
    self.imaginary = imaginary
```
self.real refers to the real attribute of the specific instance.
self.imaginary refers to the imaginary attribute.
Similarly, in the __add__ method:
```console
def __add__(self, no):
    return Complex(self.real + no.real, self.imaginary + no.imaginary)
```
self.real refers to the real part of the instance.
no.real refers to the real part of the second complex number being added.
Without self, Python wouldn’t know which instance’s attributes to access, making it essential for class-based object-oriented programming.

# splat operator

The splat operator (*) in Python is used for unpacking iterables and handling variable-length arguments. It comes in two forms: * (single asterisk) and ** (double asterisk). Here’s a breakdown of both:

# Single Asterisk (*)

Used for:

Unpacking iterables (lists, tuples, strings)
Handling variable-length positional arguments in function definitions
Unpacking Iterables
You can use * to unpack elements from a list or tuple:

```console
numbers = [1, 2, 3]
print(*numbers)  # Output: 1 2 3

a, *b, c = [10, 20, 30, 40]
print(a)  # Output: 10
print(b)  # Output: [20, 30]
print(c)  # Output: 40
```
Using * in Function Arguments
You can define functions that accept a variable number of arguments:

```console
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))  # Output: 10
````
Here, args collects all positional arguments into a tuple.

Merging Lists
You can use * to merge lists:

```console
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = [*list1, *list2]
print(merged)  # Output: [1, 2, 3, 4, 5, 6]
```

## Double Asterisk (**)
Used for:

Unpacking dictionaries
Handling variable-length keyword arguments in functions
Unpacking Dictionaries
You can use ** to unpack key-value pairs from a dictionary:

```console
data = {"name": "Alice", "age": 25}
new_data = {**data, "city": "New York"}
print(new_data)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
```
Using ** in Function Arguments
You can define functions that accept any number of keyword arguments:

```console
def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Alice", age=25)  
# Output:
# name: Alice
# age: 25
```
Here, kwargs collects all keyword arguments into a dictionary.

Combining * and **
You can use both in function definitions:

```console
def display(a, b, *args, c=10, **kwargs):
    print(f"a: {a}, b: {b}, args: {args}, c: {c}, kwargs: {kwargs}")

display(1, 2, 3, 4, 5, c=20, d=30, e=40)
# Output:
# a: 1, b: 2, args: (3, 4, 5), c: 20, kwargs: {'d': 30, 'e': 40}
```
Key Takeaways
* (single asterisk) is used for unpacking iterables and handling variable-length positional arguments.
** (double asterisk) is used for unpacking dictionaries and handling variable-length keyword arguments.
Both can be used together for flexible function definitions.


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
```console 
def __init__(self, real, imaginary):
    self.real = real
    self.imaginary = imaginary
```
This initializes a complex number with a real part (self.real) and an imaginary part (self.imaginary).
self refers to the instance of the class, allowing each object to have its own real and imaginary values.


## Addition (__add__ Method)
``` console
def __add__(self, no):
    return Complex(self.real + no.real, self.imaginary + no.imaginary)
```
Adds two complex numbers by separately adding their real and imaginary parts.
Returns a new Complex object with the computed values.


## Subtraction (__sub__ Method)
```console
def __sub__(self, no):
    return Complex(self.real - no.real, self.imaginary - no.imaginary)
```
Subtracts two complex numbers by separately subtracting their real and imaginary parts.


## Multiplication (__mul__ Method)
```console
def __mul__(self, no):
    real_part = self.real * no.real - self.imaginary * no.imaginary
    imaginary_part = self.real * no.imaginary + self.imaginary * no.real
    return Complex(real_part, imaginary_part)
```
Uses the distributive property:
(a+bi)×(c+di)=(ac−bd)+(ad+bc)i
The real part is computed as ac−bd, and the imaginary part as ad+bc.


## Division (__truediv__ Method)
```console
def __truediv__(self, no):
    denominator = no.real**2 + no.imaginary**2
    real_part = (self.real * no.real + self.imaginary * no.imaginary) / denominator
    imaginary_part = (self.imaginary * no.real - self.real * no.imaginary) / denominator
    return Complex(real_part, imaginary_part)
```

Uses the formula: (c+di) * (a+bi) = (ac+bd)+(bc−ad)i
​
 The denominator is computed as (c**2 + d**2) to normalize the division.
 
##. Modulus (mod Method)
```console
def mod(self):
    return Complex((self.real**2 + self.imaginary**2) ** 0.5, 0)
```
The modulus (or magnitude) of a complex number a+bi is: ∣a+bi∣ = sqrt(a**2 + b**2)

Returns a new Complex object with the magnitude as the real part and 0 as the imaginary part.


## String Representation (__str__ Method)
```console
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
```
This ensures proper formatting of the complex number:
3+4i → "3.00+4.00i"
-3-4i → "-3.00-4.00i"
Handles edge cases where the real or imaginary part is zero.

## main function

Breaking Down the Code
```console
c = map(float, input().split())  # Reads input, converts to floats
d = map(float, input().split())  # Reads another input, converts to floats

x = Complex(*c)  # Creates a Complex object from c
y = Complex(*d)  # Creates a Complex object from d

print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
```

Step 1: Reading and Mapping Input
When input().split() is used, it takes user input, splits it into parts (based on spaces), and returns a list of strings.

For example, if the user inputs:

2 3
```console
Then:
input().split()  # → ["2", "3"]
map(float, input().split())  # → [2.0, 3.0] (converted to floats)
So, c = map(float, input().split()) converts "2 3" into map(float, ["2", "3"]), which results in an iterator yielding 2.0 and 3.0.
```
Similarly, d does the same for the second line of input.

Step 2: Unpacking with *c
Now, this line:
```console
x = Complex(*c)
is equivalent to:
x = Complex(2.0, 3.0)  # Unpacking [2.0, 3.0] into the Complex constructor
This means:
self.real = 2.0
self.imaginary = 3.0
Similarly, if the second input was "1 -4", then:
y = Complex(*d)  # Equivalent to Complex(1.0, -4.0)
```


Understanding the Final Print Statement
```console
print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
[x+y, x-y, x*y, x/y, x.mod(), y.mod()] → Performs all operations and stores the results in a list.
map(str, ...) → Converts each result to a string using the __str__ method of Complex.
* (unpacking) → Passes the results as separate arguments to print, instead of as a list.
sep='\n' → Prints each result on a new line.
```
Example Input and Output
Input
2 3
1 -4
Processing
x = Complex(2, 3) (2 + 3i)
y = Complex(1, -4) (1 - 4i)
Compute:
Addition: (2 + 3i) + (1 - 4i) = 3 - 1i
Subtraction: (2 + 3i) - (1 - 4i) = 1 + 7i
Multiplication: (2 + 3i) * (1 - 4i) = 14 + 5i
Division: (2 + 3i) / (1 - 4i) = -0.58 + 0.64i
Modulus of x: √(2² + 3²) = 3.61
Modulus of y: √(1² + (-4)²) = 4.12
