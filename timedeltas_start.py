
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

def main1():
    print(timedelta(days=365, hours=5, minutes=1))

    n = datetime.now()
    print("Today is:", n)

    print("one year from now:", str(n + timedelta(days=365)))
    print("In two weeks and 3 days it will be:", str(n + timedelta(weeks=2, days=3)))

    t = datetime.now() - timedelta(weeks=1)
    s = t.strftime("%A %B %d, %Y")
    print("One week ago it was:", s)

def main2():
    today = date.today()
    afd = date(today.year, 4, 1)
    if afd < today:
        print("April fool's day is passed:", ((today - afd).days))
        afd = afd.replace(year = today.year + 1)
    time_to_afd = afd - today
    print("April fool's day is in:", time_to_afd.days, "days")

if __name__ == "__main__":
    main2()