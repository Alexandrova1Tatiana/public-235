E = 0.0001

s = 0
x = 1
flag = 1

while True:
if abs(1 / x) < E:
    break

if flag == 1:
    s += 1 / x
else:
    s -= 1/x

x *= 2
flag *= -1

print(s)
