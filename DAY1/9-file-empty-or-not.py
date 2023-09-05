import os

size = os.stat("read.txt").st_size
if size==0:
    print("This file is empty")
else:
    print("This file is not empty")
    with open ("read.txt", "r") as fp:
        lines = fp.readlines()
    with open("rod.txt", "w") as fp:
        for line in lines:
            fp.write(line)
        