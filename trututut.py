fib1 = 1
fib2 = 1
i = 0
n = 1000
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    print (fib_sum)
    i = i + 1