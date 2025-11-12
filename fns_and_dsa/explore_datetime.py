from datetime import datetime, timedelta

# Part 1: Display the current date and time
def display_current_datetime():
    current_date = datetime.now()  # get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # format it nicely
    print("Current date and time:", formatted_date)
    return current_date  # return so we can reuse it later

# Part 2: Calculate a future date
def calculate_future_date(current_date):
    try:
        # Ask the user how many days to add
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        future_date = current_date + timedelta(days=days_to_add)  # add days
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input! Please enter an integer number of days.")

# Main program flow
def main():
    current_date = display_current_datetime()  # display and store the current datetime
    calculate_future_date(current_date)        # calculate and display the future date

if __name__ == "__main__":
    main()
