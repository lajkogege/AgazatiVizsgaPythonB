import ertekel
ertekel.adatbeker()

import sorozat
print("II/A, B, C:")
szam_lista:int=[]
sorozat.veletlen(szam_lista)
tizzel_oszhtaok=sorozat.tizzel_oszthatok_szama(szam_lista)


print("II/D, E:")
tizzel_oszhtaok=sorozat.tizzel_oszthatok_szama(szam_lista)
sorozat.koznolra_ir(tizzel_oszhtaok)
print("II/F:")
sorozat.fajlba_ir(tizzel_oszhtaok)

import hatoslotto
print("III/A, B:")
osztaly_lista=hatoslotto.fajlbeolvasas()
print(f"\t A huzások száma: {len(osztaly_lista)}")

print("III/C:")
atlag=hatoslotto.huzasid(osztaly_lista)
print(f"\t A 42.héten huzott számok átlaga: {atlag}")

print("III/D:")
index=hatoslotto.legnagyobb_kihuzott_szam_adatai(osztaly_lista)
print(f"\t A legnagyobb kihuzott szám értéke: {osztaly_lista[index].szam}, a {osztaly_lista[index].het} héten huzták ki, ez volt a {index}")
