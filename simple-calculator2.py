num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operator = input("Enter an operator: ")

if operator == '+':
  result = num1 + num2
elif operator == '-':
  result = num1 - num2
elif operator == '*' or operator == "x":
  result = num1 * num2
elif operator == '/' or operator == '÷':
  result = num1 / num2

print(f"The answer is: {result}")