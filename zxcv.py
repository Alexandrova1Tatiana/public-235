def row_sum_odd_numbers(n):
    count=0
    total=0
    count2=0
    for i in range(n):
        count+=i
    for j in range(n):
        total+=(1+count*2)+count2
        count2+=2
    return total