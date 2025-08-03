# robust_division_calculator.py

def safe_divide(numerator, denominator):

    try:
        # Convert both inputs to float
        num = float(numerator)
        den = float(denominator)

        # Perform division
        result = num / den
        return f"Result: {result:.2f}"  # Format to 2 decimal places

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter valid numeric inputs."

    except Exception as e:
        # Failsafe for error
        return f"Unexpected error: {str(e)}"
