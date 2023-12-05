def is_leap(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                print("It is a leap year")
                return True
            else:
                print("Not leap")
                return False
        else:
            print("Not leap")
            return False
    else:
        print("Not leap")
        return False
        
def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 30, 31, 31]
    if is_leap(year) and month==2:
        ac = 29
        return ac
    ab = month_days[month-1]
    return ab
year = int(input("Enter the year : "))
month = int(input("Enter the month : "))
days = days_in_month(year, month)
print(days)