class SRU_Student:
    def __init__(self, name, roll_no, department):
        self.name = name
        self.roll_no = roll_no
        self.department = department

    def Student_Data(self, filename):
        with open(filename, 'w') as file:
            file.write(f"Name: {self.name}\n")
            file.write(f"Roll No: {self.roll_no}\n")
            file.write(f"Department: {self.department}\n")

# Example usage:
if __name__ == "__main__":
    student = SRU_Student("Alice", "2272", "Computer Science")
    student.Student_Data("student_details.txt")
    with open("student_details.txt", "r") as file:
        print(file.read())