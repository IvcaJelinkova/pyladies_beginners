def calculate(number1, mark, number2):
    """Returns the result of the math operation. """
    if mark == '-': 
        return(number1 - number2)
    elif mark == '+': 
        return (number1 + number2)
    elif mark == '*': 
        return(number1 * number2)
    elif mark == "/":
        try: 
            result = number1 / number2
            return result
        except ZeroDivisionError:
            print('I cannot divide by zero! ')
    else: 
        return 'Don\'t know this operation! '


def input_validation(query): 
    """Validates query, if the input is text or symbol it will ask again. If the input is number, returns the number. """
    while True: 
        input_result = input(query)
        try: 
            input_number = int(input_result)
            return input_number
        except ValueError: 
            print(f'{input_result} is not a number. Please, try again. ')


print('Hello, welcome to calculater!\n')
number1 = input_validation('Enter the first number: ')
mark = '0'
while True: 
    available_mark = '+-*/'
    if not mark in available_mark: 
        mark = input('Enter operator (+, -, *, /): ')
    else:
        break
number2 = input_validation('Enter the second number: ')

print(number1, mark, number2, '=', calculate(number1, mark, number2))