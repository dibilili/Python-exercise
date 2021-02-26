#Calcualtor


#Add
def add(n1, n2):
    return n1 + n2


#Subtract
def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

num1 = int(input('What` the first numer? : '))

num2 = int(input('What` the second numer? : '))

for symbol in operations:
    print(symbol)

operation_symbol = input('Pick an operation from the line above: ')

calculation_function = operations[operation_symbol]

answer = calculation_function(num1, num2)

print(f'{num1}{operation_symbol}{num2} = {answer}')
