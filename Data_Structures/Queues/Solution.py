from collections import deque

class StackUsingQueues:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
    
    def push(self, x):
        # Push element onto stack
        self.queue1.append(x)
    
    def pop(self):
        # Remove and return the top element
        if self.is_empty():
            return None
        
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        
        top_element = self.queue1.popleft()
        
        self.queue1, self.queue2 = self.queue2, self.queue1
        return top_element
    
    def top(self):
        # Get the top element
        if self.is_empty():
            return None
        
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        
        top_element = self.queue1.popleft()
        self.queue2.append(top_element)
        
        self.queue1, self.queue2 = self.queue2, self.queue1
        return top_element
    
    def is_empty(self):
        # Check if the stack is empty
        return not self.queue1
    
    def size(self):
        # Get the size of the stack
        return len(self.queue1)

# Example usage
if __name__ == "__main__":
    stack = StackUsingQueues()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.top())  # Output: 3
    print(stack.pop())  # Output: 3
    print(stack.top())  # Output: 2
