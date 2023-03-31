z=int(input("Введите число дня:"))
if 1<=z<=31:
    e = int(input("Введите пробег:"))
    if e<1000 and e>99:
        r = e//100
        t = e%100
        y = t//10
        u = t%10
        k= u+y+r
        if k>=z:
            print("Сброс")
        else:
            print("Сегодня не сломался")
else:
    print("Ошибка")
