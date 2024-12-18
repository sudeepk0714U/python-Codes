def _leap_year(y):
    return ((y %4 == 0 and y%100 != 0 ) or y%400 == 0)
y = int(input("enter year : "))
if(_leap_year(y)):
    print("it is leap year")
else:
    print("it is not a leap year")

    