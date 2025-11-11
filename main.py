# calculator.py - INITIAL MAIN BRANCH (Before any merges)
class Calculator:
    def __init__(self):
        # Initialize basic attributes that all features might need
        self.result = 0
        self.memory = 0
        self.history = []
    
    # PLACEHOLDER METHODS - Empty or with basic implementation
    # Student 1: Addition function
    def add(self, a, b):
        """Return the sum of two numbers and update result and history."""
        self.result = a + b
        self.add_to_history(f"Added {a} + {b} = {self.result}")
        return self.result
    
    # Student 2: Subtraction function
   # Student 2: Subtraction function
    def subtract(self, a, b):
        
        difference = a - b
        self.result = difference
        operation = f"{a} - {b} = {difference}"
        self.add_to_history(operation) # Call the history method (once implemented)
        return difference
    # Giddel: Multiplication_giddel0001
    def multiply(self, a, b):
        product = a * b
        self.result = product
        operation = f"{a} * {b} = {product}"
        self.add_to_history(operation)  # Log the operation to history
        return product
        raise NotImplementedError("Multiplication function not implemented yet")
    
    # Student 4: Division function
    def divide(self, a, b):
    if b == 0:
        raise ValueError("You cannot divide by zero.")
    return a / b
    
    # Student 5: Square root function
    def square_root(self, a):
        # TODO: Implement square root functionality
        raise NotImplementedError("Square root function not implemented yet")
    import math

# Ask user for input
num = float(input("Enter a number: "))

# Calculate the square root
sqrt = math.sqrt(num)

# Display the result
print(f"The square root of {num} is {sqrt}")
    # Student 6: Power function
    # Student 6: Power function
    def power(self, base, exponent):
        try:
            result = base ** exponent
            self.result = result
            operation = f"{base} ^ {exponent} = {result}"
            self.add_to_history(operation)  # Record operation in history
            return result
        except Exception as e:
            return f"Error: {e}"
    # Student 7: Percentage function
    def percentage(self, value, total):
    """
    Calculate what percentage 'value' is of 'total'.

    Parameters:
        value (float): The part value
        total (float): The total value

    Returns:
        float: Percentage value (0-100)
    """
    if total == 0:
        raise ValueError("Total cannot be zero")  # Avoid division by zero
    return (value / total) * 100
    
    # Student 8: Memory functions - Placeholders
    def memory_store(self, value):
        # TODO: Implement memory store
        pass
    
    def memory_recall(self):
        # TODO: Implement memory recall
        pass
    
    def memory_clear(self):
        # TODO: Implement memory clear
        pass
    
    # Student 9: Clear function
    def clear(self):
        # TODO: Implement clear functionality
        pass
    
    # Michelo: Trigonometric functions - updated
    import math

def sin(self, angle):
    return math.sin(angle)
    
    def cos(self, angle):
        # TODO: Implement cosine function
        pass
    
    def tan(self, angle):
        # TODO: Implement tangent function
        pass
    
    # Student 13: Logarithmic functions - Placeholders
    def log(self, value):
        # TODO: Implement logarithm function
        pass
    
    def ln(self, value):
        # TODO: Implement natural log function
        pass
    
    # Student 14: History feature - Placeholders
    def add_to_history(self, operation):
        # TODO: Implement history tracking
        pass
    
    def get_history(self):
        # TODO: Implement history retrieval
        pass

# Basic main function skeleton
def main():
    print("Calculator Project")
    print("Features will be added by individual contributors")
    calc = Calculator()
    print("Calculator initialized - waiting for feature implementations")

if __name__ == "__main__":
    main()
    
