def addition(num):
    if num:
        res = num + addition(num-1)
        return res
    else:
        return 0
fin = addition(10)
print(fin)