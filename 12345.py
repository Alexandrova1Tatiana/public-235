from copy import deepcopy
def connect_the_dots(paper):
    temp=paper.split("\n")
    res=[list(temp[i]) for i in range(len(temp))]
    temp2=deepcopy(res)
    letter="a"
    while True:
        from_=find_letter(letter, temp2)
        to_=find_letter(chr(ord(letter)+1), temp2)
        if to_==(-1, -1):
            break
        if from_[1]==to_[1]:
            for i in range(from_[0]-to_[0]+1):
                res[to_[0]+i][from_[1]]="*"
            for i in range(to_[0]-from_[0]+1):
                res[from_[0]+i][from_[1]]="*"
        elif from_[0]==to_[0]:
            for i in range(from_[1]-to_[1]+1):
                res[from_[0]][to_[1]+i]="*"
            for i in range(to_[1]-from_[1]+1):
                res[from_[0]][from_[1]+i]="*"
        else:
            x=from_[1]-to_[1]
            y=from_[0]-to_[0]
            if x==y:
                for i in range(from_[0]-to_[0]+1):
                    res[to_[0]+i][to_[1]+i]="*"
                for i in range(to_[0]-from_[0]+1):
                    res[from_[0]+i][from_[1]+i]="*"
            elif x>y:
                for i in range(from_[1]-to_[1]+1):
                    res[from_[0]+i][from_[1]-i]="*"
            else:
                for i in range(from_[0]-to_[0]+1):
                    res[from_[0]-i][from_[1]+i]="*"
        letter=chr(ord(letter)+1)
    return "\n".join("".join(i) for i in res)
def find_letter(s, arr):
    for i,j in enumerate(arr):
        for k,l in enumerate(j):
            if l==s:
                return (i, k)
    return (-1, -1)