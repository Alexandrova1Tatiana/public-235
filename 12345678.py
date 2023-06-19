def zip_with(fn,a1,a2):
    res=[]
    for i,j in zip(a1, a2):
        res.append(fn(i, j))
    return res