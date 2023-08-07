def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."


try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    output = divide_numbers(num1, num2)
    print("Output:", output)
except ValueError:
    print("Invalid input. Please enter valid numbers.")
