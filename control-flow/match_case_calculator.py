num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
result = 0

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 == 0:
            result = "Cannot divide by zero."
        else:
            result = num1 / num2
    case _:
        result = "Invalid operation"

if  result == "Cannot divide by zero." or  result == "Invalid operation":
    print(result)
else:
    print(f"The result is {result}.")
