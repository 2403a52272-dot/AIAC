def factorial(n):
    if not isinstance(n, int):
        raise TypeError("factorial() only accepts integers")
    if n < 0:
        raise ValueError("factorial() not defined for negative numbers")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


print(factorial(5))
