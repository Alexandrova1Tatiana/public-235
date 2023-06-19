def memo():
    start, end={}, {}
    for i in words:
        start[i[0]]=start.get(i[0], [])+[i]
        end[i[-1]]=end.get(i[-1], [])+[i]
    return start, end
start, end=memo()
def crossword_2x2(puzzle):
    res=set()
    if puzzle[0][0]=="#":
        if puzzle[0][1].isalpha():
            for i in start.get(puzzle[0][1], []):
                for j in end.get(i[-1], []):
                    if i!=j: res.add((j, i, sum(values[k] for k in (i+j))))
        elif puzzle[1][0].isalpha():
            for i in start.get(puzzle[1][0], []):
                for j in end.get(i[-1], []):
                    if i!=j: res.add((i, j, sum(values[k] for k in (i+j))))
        elif puzzle[1][1].isalpha():
            for i in end.get(puzzle[1][1], []):
                for j in end.get(i[-1], []):
                    if i!=j: res.add((i, j, sum(values[k] for k in (i+j))))
    elif puzzle[0][1]=="#":
        if puzzle[0][0].isalpha():
            for i in start.get(puzzle[0][0], []):
                for j in start.get(i[-1], []):
                    if i!=j: res.add((j, i, sum(values[k] for k in (i+j))))
        elif puzzle[1][0].isalpha():
            for i in end.get(puzzle[1][0], []):
                for j in start.get(i[-1], []):
                    if i!=j: res.add((j, i, sum(values[k] for k in (i+j))))
        elif puzzle[1][1].isalpha():
            for i in end.get(puzzle[1][1], []):
                for j in end.get(i[0], []):
                    if i!=j: res.add((i, j, sum(values[k] for k in (i+j))))
    elif puzzle[1][0]=="#":
        if puzzle[0][0].isalpha():
            for i in start.get(puzzle[0][0], []):
                for j in start.get(i[-1], []):
                    if i!=j: res.add((i, j, sum(values[k] for k in (i+j))))
        elif puzzle[0][1].isalpha():
            for i in end.get(puzzle[0][1], []):
                for j in start.get(i[-1], []):
                    if i!=j: res.add((i, j, sum(values[k] for k in (i+j))))
        elif puzzle[1][1].isalpha():
            for i in end.get(puzzle[1][1], []):
                for j in end.get(i[0], []):
                    if i!=j: res.add((j, i, sum(values[k] for k in (i+j))))
    elif puzzle[1][1]=="#":
        if puzzle[0][0].isalpha():
            for i in start.get(puzzle[0][0], []):
                for j in start.get(i[0], []):
                    if i!=j: res.add((i, j, sum(values[k] for k in (i+j))))
        elif puzzle[0][1].isalpha():
            for i in end.get(puzzle[0][1], []):
                for j in start.get(i[0], []):
                    if i!=j: res.add((i, j, sum(values[k] for k in (i+j))))
        elif puzzle[1][0].isalpha():
            for i in end.get(puzzle[1][0], []):
                for j in start.get(i[0], []):
                    if i!=j: res.add((j, i, sum(values[k] for k in (i+j))))
    return sorted(res, key=lambda x: (-x[-1], x[0], x[1]))