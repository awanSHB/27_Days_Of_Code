num = 0
for num in range(0, 101):
    if num%3 == 0:
        if num%5 == 0:
            print("FizzBuzz")
        else:
            print("fizz")
    elif num%5 == 0:
        print("buzz")
    else:
        print(num)