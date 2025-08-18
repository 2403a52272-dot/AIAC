def factorial(n):
    """
    Calculate the factorial of a given non-negative integer using a loop.

    Args:
        n (int): The number to calculate the factorial for.

    Returns:
        int: The factorial of n.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    try:
        num = int(input("Enter a non-negative integer: "))
        print(f"Factorial of {num} is {factorial(num)}")
    except Exception as e:
        print("Error:", e)
