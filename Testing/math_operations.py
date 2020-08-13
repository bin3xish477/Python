#!/usr/bin/env python3
def add(a, b):
    """Adds two numbers"""
    return a + b

def subtract(a, b):
    """Subtracts two numbers"""
    return a - b

def multiply(a, b):
    """Multiplies two numbers"""
    return a * b

def divide(a, b):
    """Divides two numbers"""
    if b == 0:
        raise ZeroDivisionError("Attention: Cannot divide by zero")
    return a / b

def mod(a, b):
    """Performs modulo operation on two numbers"""
    return a % b
