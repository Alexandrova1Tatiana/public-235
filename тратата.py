def max(x, y):
    if x > y:
        return x
    else:
        return y
    def min(x, y):
        if x<y:
            return x
        else:
            return y
print("Введите 4 числа:")
a = int(input(Введите число:))
b = int(input(Введите число:))
c = int(input(Введите число:))
d = int(input(Введите число:))
m1 = max(max(a,b),max(c,d))
m2 = min(min(a,b),min(c,d))
print("max = "m1)
print("min = ",m2)
S = m1+m2
print("s = ",s)
