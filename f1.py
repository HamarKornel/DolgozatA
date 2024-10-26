def elso():
    a1 = int(input("Kérem adjon meg egy egész számot!"))
    q = int(input("Kérem adjon meg egy egész számot!"))
    n = 1
    while n < 10:
        print(a1 * (q ** (n-1)), end=",")
        n += 1
    print(a1 * (q ** (10-1)))


