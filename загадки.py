def Leap(year):
    if year % 4 != 0:
        return False;
    if year % 100 != 0:
        return True;
    if year % 400 != 0:
        return False;
    return True;


year = int(input("Введите год : "))
if Leap(year):
    print("Високосный")
else:
    print("Невисокосный")
