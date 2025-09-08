def fibonacci(n):
    """
    Recursively calculates the nth Fibonacci number.

    The Fibonacci sequence is defined as:
    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2) for n > 1

    Args:
        n (int): The position in the Fibonacci sequence (n >= 0).

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0  # Base case: F(0) = 0
    elif n == 1:
        return 1  # Base case: F(1) = 1
    else:
        # Recursive case: sum of previous two Fibonacci numbers
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage:
print(fibonacci(6))  # Output: 8

"""
Explanation:
-------------
This function calculates the nth Fibonacci number using recursion.
- The base cases are when n is 0 or 1, returning 0 and 1 respectively.
- For n > 1, the function calls itself with (n-1) and (n-2) and adds the results.
- The recursion continues until it reaches the base cases.
- The function raises an error if a negative number is provided.

Assessment:
-------------
The explanation is clear and correct. It describes the recursive approach, base cases, and error handling.
"""