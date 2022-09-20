from dataclasses import dataclass
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    obj1name = "textfile.txt"
    # print(os.name)
    # print("Item exists: ", str(path.exists(obj1name)))
    # print("Item is file: ", path.isfile(obj1name))
    # print("Item is directory: ", path.isdir(obj1name))
    # print("Item real path: ", path.realpath(obj1name))
    # print("Item path and name: ", path.split(path.realpath(obj1name)))
    p = path.getmtime(obj1name)
    t = time.ctime(p)
    print(t)
    print(datetime.datetime.fromtimestamp(p))
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(p)
    print("It has been", td, "since the file was modified")
    print("OR", td.total_seconds(), "seconds ago")

if __name__ == "__main__":
    main()
