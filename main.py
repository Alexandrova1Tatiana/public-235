moth = int(input("Введите число месяца: "))
def season(moth):
    if moth == 12 or moth < 3:
        print("Зима")
    elif moth == 3 or moth < 6:
        print("Весна")
    elif moth == 6 or moth < 9:
        print("Лето")
    else:
        print("Осень")
season(moth)