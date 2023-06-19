def removNb(n):
    temp=n*(n+1)//2
    res=[]
    for i in range(n//2, n):
        rec=((temp-i)/(i+1))
        if str(rec)[-2:]==".0":
            res.append(int(rec))
    final=[]
    index=0
    index2=len(res)-1
    while index<index2:
        final.append((res[index2], res[index]))
        final.append((res[index], res[index2]))
        index+=1
        index2-=1
    final=sorted(final, key=lambda x: x[0])
    return final