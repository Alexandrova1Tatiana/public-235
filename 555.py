year= int(input("Введите год:"))
def century(year):
    if year % 10 == 0:
        return (year // 100)
    else:
        return (year // 100) +1
print(century(year))
