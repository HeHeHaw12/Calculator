print('''Calculator
Use the symbol '+' for addition
Use the symbol '-' for subtraction
Use the symbol '*' for multiplication
Use the symbol '/' for division
Use the symbol '**' for exponent
Use the symbol '%' for a percentage
''')

first_number = (float(input("enter your first number: ")))
operator = input("enter your arithmetic operator: ")

if operator == "+":
    second_number = (float(input("enter your second number: ")))
    print(first_number + second_number)

elif operator == "-":
    second_number = (float(input("enter your second number: ")))
    print(first_number - second_number)

elif operator == "*":
    second_number = (float(input("enter your second number: ")))
    print(first_number * second_number)

elif operator == "/":
    second_number = (float(input("enter your second number: ")))
    print(first_number / second_number)

elif operator == "**":
    second_number = (float(input("enter your second number: ")))
    print(first_number ** second_number)

elif operator == "%":
    print(first_number * 0.01)

else:
    print(" Error: Please type a mathematical symbol.")