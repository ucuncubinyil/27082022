#### Tuple: Sabit Liste ###
# Listeden farkı içerik güncellenemez

"""
sabit_liste =  () # boş sabit liste
sabit_liste_2 =  tuple() # boş sabit liste

tercihler = (1,2,3,4,5,"Mehmet", 22.5, False)
print(tercihler)
for tercih in tercihler:
    print(tercih)

print(tercihler[tercihler.index("Mehmet")])
liste = (1,2,[3,4] )
print(liste[2][1])

"""

### Set : Kume ###
kume = set() #boş küme
kume = {}#boş küme
kume_2 = {1,2,3,4}
print(kume_2)

kume_2.add("A") # var olan kümeye eleman ekleme
print(kume_2)

kume_2.remove("A") # var olan kümeden eleman silme
print(kume_2)

kume_2.discard("b") # remove dan farkı hata patlatmaz.
print(kume_2)
print(len(kume_2)) # kumenin eleman sayısını bulma
