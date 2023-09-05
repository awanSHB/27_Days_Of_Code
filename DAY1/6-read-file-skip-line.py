# read read.txt
with open("read.txt", "r") as fp:
    # read all the lines from the file
    lines = fp.readlines()
    
# open new file in write mode
with open("new_file.txt", "w") as fp:
    counting = 0
    #iterat each line from the txt file
    for line in lines:
        if counting==4:
            counting+=1
            continue
        else:
            fp.write(line)
        counting+=1
