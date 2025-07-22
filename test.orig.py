def calculate(op, numbers):
    if op == "+":
        result = sum(numbers)
    elif op == "-":
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
    elif op == "*":
        result = 1
        for num in numbers:
            result *= num
    elif op == ":" or op == "/":
        result = numbers[0]
        for num in numbers[1:]:
            if num == 0:
                return "Error: Division by zero"
            result /= num
    else:
        return "Invalid operation"
    
    return round(result, 2)

# --- Main program ---
op = input("choose pls (+,-,* or / )\n")
nums = input("enter the number (seperate it by spaces vro):\n").split()

try:
    numbers = [float(n) for n in nums]
    output = calculate(op, numbers)
    print("Result:", output)
except ValueError:
    print("Please enter valid numbers.")

