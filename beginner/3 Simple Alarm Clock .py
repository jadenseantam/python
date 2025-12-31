import time

while True:
    try:
        hrs = int(input("Enter the time to wait in hours: "))
        mins = int(input("Enter the time to wait in minutes: "))
        sec = int(input("Enter the time to wait in seconds: "))
        
        # Calculate total seconds
        totalsec = hrs * 3600 + mins * 60 + sec
        
        # Start countdown
        for remaining in range(totalsec, 0, -1):
            h = remaining // 3600
            m = (remaining % 3600) // 60
            s = remaining % 60
            formatted_time = f"{h:02}:{m:02}:{s:02}"
            print(f"Time remaining: {formatted_time}", end='\r')
            time.sleep(1)
        
        print("\nTime's up!")
        
    except ValueError:
        print("Please enter valid integers for hours, minutes, and seconds.\n")