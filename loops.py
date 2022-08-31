def main(x=0):
    while(x < 10):
        print(x)
        x = x+1

def main2():
    for x in range(50,60):
        # if x == 53:
        #     break
        if x % 2 == 0:
            continue
        print(x)

def main3(d):
    for i in d:
        print(i) 


def main4(arr): 
    for i, x in enumerate(arr):
        print(str(i) + " " + x)


if __name__ == "__main__":
    x = 10
    days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    # main(x)
    # main2()
    # main3(days)
    main4(days)
