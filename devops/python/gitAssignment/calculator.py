import math

class Calculator:
    # Addition of two numbers
    def add(self, a, b):
        return a + b

    # Subtraction of two numbers
    def subtract(self, a, b):
        return a - b

    # Multiplication of two numbers
    def multiply(self, a, b):
        return a * b

    # Division of two numbers, handling divide by zero case
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    # Square root function
    def square_root(self, x):
        return math.sqrt(x)

if __name__ == "__main__":
    calculator = Calculator()

    num1 = 16
    num2 = 4
    num3 = 25

    # Testing basic arithmetic functions
    print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
    print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")
    print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
    print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")

    # Testing square root function
    print(f"The square root of {num3} = {calculator.square_root(num3)}")