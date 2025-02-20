import time

# Logging decorator
def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Starting function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Ending function: {func.__name__}")
        return result
    return wrapper

# Timing decorator
def time_execution(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# Exception handling decorator
def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    return wrapper

# Combining all decorators
@log_function
@time_execution
@handle_exceptions
def complex_function(n):
    if n < 0:
        raise ValueError("Input must be a positive number!")
    result = 0
    for i in range(n):
        result += i
    return result

# Calling the decorated function
print(complex_function(5))
print(complex_function(-5))  # This will raise an exception
