def isValid(s: str) -> bool:
    # Initialize an empty stack
    stack = []
    
    # Define a dictionary to map closing parentheses to their corresponding opening parentheses
    parentheses_map = {')': '(', '}': '{', ']': '['}
    
    # Iterate through each character in the string
    for char in s:
        # If the character is a closing parenthesis, check if it matches the top of the stack
        if char in parentheses_map:
            # Pop the top element from the stack if it's non-empty, otherwise assign a dummy value
            top_element = stack.pop() if stack else '#'
            
            # If the top element doesn't match the corresponding opening parenthesis, return False
            if parentheses_map[char] != top_element:
                return False
        else:
            # If the character is an opening parenthesis, push it onto the stack
            stack.append(char)
    
    # If the stack is empty, all parentheses were properly matched, return True
    return not stack

# Example Usage
print(isValid("()"))       # Output: True
print(isValid("()[]{}"))   # Output: True
print(isValid("(]"))       # Output: False
print(isValid("([)]"))     # Output: False
print(isValid("{[]}"))     # Output: True
