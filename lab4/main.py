from students_marks.calculations import calculate_result
from students_marks.display import display_student_result
from students_marks.validation import input_name_and_marks


if "__main__" == __name__:
    (name, marks) = input_name_and_marks(no_of_subjects=3)
    (total, average, grade) = calculate_result(marks=marks)
    display_student_result(name=name, total=total, grade=grade, average=average)
