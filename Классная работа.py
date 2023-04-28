a=0
n=10
for i in range(1,n+ 1,2):
    a=a+1
    if a==5:
        continue
    print (a)
    if a==7:
        break
print ("всё!")