def perform_operation(num1, num2, operation):
        if operation == "add":
            return num1 + num2
        if operation == "subtract":
            return num1 - num2
        if operation == "multiply":
            return num1 * num2
        if operation == "divide":
            return num1 / num2 if num2 != 0 else "Cannot divide by zero"
        if operation == _:
            return "Invalid operation"