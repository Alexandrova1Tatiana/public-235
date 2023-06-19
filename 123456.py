def Dragon(n):
    if not isinstance(n, int) or n<0:
        return ""
    res="Fa"
    for _ in range(n):
        temp=""
        for i in res:
            if i=="a":
                temp+='aRbFR'
            elif i=="b":
                temp+='LFaLb'
            else:
                temp+=i
        res=temp
    return res.replace("a", "").replace("b", "")