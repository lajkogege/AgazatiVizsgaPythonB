from Osztaly import Osztaly

def fajlbeolvasas():
    with open("huzasok.txt", "r", encoding="utf-8") as fajlom:
        fajlom.readline()  # Elolvassuk az első sort, ha szükséges
        fajbol_sorok_lista = fajlom.readlines()

    osztaly_lista = []
    for sor in fajbol_sorok_lista:
        sor_lista = sor.strip().split('@')
        huzas = int(sor_lista[0])
        ev = int(sor_lista[1])
        het = int(sor_lista[2])
        szam = int(sor_lista[3])
        osztaly = Osztaly(huzas, ev, het, szam)
        osztaly_lista.append(osztaly)

    return osztaly_lista

def huzasid(osztaly_lista):
    osszeg:int=0
    atlag:int=0
    db:int=0
    for i in range (0,len(osztaly_lista),1):
        if osztaly_lista[i].het == "42":
            osszeg += osztaly_lista[i].szam
            db+=1

    if db != 0:
        atlag = osszeg / db
    return atlag

def legnagyobb_kihuzott_szam_adatai(osztaly_lista):
    max:int=0
    index:int=0
    for i in range (0,len(osztaly_lista),1):
        if osztaly_lista[i].szam > max:
            max = osztaly_lista[i].szam
            index=i
    return index
