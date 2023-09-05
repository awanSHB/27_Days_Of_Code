def out(a, b):
    def cal(a, b):
        add = a+b
        return add
    res = cal(a, b)
    print(res)
    fin = res + 5
    return fin
check = out(70, 10)
print(check)