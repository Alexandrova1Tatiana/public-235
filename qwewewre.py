Time_Left = int(input('введите время в минутах с начала часа: '))

x = Time_Left // 5
l = Time_Left - (x * 5)

if l == 0:
    print('it is red')
elif l == 1:
    print('it is green')
elif l == 2:
    print('it is green')
elif l == 3:
    print('it is green')
elif l == 4:
    print('it is red')
elif l == 5:
    print('it is red')
    