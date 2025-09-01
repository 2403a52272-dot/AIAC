class Student:
    """
    A class to represent a student.

    Attributes:
    - name (str): The name of the student.
    - roll_no (int): The student's roll number.
    - marks (float): The student's marks.
    """
    def __init__(self, name, roll_no, marks):
        """
        Initializes the Student object with name, roll number, and marks.
        """
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_details(self):
        """
        Displays the student's details.
        """
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")

    def calculate_grade(self):
        """
        Calculates and returns the grade based on marks.
        """
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 75:
            return 'B'
        elif self.marks >= 60:
            return 'C'
        else:
            return 'Fail'

# Example Usage:
# Creating a Student object
student1 = Student("pranith", 101, 88)

# Displaying details
student1.display_details()
# Expected output:
# Name: Alice
# Roll No: 101
# Marks: 88

# Calculating and printing grade
print(f"Grade: {student1.calculate_grade()}")
# Expected output:
# Grade: B