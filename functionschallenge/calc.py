#! python3

def calculate( a, b, op ):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b



def tryCalculate():
    try:
        input_a = float(input('Please enter the first number: '))
        input_b = float(input('Please enter the second number: '))
        input_op = input('Please enter the operator (+, -, *, or /): ')
        while input_op != '+' and input_op != '-' and input_op != '*' and input_op != '/':
            input_op = ('Input a valid operator (+, -, *, or /): ')
        print(calculate(input_a, input_b, input_op))
    except:
        input_a = input('Ender a valid first number: ')
        input_b = input('Enter a valid second number: ')
        tryCalculate()

tryCalculate()