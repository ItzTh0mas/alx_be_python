from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        future_date = datetime.now() + timedelta(days=number_of_days)
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()

