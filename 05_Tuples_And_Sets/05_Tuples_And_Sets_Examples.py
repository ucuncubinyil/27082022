kume = { 11, 22, 33, 44 }
kume2 = { 33, 44, 55, 66, 77, 88, 99 }

"""
# Küme Farkı Bulma

kume_fark =  kume - kume2 # 1. yöntem tavsiye edilmeyen
print(kume_fark)

kume_fark =  kume.difference(kume2) # 2. yöntem tavsiye edilen
print(kume_fark)

"""

"""
#Küme Kesişim

kume_kesisim =  kume & kume2 #1. yöntem tavsiye edilmeyen
print(kume_kesisim)

kume_kesisim = kume.intersection(kume2) # 2. yöntem tavsiye edilen
print(kume_kesisim)

"""
"""
#Küme Birleşim

#kume_birlesim = kume + kume2 # Hata verir + operatörü setlerde kullanılmaz
#print(kume_birlesim)

kume_birlesim =  kume.union(kume2)
print(kume_birlesim)
"""

#Alt Küme
print(f"Küme kümesi Küme2 kümesinin alt kümesi midir? :{kume.issubset(kume2)}")

#Üst Küme
print(f"Küme kümesi Küme2 kümesinin üst kümesi midir? :{kume.issuperset(kume2)}")

# Ayrk Küme
print(f"Küme kümesi ile Küme2 kümesi ayrık küme midir? :{kume.isdisjoint(kume2)}")
