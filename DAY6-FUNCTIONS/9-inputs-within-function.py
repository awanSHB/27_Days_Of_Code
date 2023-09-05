def fun(f_n, l_n):
    if f_n== '' and l_n != '':
        f_n = 'sohaib'
        a = f_n.title()
        b = l_n.title()
        print(f'{a} {b}')
    elif f_n != '' and l_n == '':
        l_n = 'awan'
        a = f_n.title()
        b = l_n.title()
        print(f'{a} {b}')
    elif f_n!='' and l_n!='':
        a = f_n.title()
        b = l_n.title()
        print(f'{a} {b}')
    elif f_n=='' and l_n=='':
        print("You haven't entered any input")
        return
fun(input("What is your first name?: "), input("What is your last name?: "))