
#-------------------------------------- Guided Task Functions

def calculate_subtotal(price, quantity):
    return price * quantity


def calculate_discount(discount_percentage, subtotal):
    return (discount_percentage / 100) * subtotal


def calculate_total(subtotal, discount):
    return subtotal - discount


def print_details(productName, price, quantity, subtotal, discount, total):
    print("Product Name: ", productName)
    print("Price: ", price)
    print("Quantity: ", quantity)
    print("Subtotal: ", subtotal)
    print("Discount: ", discount)
    print("Total: ", total)

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
    # Guided Lab Task
    product_name = input("Enter your product name: ")
    product_price = int(input("Enter your product price: "))
    product_quantity = int(input("Enter your Quantity: "))

    subtotal = calculate_subtotal(product_price, product_quantity)
    discount = calculate_discount(10, subtotal)
    total = calculate_total(subtotal, discount)

    print_details(product_name, product_price, product_quantity, subtotal, discount, total)

    # Challenge Task

    employee_name = input("Enter your Name: ")
    employee_basic_salary = float(input("Enter your basic salary: "))
    employee_allowance = float(input("Enter your allowance: "))
    tax_rate = float(input("Enter your tax rate: "))

    gross_salary = calculate_gross_salary(basic_salary=employee_basic_salary, allowance=employee_allowance)
    total_tax = calculate_tax(tax_rate=tax_rate, gross_salary=gross_salary)
    net_salary = calculate_net_salary(gross_salary=gross_salary, total_tax=total_tax)

    print_employee_salary(name=employee_name, basic_salary=employee_basic_salary, allowance=employee_allowance,
                          gross_salary=gross_salary, total_tax=total_tax, net_salary=net_salary)
