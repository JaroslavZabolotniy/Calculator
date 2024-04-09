#Some comment
class Calculator:
    def add(self, x, y):
        return x + y
    def subtract(self, x, y):
        return x - y
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            raise ZeroDivisionError("Error: Division by zero")
        
    def power(self, x, y):
        if x == 0 and y == 0:
            raise ArithmeticError("Error: 0 in power of 0")
        else:
            return x ** y
    
    def gcd(self, x, y):
        while y:
            x, y = y, x % y
        return abs(x)
    
    def lcm(self, x, y):
        return x * y // self.gcd(x, y)
