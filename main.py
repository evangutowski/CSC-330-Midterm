from flask import Flask
import random

app=Flask(__name__)

@app.route('/')
def greeting():
    return '<h1>This is a calculator using routes.</h1>'

@app.route('/add/<num1>/<num2>')
def add_nums(num1,num2):
    return f'<h1>Sum of {num1} and {num2} is {str(int(num1)+int(num2))}</h1>'

@app.route('/subtract/<num1>/<num2>')
def subtract_nums(num1,num2):
    return f'<h1>{num1} subtracted by {num2} is {str(int(num1)-int(num2))}</h1>'

@app.route('/multiply/<num1>/<num2>')
def multiply_nums(num1,num2):
    return f'<h1>{num1} multiplied by {num2} is {str(int(num1)*int(num2))}</h1>'

@app.route('/divide/<num1>/<num2>')
def divide_nums(num1,num2):
    return f'<h1>{num1} divided by {num2} is {str(int(num1)/int(num2))}</h1>'
