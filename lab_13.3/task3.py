class Student:
    """Represents a student with personal details and marks."""

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def total_marks(self):
        return sum(self.marks)


def main():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    marks = []
    for i in range(3):
        mark = int(input(f"Enter mark {i+1}: "))
        marks.append(mark)

    student = Student(name, age, marks)
    student.show_details()
    print("Total Marks:", student.total_marks())


if __name__ == "__main__":
    main()
