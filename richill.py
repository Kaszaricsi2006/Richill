def szamologep():
    print("Egyszerű Számológép")
    print("Válassz műveletet:")
    print("1. Összeadás")
    print("2. Kivonás")
    print("3. Szorzás")
    print("4. Osztás")
    
    valasz = input("Választott művelet (1/2/3/4): ")

    szam1 = float(input("Kérem az első számot: "))
    szam2 = float(input("Kérem a második számot: "))

    if valasz == '1':
        print(f"Az összeg: {szam1 + szam2}")
    elif valasz == '2':
        print(f"A különbség: {szam1 - szam2}")
    elif valasz == '3':
        print(f"A szorzat: {szam1 * szam2}")
    elif valasz == '4':
        if szam2 != 0:
            print(f"A hányados: {szam1 / szam2}")
        else:
            print("Nem osztható 0-val")
    else:
        print("Érvénytelen választás")

szamologep()
