# Python Decorators 🐍

## 🔹 What is a Decorator?
A **decorator** in Python is a function that modifies the behavior of another function or class **without modifying its code**. Decorators are useful for:

✅ Logging 📜  
✅ Authentication 🔑  
✅ Performance measurement ⏳  
✅ Access control 🔐  
✅ Caching 🚀  

---

## 🔹 How Do Decorators Work?

A decorator is a function that **wraps another function** to modify its behavior:

```python
# Basic decorator

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"Wrapper executed before {original_function.__name__}")
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function  # Applying decorator
def say_hello():
    print("Hello!")

say_hello()
```

🔹 **Output:**
```
Wrapper executed before say_hello
Hello!
```

---

## 🔹 Types of Decorators

### **1️⃣ Function Decorators**
```python
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def greet():
    return "hello, world"

print(greet())  # Output: "HELLO, WORLD"
```

---

### **2️⃣ Decorators with Arguments**
```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello!")

greet()  # Executes greet() 3 times
```

---

### **3️⃣ Class Decorators**
```python
class Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Calling {self.func.__name__}")
        return self.func(*args, **kwargs)

@Logger
def display():
    print("Executing function!")

display()
```

---

### **4️⃣ Built-in Decorators**
Python provides built-in decorators like:

| Decorator | Description |
|-----------|-------------|
| `@staticmethod` | Defines a static method inside a class (no `self` or `cls` needed). |
| `@classmethod` | Defines a class method that receives `cls` as the first argument. |
| `@property` | Allows method-like access to attributes. |

```python
class Example:
    _value = 10

    @classmethod
    def get_value(cls):
        return cls._value

    @staticmethod
    def info():
        print("This is a static method.")

print(Example.get_value())  # Class method
Example.info()  # Static method
```

---

## 🔹 When to Use Decorators?
✅ **Logging**: Track function calls.  
✅ **Access Control**: Restrict function execution.  
✅ **Performance Timing**: Measure function execution time.  
✅ **Caching**: Store results to improve efficiency.  
✅ **Validation**: Ensure inputs are valid.  

🚀 **Happy Coding!** 🚀
