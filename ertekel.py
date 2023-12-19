def adatbeker():
    het_napja:str=str(input("Hét napja: "))
    ora_neve:str=str(input("Óra neve: "))
    ertekeles:int=int(input("Értékelés: "))
    if ertekeles <1 and ertekeles>5:
        print("Nem megfelő határokon belül lett megadva. ")
    elif ertekeles <0:
        print("Az értékelés nem lehet negatív!")
    elif ertekeles >5:
        print("5 pont feletti értékelés nem elfogadható!")
    else:
        print("Köszönjük az értékelést!")
