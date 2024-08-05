class Addition:
    def add(self, a, b):
        return a + b

class Multiplication:
    def multiply(self, a, b):
        return a * b

class Calculator(Addition, Multiplication):
    def perform_operations(self, a, b):
        print("Addition:", self.add(a, b))
        print("Multiplication:", self.multiply(a, b))

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

calc = Calculator()
calc.perform_operations(a, b)
