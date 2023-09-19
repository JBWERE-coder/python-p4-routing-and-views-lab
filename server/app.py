#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string_param>')
def print_string(string_param):
    print(string_param)
    return f'<h2>Printed String: {string_param}</h2>'

@app.route('/count/<int_param>')
def count(int_param):
    numbers = '\n'.join(map(str, range(int_param)))
    return f'<h2>Counted Numbers:<br>{numbers}</h2>'

@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return '<h2>Error: Division by zero</h2>'
    elif operation == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            return '<h2>Error: Modulo by zero</h2>'
    else:
        return '<h2>Error: Invalid operation</h2>'
    
    return f'<h2>Result of {num1} {operation} {num2} is {result}</h2>'
