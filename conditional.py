from ast import match_case


def main(x,y):
    if x<y:
        result = "x < y"
    elif x==y:
        result = "x = y"
    else:
        result = "x > y"
    return(result)


def main2(x,y):
    result = "x is less than y" if x < y else "x is equal to or greater than y"
    return result


def main3(x,y):
    match x:
        case 1: r = "one"
        case 2: r = "two"
        case 3|4|5|6|7|8|9: r = "three to nine"
        case _: r = "unknown"
    return r

if __name__ == "__main__":
    x,y = 80,100
    print(main3(x,y))  