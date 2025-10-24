def f(x):
    return x ** 2 - 4 * x + 5

def df(x):
    return 2 * x - 4

def gradient_descent(lr=0.01, epochs=1000, x_init=0.0, tolerance=1e-6):
    x = x_init
    for i in range(epochs):
        grad = df(x)
        x_new = x - lr * grad
        if abs(x_new - x) < tolerance:
            break
        x = x_new
    return x

if __name__ == "__main__":
    x_min = gradient_descent(lr=0.01, epochs=10000, x_init=0.0)
    print(f"Approximate minimum at x = {x_min}")
    print(f"Minimum value f(x) = {f(x_min)}")
    print(f"Analytical minimum should be at x = 2 (f'(x) = 2x - 4 = 0 when x = 2)")
