
from datetime import datetime

def main():
    now = datetime.now()

    # %y,%Y = year
    # %a, %A = weekday
    # %b, %B = month
    # %d = day of month
    print(now.strftime("The current year is: %Y"))
    print(now.strftime("%a, %d %B, %y"))

    # %c = locale's date and time
    # %x = locale's date
    # %X = locale's time
    print(now.strftime("Local date and time: %c"))
    print(now.strftime("Local date: %x"))
    print(now.strftime("Local time: %X"))

    # %I, %H = 12/24hr
    # %M = minute
    # %S = second
    # %p = locale am/pm
    print(now.strftime("Current time: %I:%M:%S %p"))
    print(now.strftime("24-hour time: %H:%M"))

if __name__ == "__main__":
    main()