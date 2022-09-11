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
import random

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

"""
rakamlar = [ 1, 2, 3, 4, 5, 6, 7 ]
print(rakamlar)
print(rakamlar[4])

rakamlar.insert(4,9)
print(rakamlar)


# # *** Listedeki değerin index'ine ulaşma ***
print(rakamlar.index(3))

"""
"""
sayilar = [ 10, 20, 30, 40, 20, 20, 20 ]

print(sayilar.index(20))# ilk 20 değerinin index i yazdırılır.
print(sayilar.index(20,4))# 2. indexten itibaren aramaya başla
"""
"""
isimler = ["Ahmet","Mehmet","Veli", "Ali"]
print(len(isimler)) # Len komutu dizinin uzunluğunu verir

print(isimler[ int(len(isimler) -len(isimler)) ])

#Tavsiye edilen
for isim in isimler:
	print(isim)

#Tavsiye edilmeyen
for i in range(len(isimler)):
	print(isimler[i])

i = 0
while i < len(isimler):
	print(isimler[i])
	i += 1

for isim in isimler:
	print(f"İndex {isimler.index(isim)} Değer: {isim}")
	
	"""
"""
# *** Listedeki bir değerin kaç defa eklendiğini bulma ***

sayilar = [ 10, 20, 30, 40, 20, 20, 20 ]
print(sayilar.count(20))
"""
"""
# SORU: Listedeki 20 değerlerinin indexlerini ekrana yazdırınız.
sayilar = [ 10, 20, 30, 40, 20, 20, 20 ]

for sayi in range( len( sayilar ) ):
	if sayilar[ sayi ] == 20:
		print( sayi )


indis = 0
for i in range( sayilar.count( 20 ) ):  # listedeki 20 adededine döngü
	print( sayilar.index( 20, indis ) )
	indis = sayilar.index( 20, indis ) + 1 #her seferinde bulduğu 20 değerinin indexinin 1 fazlasından aramaya başlayacak.
"""
"""
sayilar = [ 10, 20, 30, 40, 20, 20, 20 ]
print(sayilar[0])
print(sayilar[-1]) # listenin en sondaki değeri verir
print(sayilar[-3])
print(sayilar[-4])

"""

"""
import locale

locale.setlocale( locale.LC_ALL, "tr_TR.UTF-8" )

sehirler = [ "ZONGULDAK", "KONYA", "BURSA", "İZMİR", "ANTALYA", "MALATYA" ]
sehirler.sort( key=locale.strxfrm ) # Adan Zye sıralar

sehirler.sort( key=locale.strxfrm ,reverse=True) #Z den Aya sıralar
print( sehirler )

"""
"""
rakamlar = [ 5, 69, 76, 654, 498, 67868, 4797 ]
rakamlar.sort( ) #küçüktenbüyüğe
rakamlar.sort(reverse=True) #büyükten küçüğe
print( rakamlar )
"""

"""
#### Listeden değerleri dışarı atma
rakamlar = [ 5, 69, 76, 654, 498, 67868, 4797 ]

rakamlar.pop( )  # varsayılan en son elemanı siler
print( rakamlar )
rakamlar.pop( 3 )  # Parametresi indis tir. Indisi verilen eleman listeden silinir
print( rakamlar )

rakamlar.pop( rakamlar.index( 76 ) )
print( rakamlar )

##### bir değerin listede var olup olmadığı kontrol etme
if 5646 in rakamlar:
	print( "69 rakamlar dizisinin içinde" )

varmi = rakamlar.index( 67868 )
print( varmi )

sehirler = [ "ZONGULDAK", "KONYA", "BURSA", "İZMİR", "ANTALYA", "MALATYA" ]

if "MALATYA" in sehirler:
	print( "Malatya şehirler listesinde" )

# Liste birleştirme
liste1 = [ 1, 2, 3 ]
liste2 = [ 4, 5, 6 ]
liste = liste1 + liste2
print( liste )

listem = [ ]
listem.append( liste1 )
listem.append( liste2 )

print( listem )

sonListe = list( )

for i in liste1:
	sonListe.append( i )

for i in liste2:
	sonListe.append( i )

print( sonListe )

print( max( sonListe ) )  # Listedeki en büyük değeri verir
print( min( sonListe ) )  # Listedeki en küçük değeri verir,

# *** Tek satırda for yazma işlemi ***
"""

"""
rakamlar = list()

for i in range(11):
	rakamlar.append(i)

print(rakamlar)



rakamlar = [ i for i in range( 11 )]
print( rakamlar )
"""

# SORU 10 ile 100 arasındaki çift sayıları bir listeye atın.
"""
cift_sayilar = list( )
for sayi in range( 10, 101, 2 ):
	cift_sayilar.append( sayi )
print( cift_sayilar )

cift_sayilar_2 = [ i for i in range( 10, 101, 2 ) ]
print( cift_sayilar_2 )
"""
"""
liste = [ 44, 55, 66, 77 ]
liste2 = liste  # liste değişkeninin ramdeki adresini liste2 ye kopyala
liste2 = liste.copy() # yeni adres al
liste2.append("55")

print(liste)
print(liste2)

"""
### ALIŞTIRMALAR ###
# SORU: Kullanicidan 10 adet sayı alıp listeye
# atın ve sonrasında listenin aritmetik ortalamasını bulun.
"""
sayi_listesi = list()

for i in range(1,11):
	sayi =  input(f"{str(i)}. sayıyı giriniz")
	
	if sayi.isnumeric(): # sayi değişkeninin içeriği int mi kontrol eder
		sayi_listesi.append(int(sayi))
		
print(sum(sayi_listesi)/ len(sayi_listesi)) # sum() listedeki tüm elemanları toplar
"""

# 1. 1-100 arasında 20 adet rastgele sayı üretin ve
# aynı numara içerde olmadan listeye atın.
"""
sayilar = list()

while len(sayilar) <20:
	sayi = random.randint(1,100)
	if sayi not in sayilar:
		sayilar.append(sayi)
		
print(sayilar)
"""

"""
sayilar =  list()
for i in range(1,21):
	
	if len( sayilar  ) < 21:
		sayi = random.randint( 1, 100 )
		if sayi not in sayilar:
			sayilar.append( sayi )
		else:
			continue
	else:
		break
	
print(sayilar)
# 2. sayilar listesindeki sayıları ciflistesi ve
# teklistesi isimindeki iki ayrı listeye kontrol ederek ekleyiniz.

tek_sayilar = list()
cift_sayilar= list()
for sayi in sayilar:
	if sayi %2 ==0:
		cift_sayilar.append(sayi)
	else:
		tek_sayilar.append(sayi)

print(tek_sayilar)
print(cift_sayilar)
"""
"""
# ASAL SAYI BULMA KODU
sayi = int( input( "Asal kontrolü yapılacak sayıyı giriniz: " ) )
asal_mi = True

if sayi > 1:
	for i in range(2,sayi):
		if sayi % i == 0:
			asal_mi = False
			print(i)
			break
else:
	asal_mi = True
	print("Asal")
	
if asal_mi:
	print("Asal")
else:
	print("Asal değil")
"""
# SORU: Klavyeden alınan 5 kelimeyi bir listeye atın.
# : Girilen 6. kelimenin listede olup olmadığını ekrana yazdırınız.
"""
sayac = 1
kelimeler =  list()

while sayac < 7:
	kelime = input("Kelime gir")
	
	if sayac < 6:
		if kelime not in kelimeler:
			kelimeler.append(kelime)
			sayac += 1
		else:
			print(f"Bu kelime zaten listede mevcut {kelime}")
	else:
		if kelime in kelimeler:
			print(f"{kelime} kelimesi  kelimeler listesinde mevcut")
			break
		else:
			print(f"{kelime} kelimesi  kelimeler listesinde mevcut değil")
			break
"""
## Klavyeden -1 girilene kadar girilen sayıları bir listeye atsın.
"""

sayilar = list( )
sayi = int( input( "Sayı girin" ) )

while sayi != -1:
	sayilar.append( sayi )
	sayi = int( input( "Sayı girin" ) )

print( sayilar )
"""
### ÇOK BOYUTLU LİSTELER
cokBoyutlu = [ [ 1, 2, 3 ], [ 4, 5, 6 ] ]# 2x3 matris(liste)
print(cokBoyutlu[0][0])
print(cokBoyutlu[0][1])
print(cokBoyutlu[0][2])

print(cokBoyutlu[1][0])
print(cokBoyutlu[1][1])
print(cokBoyutlu[1][2])

