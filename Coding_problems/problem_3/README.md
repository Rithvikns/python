# Python Dunder (Magic) Methods Guide

## 1️⃣ Arithmetic Operators (Like +, -, *, /)
These are the ones we've already discussed. Python automatically translates them into dunder (double underscore) methods like:

| Operator | Special Method (Dunder Method) |
|----------|-------------------------------|
| +        | `__add__(self, other)`        |
| -        | `__sub__(self, other)`        |
| *        | `__mul__(self, other)`        |
| /        | `__truediv__(self, other)`    |
| //       | `__floordiv__(self, other)`   |
| %        | `__mod__(self, other)`        |
| **       | `__pow__(self, other)`        |

✅ Example: If you write `x * y`, Python actually calls `x.__mul__(y)`.

---

## 2️⃣ Comparison Operators (Like ==, <, >, !=)
Python also translates comparison operations into methods.

| Operator | Special Method |
|----------|---------------|
| ==       | `__eq__(self, other)` |
| !=       | `__ne__(self, other)` |
| <        | `__lt__(self, other)` |
| >        | `__gt__(self, other)` |
| <=       | `__le__(self, other)` |
| >=       | `__ge__(self, other)` |

✅ Example:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __lt__(self, other):  # Defines "less than"
        return self.age < other.age

p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

print(p1 < p2)  # Calls p1.__lt__(p2) → True
```

---

## 3️⃣ String and Object Representation (str, repr)
Python also translates string representations of objects.

| Usage      | Special Method |
|-----------|---------------|
| `str(obj)` | `__str__(self)` (User-friendly string) |
| `repr(obj)` | `__repr__(self)` (Developer-friendly string) |

✅ Example:

```python
class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def __str__(self):  # For print()
        return f"Car Model: {self.model}, Price: ${self.price}"

    def __repr__(self):  # For debugging
        return f"Car('{self.model}', {self.price})"

c = Car("Tesla", 50000)
print(str(c))  # Calls c.__str__() → "Car Model: Tesla, Price: $50000"
print(repr(c))  # Calls c.__repr__() → "Car('Tesla', 50000)"
```

---

## 4️⃣ Indexing and Slicing ([])
If you want objects to behave like lists or dictionaries, you can use:

| Operation | Special Method |
|-----------|---------------|
| `obj[index]` | `__getitem__(self, index)` |
| `obj[index] = value` | `__setitem__(self, index, value)` |
| `del obj[index]` | `__delitem__(self, index)` |

✅ Example:

```python
class CustomList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):  # Enables obj[index]
        return self.data[index]

    def __setitem__(self, index, value):  # Enables obj[index] = value
        self.data[index] = value

cl = CustomList([10, 20, 30])
print(cl[1])  # Calls cl.__getitem__(1) → 20

cl[1] = 99  # Calls cl.__setitem__(1, 99)
print(cl.data)  # [10, 99, 30]
```

---

## 5️⃣ Iteration (For Loops)
Python translates loops like `for item in obj:` into `__iter__()`.

| Operation | Special Method |
|-----------|---------------|
| `for x in obj` | `__iter__(self)` |

✅ Example:

```python
class MyNumbers:
    def __init__(self):
        self.nums = [1, 2, 3]

    def __iter__(self):
        return iter(self.nums)  # Returns an iterator

mn = MyNumbers()
for num in mn:  # Calls mn.__iter__()
    print(num)  # Prints 1, 2, 3
```

---

## 6️⃣ Customizing `len()`, `abs()`, and `call()`
Python also translates built-in functions into methods:

| Function | Special Method |
|----------|---------------|
| `len(obj)` | `__len__(self)` |
| `abs(obj)` | `__abs__(self)` |
| `obj()` | `__call__(self, *args)` |

✅ Example:

```python
class Counter:
    def __init__(self, count):
        self.count = count

    def __len__(self):  # Enables len(obj)
        return self.count

    def __call__(self, x):  # Allows obj() to be called like a function
        return self.count + x

c = Counter(5)
print(len(c))  # Calls c.__len__() → 5
print(c(10))  # Calls c.__call__(10) → 15
```

---

## 🔹 Summary: Python Translates Many Operations!
Python automatically translates many operations using special methods (dunder methods):

✅ Arithmetic: `+`, `-`, `*`, `/` (`__add__`, `__sub__`, `__mul__`, etc.)
✅ Comparisons: `==`, `<`, `>` (`__eq__`, `__lt__`, etc.)
✅ Strings: `str(obj)`, `repr(obj)` (`__str__`, `__repr__`)
✅ Indexing: `obj[index]` (`__getitem__`, `__setitem__`)
✅ Loops: `for x in obj:` (`__iter__`)
✅ Built-ins: `len(obj)`, `abs(obj)`, `obj()` (`__len__`, `__abs__`, `__call__`)

Python does more than just arithmetic—it translates almost every operator using special methods!

Would you like an example of overloading a logical operator like `and` or `or`? 🚀

