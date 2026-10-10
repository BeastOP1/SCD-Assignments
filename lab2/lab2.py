import array

#-------------------------------------- Guided Task Functions
def calculate_average(total,marks):
    return total/len(marks)

def calculate_grade(average):
    if (average > 80):
        return  "A"
    elif (average > 70):
        return  "B"
    elif (average > 60):
        return "C"
    else:
        return "D"

def write_result(filename, name, grade):

    with open(filename, "a") as file:
        file.write(f'{name},{grade}\n')

def process_student(name:str, marks:array.array[int]):
    total = sum(marks)
    average =calculate_average(total,marks)
    grade = calculate_grade(average)
    print(name,total,average, grade)
    write_result("result.txt", name, grade)

    return  grade

#-----------------------------------------Challenge Task Functions

def calculate_gross_salary(basic_salary, allowance):
    return basic_salary + allowance


def calculate_tax(gross_salary, tax_rate):
    return (tax_rate / 100) * gross_salary


def calculate_net_salary(gross_salary, total_tax):
    return gross_salary - total_tax


def print_employee_salary(name, basic_salary, allowance, gross_salary, total_tax, net_salary):
    print("Name: ", name)
    print("Basic Salary: ", basic_salary)
    print("Allowance: ", allowance)
    print("Gross Salary: ", gross_salary)
    print("Total Tax: ", total_tax)
    print("Net Salary: ", net_salary)


if __name__ == '__main__':
    #Guided Task
    process_student("Hassan",[70,20])


    #Challenge Task
    employee_name = input("Enter your Name: ")
    employee_basic_salary = float(input("Enter your basic salary: "))
    employee_allowance = float(input("Enter your allowance: "))
    tax_rate = float(input("Enter your tax rate: "))

    gross_salary = calculate_gross_salary(basic_salary=employee_basic_salary, allowance=employee_allowance)
    total_tax = calculate_tax(tax_rate=tax_rate, gross_salary=gross_salary)
    net_salary = calculate_net_salary(gross_salary=gross_salary, total_tax=total_tax)

    print_employee_salary(name=employee_name, basic_salary=employee_basic_salary, allowance=employee_allowance,
                          gross_salary=gross_salary, total_tax=total_tax, net_salary=net_salary)





