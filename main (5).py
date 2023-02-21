q = int(input("Введите четырехзначное число"))
w = q//1000
e = q%1000
r = e//100
t = e%100
y = t//10
u = t%10
cym = w+r+y+u
rar = w*r*y*u
print("Сумма",cym)
print("Произведение",rar)