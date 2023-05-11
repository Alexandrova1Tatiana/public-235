a=int (input ("Введите а:"))
b=int (input ("Введите b:"))
x=a
for x in range (a,b+1) :
    y= x**(1/2)
    print("Ответ :",x,y)
    x+= 1