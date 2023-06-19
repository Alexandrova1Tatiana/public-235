def checkered_board(n):
    if not isinstance(n, int) or n<=1:
        return False
    res=[]
    if n%2==0:
        for i in range(n):
            temp=[]
            for j in range(n):
                temp.append("□") if (i+j)%2==0 else temp.append("■")
            res.append(" ".join(temp))
        return "\n".join(res)
    else:
        for i in range(n):
            temp=[]
            for j in range(n):
                temp.append("■") if (i+j)%2==0 else temp.append("□")
            res.append(" ".join(temp))
        return "\n".join(res)