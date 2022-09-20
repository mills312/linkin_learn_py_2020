
from datetime import date
from datetime import time
from datetime import datetime


def main():
    today = date.today()
    arr_days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    # print("today is", today)
    # print("Date components: ", today.day, today.month, today.year)
    # print("weekday #", today.weekday())
    # print("Which is a ", arr_days[(today.weekday())])

    n = datetime.now()
    print("The current date time is:", n)

    t = datetime.time(datetime.now())
    print("The current time is:", t)

if __name__ == "__main__":
    main()

