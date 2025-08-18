def factorial(n):
    """
    Calculate the factorial of a non-negative integer n
    Factorial: n! = n × (n-1) × (n-2) × ... × 2 × 1
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        int: Factorial of n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    """
    Recursive implementation of factorial function
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        int: Factorial of n
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    
    return n * factorial_recursive(n - 1)

def factorial_math(n):
    """
    Using Python's built-in math.factorial() function
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        int: Factorial of n
    """
    import math
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return math.factorial(n)

# Test the factorial function
if __name__ == "__main__":
    # Test cases
    test_numbers = [0, 1, 5, 10]
    
    print("FACTORIAL FUNCTION TESTING")
    print("=" * 40)
    
    for num in test_numbers:
        try:
            result = factorial(num)
            print(f"{num}! = {result}")
        except Exception as e:
            print(f"Error calculating {num}!: {e}")
    
    print("\n" + "=" * 40)
    print("INTERACTIVE FACTORIAL CALCULATOR")
    print("=" * 40)
    
    # Interactive input
    try:
        user_input = int(input("Enter a number to calculate factorial: "))
        if user_input < 0:
            print("Please enter a non-negative number.")
        else:
            result = factorial(user_input)
            print(f"{user_input}! = {result}")
    except ValueError:
        print("Please enter a valid integer.")
    except Exception as e:
        print(f"An error occurred: {e}")
