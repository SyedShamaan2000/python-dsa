import time


# Custom time decorator to measure the execution time of a function
def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate the execution time
        print(f"Execution time of {func.__name__}: {execution_time:.6f} seconds")
        return result  # Return the result of the original function

    return wrapper


# # Example usage of the time_decorator
# @time_decorator
# def example_function(n):
#     total = 0
#     for i in range(n):
#         total += i
#     return total


# # Call the decorated function
# example_function(1000000)
