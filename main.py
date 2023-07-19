
def template_operation(_operation):
    if operation == "+":
        return lambda _number1, _number2: f"{_number1} + {_number2} = {_number1 + _number2}"
    elif operation == "-":
        return lambda _number1, _number2: f"{_number1} - {_number2} = {_number1 - _number2}"
    elif operation == "*":
        return lambda _number1, _number2: f"{_number1} * {_number2} = {_number1 * _number2}"
    elif operation == "/":
        return lambda _number1, _number2: f"{_number1} / {_number2} = {_number1 / _number2}"
    elif operation == "//":
        return lambda _number1, _number2: f"{_number1} // {_number2} = {_number1 // _number2}"
    elif operation == "%":
        return lambda _number1, _number2: f"{_number1} % {_number2} = {_number1 % _number2}"
    elif operation == "**":
        return lambda _number1, _number2: f"{_number1} ** {_number2} = {_number1 ** _number2}"
    else:
        return lambda _number1, _number2: f"{_number1} {operation} {_number2} = ?"

operation = input("Enter operation(+, -, *, /, //, %, **): ")
func_calc = template_operation(operation)

number1 = int(input('Enter number1: '))
number2 = int(input('Enter number2: '))

result = func_calc(number1, number2)
print(result)

