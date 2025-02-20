class Example:
    def __init__(self, value):
        self.value = value

    # Arithmetic Operators
    def __add__(self, other):
        return Example(self.value + other.value)
    
    def __sub__(self, other):
        return Example(self.value - other.value)
    
    def __mul__(self, other):
        return Example(self.value * other.value)
    
    def __truediv__(self, other):
        return Example(self.value / other.value)
    
    # Comparison Operators
    def __eq__(self, other):
        return self.value == other.value
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __le__(self, other):
        return self.value <= other.value
    
    # String Representation
    def __str__(self):
        return f"Example({self.value})"
    
    def __repr__(self):
        return f"Example({self.value})"
    
    # Length
    def __len__(self):
        return abs(self.value)
    
    # Call method
    def __call__(self, x):
        return self.value + x
    
    # Indexing
    def __getitem__(self, index):
        return str(self.value)[index]
    
    # Iteration
    def __iter__(self):
        return iter(str(self.value))

# Example usage
e1 = Example(10)
e2 = Example(5)

print(e1 + e2)  # __add__
print(e1 - e2)  # __sub__
print(e1 * e2)  # __mul__
print(e1 / e2)  # __truediv__
print(e1 == e2)  # __eq__
print(e1 < e2)  # __lt__
print(len(e1))  # __len__
print(e1(5))  # __call__
print(e1[0])  # __getitem__
for char in e1:  # __iter__
    print(char)
