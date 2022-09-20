
from operator import concat


def main():
#    my_file = open("textfile.txt", "w+")
    my_file = open("textfile.txt", "a+")

    for i in range(10):
        t1 = concat(str(i), " New Line of text\r")
        my_file.write(t1)

    my_file.close()

def read():
    my_file = open("textfile.txt", "r")
    if my_file.mode == 'r':
        # contents = my_file.read()
        # print(contents)
        fl = my_file.readlines()
        for x in fl:
            print(x)  

if __name__ == "__main__":
    #main()
    read()