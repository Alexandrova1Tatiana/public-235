b = int(input("Введите шестизначное число"))
a= b//100000
if a==2:
    print("есть 2")
m= b% 100000
if m==2:
    print("есть 2")
k = m // 10000
if k==2:
    print("есть 2")
q = m % 10000
if q==2:
    print("есть 2")
w = q//1000
if w==2:
    print("есть 2")
e = q%1000
if e==2:
    print("есть 2")
r = e//100
if r==2:
    print("есть 2")
t = e%100
if t==2:
    print("есть 2")
y = t//10
if y==2:
    print("есть 2")
u = t%10
if u==2:
    print("есть 2")