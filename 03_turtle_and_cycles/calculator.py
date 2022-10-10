def calculate(number1, mark, number2):
    if mark == '-': 
        return(number1 - number2)
    elif mark == '+': 
        return (number1 + number2)
    elif mark == '*': 
        return(number1 * number2)
    elif mark == "/":
        return(number1 / number2)
    else: 
        return 'Don\'t know this operation! '

number1 = float(input('Hello, welcome to calculater \n Enter first number: '))
mark = input('Enter operator (+, -, *, /): ')
number2 = float(input('Hello, welcome to calculater, enter first number: '))

print(number1, mark, number2, '=', calculate(number1, mark, number2))