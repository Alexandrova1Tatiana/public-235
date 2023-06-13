def nb_year (p0, pmax, percent, extra):
    p = p0
    years = 0
    while (p<=pmax):
        p += ((percent/100)*p0)+extra
        years += 1
    return years
print ("Требуемое количество лет:", nb_year(1000, 1200, 2, 50))