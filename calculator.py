#calc by james
import operator
import ast
import time
from typing import Any

operator_dict = {"+": operator.add, 
                 "-": operator.sub, 
                 "*": operator.mul,
                 "/": operator.truediv
                 }

while True:
    print("Enter your first operand.")
    isRight = True
    try:
        a = float(input(''))
    except ValueError as err:
        print("The value listed cannot be parsed: ", err)
        isRight = False 
    if isRight == True: # if passed as True then go
        print("Enter the operator.")
        try:
            op = input('')
            if op in operator_dict: # last check
                isRight = True
            else:
                print("Incorrect operator. Please restart the application.")
                isRight = False
                time.sleep(10) #close if they dont do anything, i cba
                break
        except ValueError as err:
            print("The value listed cannot be parsed: ", err)
        print("Enter your second operand.")
        try:
            b = float(input(''))
        except ValueError as err:
            print("The value listed cannot be parsed: ", err)
            isRight = False
        result = operator_dict[op](a,b)
        print(a, op, b, "=", result)
            
    else:
        print("") # if they begin off with an incorrect input restart