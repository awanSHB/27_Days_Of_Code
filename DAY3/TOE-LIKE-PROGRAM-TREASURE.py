row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
map = [row1, row2, row3]
print("     1    2    3")
print("     -    -    -")
print(f"1| {row1}\n2| {row2}\n3| {row3}")
print()
position = input("where do you want to put the treasure? : ")
horizontal = int(position[0])
vertical = int(position[1])
map[vertical-1][horizontal-1] = "X"
print()
print(f"{row1}\n{row2}\n{row3}")