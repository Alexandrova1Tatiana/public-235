e = int(input("Введите трехзначное число"))
if e<1000 and e<99:
  print("Ошибка")
r = e//100
t = e%100
y = t//10
u = t%10
o= u*100+y*10+r
if e==o:
    print("Палиндром")
if e!=o:
    print("Ошибка")