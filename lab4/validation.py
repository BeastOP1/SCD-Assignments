def validate_mark(mark):
    if mark < 0 or mark > 100:
        return True
    else:
        return False

def validate_grade(average):
    grade = ""
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    return grade


def input_name():
    return input("Enter student name: ")


def input_marks(no_of_subjects):
    marks = []
    for i in range(no_of_subjects):  ##input
        mark = float(input(f"Enter marks for subject {i + 1}: "))

        while validate_mark(mark):
            print("Invalid marks. Enter 0-100.")
            mark = float(input(f"Enter marks for subject {i + 1}: "))

        marks.append(mark)

    return marks


def input_name_and_marks(no_of_subjects):
    name = input_name()
    marks = input_marks(no_of_subjects)
    return name, marks
