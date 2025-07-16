# operations.py
from calculatorLab.utils import log_call;

@log_call
def add(a, b):
    return a + b; 

@log_call
def sub(a, b):
    return a - b; 

@log_call
def mul(a, b):
    return a * b; 

@log_call
def div(a, b):
    if b == 0:
        return "undefined";
    else:
        return a / b;