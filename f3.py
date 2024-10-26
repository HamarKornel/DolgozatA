def harmadik():
    for szam1 in range(50, 901, 2):
        if szam1 % 11 == 0:
            print(szam1, end="|")

    szam2 = 50
    while (szam2 >= 50) and (szam2 < 900):
        szam2 += 2
        if szam2 % 2 == 0 and szam2 % 11 == 0:
            print(szam2, end="|")
