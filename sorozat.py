
import random
def veletlen(szam_lista):
    szam:int=0
    for i in range (0,8,1):
        szam = random.randint(-100, 859)
        print(szam, end=";" )
        szam_lista.append(szam)
    print()
    return szam

def tizzel_oszthatok_szama(szam_lista):
    tizzel_oszhtaok:int=0
    for i in range (0,len(szam_lista),1):
        if szam_lista[i] %10 ==0:
            tizzel_oszhtaok+=1
    return tizzel_oszhtaok

def koznolra_ir(tizzel_oszhtaok):
    print(f"Tizzel oszthatok száma: {tizzel_oszhtaok}")


def fajlba_ir(tizzel_oszhtaok):
    with open('vegeredmeny.txt','w', encoding="utf-8") as fajlom:
        fajlom.write(str(tizzel_oszhtaok))



