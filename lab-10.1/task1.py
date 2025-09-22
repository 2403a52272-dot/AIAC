# Corrected and runnable Python code with explanations of the fixes.

# Calculate average score of a student
def calc_average(marks):
    # Initialize total to 0
    total = 0
    # Sum all marks
    for m in marks:
        total += m
    # Calculate average
    average = total / len(marks)
    return average  # Fixed typo: 'avrage' to 'average'

marks = [85, 90, 78, 92]
# Added missing parenthesis to print function
print("Average Score is", calc_average(marks))
