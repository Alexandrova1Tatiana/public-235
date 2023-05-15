def calculation(a, b, c):
    result = (a + b) * c
    return result

if __name__ == "__main__":
a = int(input("Введите значение переменной a: "))
b = int(input("Введите значение переменной b: "))
c = int(input("Введите значение переменной c: "))
result = calculation(a, b, c)
print("Результат вычислений:", result)
