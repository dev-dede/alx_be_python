from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    
    # Format the current date and time in the "YYYY-MM-DD HH:MM:SS" format
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the formatted date and time
    print(f"Current date and time: {formatted_date}")
    

def calculate_future_date(days):
    
    current_date = datetime.now()
    
    future_date = current_date + timedelta(days=days)
    
    # Format the future date as "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    
    # Print the future date
    print(f"Future Date: {formatted_future_date}")


# Call the function to test it
display_current_datetime()

# Prompt the user to enter the number of days
days_to_add = int(input("Enter the number of days to add to the current date: "))

# Call the function to calculate and display the future date
calculate_future_date(days_to_add)