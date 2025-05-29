class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    
calc = Calculator()

choice = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()
if choice in ['add', 'subtract', 'multiply', 'divide']:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == 'add':
            result = calc.add(num1, num2)
        elif choice == 'subtract':
            result = calc.subtract(num1, num2)
        elif choice == 'multiply':
            result = calc.multiply(num1, num2)
        elif choice == 'divide':
            result = calc.divide(num1, num2)
        
        print(f"The result is: {result}")
    except ValueError as e:
        print(f"Error: {e}")
else:
    print("Invalid operation selected.")