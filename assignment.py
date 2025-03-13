
# Taking user input
num1= float(input("Enter first number: "))
operator = input("Enter operation (+,-,*,/): ")
num2= float(input("Entyer second number: "))

# performing the calculation based on the operator
if operator== '+':
    result=num1 + num2
    print(f"{num1} {operator} {num2} = {result}")
elif operator == '-':
      result= num1 - num2
      print(f"{num1} {operator} {num2} = {result}")
elif operator == '*':
     result= num1 * num2
     print(f"{num1} {operator} {num2} = {result}")
elif operator =='/':
     result =num1 / num2 if num2 != 0 else "Error! Division by zero."
else:
     result= "Invalid operator!"
     print(f"{num1} {operator} {num2} = {result}")