def welcome_student(name): # function to welcome a student
    """
    Prints a welcome message for the given student name.

    Parameters:
    name (str): The name of the student to welcome.
    """
    print("Welcome", name)# print the welcome message
students = ["Alice", "Bob", "Charlie"] # list of students
for student in students:
    welcome_student(student)# call the function to welcome the student
