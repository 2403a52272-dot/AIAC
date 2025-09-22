def grade(score):
    """
    Returns the letter grade for a given numeric score.

    Parameters:
    score (int or float): The numeric score to grade.

    Returns:
    str: The letter grade ("A", "B", "C", "D", or "F").
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

score_input = int(input("Enter the score: "))
print("The grade is", grade(score_input))
