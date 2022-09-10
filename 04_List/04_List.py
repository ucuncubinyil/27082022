############### LİSTE list() #####################
"""
liste =  list() # boş liste oluşturma 1. yöntemi ve tavsiye edilen
liste2 =  [] # boş liste oluşturma 2. yöntemi ve tavsiye edilmeyen

liste3 = [2,"Mehmet", False, 2.5]
print(liste3)

#Var olan listeye eleman ekleme
liste2 +=[2] # tavsiye edilmeyen
print(liste2)

liste.append("Deneme") # Tavsiye edilen
print(liste)
"""
"""
liste = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

#Listenin içindeki herhangi bir değere index numarasıyla erişmek
print(liste[7])

# Listeden eleman silme
del liste[3] # tavsiye edilmeyen(index no ile)
print(liste)

liste.remove(5) # tavsiye edilen(değer arama ile)
print(liste)


# Çoklu veri ekleme

#1. yöntem tavsiye edilmeyen
liste += ["Veli","Deli", "Ali"]
print(liste)

#2. yöntem tavsiye edilen
liste.append(["Kemal","Bora", "Deniz"])
liste.append("Kemal")
liste.append("Bora")
liste.append("Deniz")
print(liste)


"""

"""
# Çok boyutlu dizi
liste = [ [ 1, 2, 3 ], [ 4, 5, 6 ] ]
print( liste[ 1 ][ 0 ] )
print( [ 0 ][ 0 ] )
"""

# *** Listede verilen index veri ekleme ***

rakamlar = [ 1, 2, 3, 4, 5, 6, 7 ]
print(rakamlar)
print(rakamlar[4])

rakamlar.insert(4,9)
print(rakamlar)


# # *** Listedeki değerin index'ine ulaşma ***
print(rakamlar.index(3))