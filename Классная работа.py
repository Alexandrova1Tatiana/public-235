E = 0.0001

s = 0
n = 1
while True:
    delta = (2*n-1)/2*n
    s += delta
if delta < E:
    break
n += 1
print(delta)
print(s)