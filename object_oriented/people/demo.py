from person import Person, Student


def main():
    print(Person())
    student = Student(ID="1717", name="Jack", age=22, height="1.77 m",
                      weight=200, major="Computer Science", GPA=3.6)
    same_student = Student(ID="1717", name="Jack", age=22, height="1.77 m",
                           weight=200, major="Computer Science", GPA=3.6)
    print(student)
    print("Same student ID:", student == same_student)


if __name__ == "__main__":
    main()
