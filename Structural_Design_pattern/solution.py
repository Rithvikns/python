"""
Structural Design Patterns in Python

This script demonstrates various structural design patterns, including:
- Adapter
- Bridge
- Composite
- Decorator
- Facade
- Flyweight
- Proxy

Each pattern includes a simple implementation example.
"""

# Adapter Pattern
class EuropeanPlug:
    def connect_to_european_socket(self):
        return "Connected to European socket"

class Adapter:
    def __init__(self, plug):
        self.plug = plug

    def connect_to_us_socket(self):
        return self.plug.connect_to_european_socket() + " via Adapter"

# Bridge Pattern
class Device:
    def __init__(self, implementation):
        self.implementation = implementation
    
    def operate(self):
        return self.implementation.run()

class TV:
    def run(self):
        return "TV is running"

# Composite Pattern
class Component:
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        return "Leaf"

class Composite(Component):
    def __init__(self):
        self.children = []
    
    def add(self, component):
        self.children.append(component)
    
    def operation(self):
        return " + ".join(child.operation() for child in self.children)

# Decorator Pattern
class Coffee:
    def cost(self):
        return 5

class MilkDecorator:
    def __init__(self, coffee):
        self.coffee = coffee
    
    def cost(self):
        return self.coffee.cost() + 2

# Facade Pattern
class SubsystemA:
    def operation_a(self):
        return "A operation"

class SubsystemB:
    def operation_b(self):
        return "B operation"

class Facade:
    def __init__(self):
        self.sub_a = SubsystemA()
        self.sub_b = SubsystemB()
    
    def operation(self):
        return f"{self.sub_a.operation_a()} and {self.sub_b.operation_b()}"

# Flyweight Pattern
class Flyweight:
    _shared_state = {}
    
    def __init__(self, state):
        self._state = self._shared_state.setdefault(state, state)
    
    def get_state(self):
        return self._state

# Proxy Pattern
class RealSubject:
    def request(self):
        return "RealSubject request"

class Proxy:
    def __init__(self, real_subject):
        self.real_subject = real_subject
    
    def request(self):
        return "Proxy: " + self.real_subject.request()

# Example usage
if __name__ == "__main__":
    # Adapter
    plug = EuropeanPlug()
    adapter = Adapter(plug)
    print(adapter.connect_to_us_socket())
    
    # Bridge
    device = Device(TV())
    print(device.operate())
    
    # Composite
    leaf1 = Leaf()
    leaf2 = Leaf()
    composite = Composite()
    composite.add(leaf1)
    composite.add(leaf2)
    print(composite.operation())
    
    # Decorator
    coffee = Coffee()
    milk_coffee = MilkDecorator(coffee)
    print(milk_coffee.cost())
    
    # Facade
    facade = Facade()
    print(facade.operation())
    
    # Flyweight
    flyweight1 = Flyweight("shared")
    flyweight2 = Flyweight("shared")
    print(flyweight1.get_state() == flyweight2.get_state())  # True
    
    # Proxy
    real_subject = RealSubject()
    proxy = Proxy(real_subject)
    print(proxy.request())
