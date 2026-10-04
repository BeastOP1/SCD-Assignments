from array import ArrayType

from students_marks.validation import validate_grade


def calculate_average(marks: ArrayType[int]):
    average = calculate_total(marks) / len(marks)
    return average

def calculate_total(marks: ArrayType[int]):
    return sum(marks)

def calculate_result(marks: ArrayType[int]):
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade =validate_grade(average=average)
    return total, average,grade