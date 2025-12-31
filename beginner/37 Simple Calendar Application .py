import calendar

print("Calendar Application\n")

while True:
    try:
        year = int(input("Enter the year: "))
        month = int(input("Enter the month (1-12): "))
        
        if 1 <= month <= 12:
            print(calendar.month(year, month), "\n")
        else:
            print("Please enter a month between 1 and 12.")
    except ValueError:
        print("Invalid input! Please enter numeric values for year and month.")
    except Exception as e:
        print(f"An error occurred: {e}")