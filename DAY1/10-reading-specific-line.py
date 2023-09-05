with open ("read.txt", "r") as fp:
    lines = fp.readlines()
with open("check.txt", "w") as fp:
    count = 0
    for line in lines:
        if(count==4):
            fp.write(line)
            break
        count+=1
        