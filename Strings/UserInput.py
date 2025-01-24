 # input() will always takse an input as a string
# Division result will always be of type float
num1 = int(input("Enter the num1"))
print('Value of num1 is:',num1,'Data Type is:',type(num1))

num2 = int(input("Enter the number1"))
num3 =int(input("Enter the number2"))
sum = num2 + num3
print(f'Addition of {num2} and {num3} is {sum}')
print(f'Subtraction of {num2} and {num3} is {num2 - num3}')
print(f'Multiplication of {num2} and {num3} is {num2 * num3}')
print(f'Division of {num2} and {num3} is {num2 / num3}')