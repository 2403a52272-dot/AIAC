def calculate_percentage(value, percentage):
    """
    Calculate the percentage of a given value.

    Parameters:
    value (float or int): The base value.
    percentage (float or int): The percentage to calculate.

    Returns:
    float: The calculated percentage of the value.
    """
    return value * percentage / 100

base_amount = 200  # The base value to calculate the percentage from
percentage_value = 15  # The percentage to calculate

# Calculate and print the result
print(calculate_percentage(base_amount, percentage_value))
#generate 5 test cases above function
print(calculate_percentage(100, 10))
print(calculate_percentage(200, 20))
print(calculate_percentage(300, 30))