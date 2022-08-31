f=0

def main():
    print("hellow world")
    # name = input("what is your name?")
    # print("Nice to mee you, ", name)

def course_vars():
    global f
    f="def"
    print(f)


# print("blah" + str(123))

if __name__ == "__main__":
    course_vars()
    print(f)
    del f
    # print(f)


# notes for launch config
#  //"integratedTerminal",