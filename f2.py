def masodik():
    honap = int(input("Kéram adja meg az aktuális honap sorszámát:"))
    if (honap >= 1) and (honap <= 12):
        vegOsszeg = int(input("kérem Adja meg a fizetendő teljes árat:"))
        if honap == 1:
            print("Hónapos akció: Január")
            print("fizetendő összeg: "+str(int(vegOsszeg-(vegOsszeg*(1/100)))))
        elif honap == 2:
            print("Hónapos akció: Február")
            print("Fizetendő összeg: "+str(int(vegOsszeg-(vegOsszeg*(2/100)))))
        elif honap == 3:
            print("Hónapos akció: Március")
            print("Fizetendő összeg: "+str(int(vegOsszeg-(vegOsszeg*(3/100)))))
        elif honap == 4:
            print("Hónapos akció: Április")
            print("Fizetendő összeg: "+str(int(vegOsszeg-(vegOsszeg*(4/100)))))
        elif honap == 5:
            print("Hónapos akció: Május")
            print("Fizetendő összeg: "+str(int(vegOsszeg-(vegOsszeg*(5/100)))))
        elif honap == 6:
            print("Hónapos akció: Június")
            print("Fizetendő összeg: "+str(vegOsszeg))
        elif honap == 7:
            print("Hónapos akció: Július")
            print("Fizetendő összeg: "+str(vegOsszeg))
        elif honap == 8:
            print("Hónapos akció: Agusztus")
            print("Fizetendő összeg: "+str(int(vegOsszeg-(vegOsszeg*(6/100)))))
        elif honap == 9:
            print("Hónapos akció: Szeptember")
            print("Fizetendő összeg: "+str(int(vegOsszeg-(vegOsszeg*(7/100)))))
        elif honap == 10:
            print("Hónapos akció: Oktober")
            print("Fizetendő összeg: "+str(int(vegOsszeg-(vegOsszeg*(8/100)))))
        elif honap == 11:
            print("Hónapos akció: November")
            print("Fizetendő összeg: "+str(int(vegOsszeg-(vegOsszeg*(9/100)))))
        else:
            print("Hónapos akció: December")
            print("Fizetendő összeg: "+str(int(vegOsszeg-(vegOsszeg*(10/100)))))

    else:
        print()


