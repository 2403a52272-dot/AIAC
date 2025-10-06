operation = "multiply"
a, b = 5, 3
operations = {
    "add": a + b,
    "subtract": a - b,
    "multiply": a * b
}
result = operations.get(operation, None)
print(result)