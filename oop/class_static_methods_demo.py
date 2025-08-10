# class_static_methods_demo.py

class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Return the product of two numbers and display calculation type."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# Example usage
if __name__ == "__main__":
    # Using static method
    sum_result = Calculator.add(5, 3)
    print(f"Sum: {sum_result}")

    # Using class method
    product_result = Calculator.multiply(4, 2)
    print(f"Product: {product_result}")
