def main():
    # Prompting the user for the time
    time = input("What time is it? ")

    # Converting the time to hours
    time_in_hours = convert(time)

    # Checking if it's breakfast time (6:00 to 11:59)
    if 6 <= time_in_hours < 12:
        print("breakfast time")

    # Checking if it's lunch time (12:00 to 16:59)
    elif 12 <= time_in_hours < 17:
        print("lunch time")

    # Checking if it's dinner time (17:00 to 23:59)
    elif 17 <= time_in_hours < 24:
        print("dinner time")

def convert(time):
    # Splitting the time into hours and minutes
    hours, minutes = time.split(":")

    # Converting hours and minutes to integers
    hours = int(hours)
    minutes = int(minutes)

    # Converting the time to hours as a float
    total_hours = hours + minutes / 60

    return total_hours

if __name__ == "__main__":
    main()
