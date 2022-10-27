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


def input_validation(query): 
    """Validates, if the input is not a text or symbol. """
    while True: 
        input_result = input(query)
        try: 
            input_number = int(input_result)
            return input_number
        except ValueError: 
            print(f'{input_result} is not a number. Please, try again. ')


print('Hello, welcome to calculater!\n')
number1 = input_validation('Enter the first number: ')
mark = input('Enter operator (+, -, *, /): ')
number2 = input_validation('Enter the second number: ')

print(number1, mark, number2, '=', calculate(number1, mark, number2))