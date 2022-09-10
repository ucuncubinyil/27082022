##### FOR DONGUSU #####
"""
i =  1

while( i <10):
	print(i)
	i +=1
"""
"""
print(range(5)) # 0-5 aralığını verir bitiş değerini almaz
print(range(1,5)) #1-5 aralığını alır 5 i dahil etmez
print(range(1,9,3))  #1,4,7 aralığını alır. Başlangıçtan itibaren 3 er 3 er arttırır
"""

"""
for i in range(aralık):
    çalışacak kod bloğu
"""
"""
# 1-11 arasındaki sayilar 1,2,3...10
for sayi in range(1,11):
	print(sayi)
	
"""

"""
for say in range(1,9,3):
	print(say)
"""
"""
ilce = "Kadıköy"

for karakter in ilce:
	print(karakter)
"""
##### ALIŞTIRMALAR #####
# 1 ile 40 arasındaki sayıları toplayan programı yazınız. 40 dahil.

"""
toplam = 0
for sayi in range(1,41):
	toplam += sayi

print(f"1-40 arasındaki sayıların toplamı {toplam}")
"""

"""
## SORU 20-40 arasındaki çift ve tek sayıların
# toplamlarını ayrı ayrı ekrana yazdırınız.

cift_toplam = 0
tek_toplam = 0
for sayi in range( 20, 41 ):
	if sayi % 2 == 0:
		cift_toplam += sayi
	else:
		tek_toplam += sayi

print( f"20-40 aralığındaki çift sayıların toplamı {cift_toplam}" )
print( f"20-40 aralığındaki tek sayıların toplamı {tek_toplam}" )
"""
# 1'den başlayarak Klavyeden girilen sayıya kadar
# olan sayılardan 4'e tam bölünenlerinin çarpımını yazdırınız
"""
carp = 1
bitis =  int(input("Lütfen bitiş sayısını girin: "))

# faktöryel !!! 5 ! 1*2*3*4*5
for i in range(1,(bitis+1)):
	if i % 4 ==0:
		carp *= i
print(f"1 ile {bitis} aralığındaki sayıların çarpımı {carp} !")

"""
# Kullanıcıdan girilen sayıya kadar olan sayıların çarpımını
# hesaplayın (Faktöryel Hesabı)
"""
carp = 1
baslagic = int( input( "Başlangıç değerini yazın" ) )
bitis = int( input( "Bitiş değerini yazın" ) )

if baslagic < 1:
	baslagic = 1

for sayi in range( baslagic, bitis + 1 ):
	
	carp *= sayi

print( f"{bitis}! = {carp}" )
"""

"""
print("Ahmet"*2)
"""
"""
*
**
***
****
*****
"""
"""
for i in range(1,6):
	print("*"*i)
	
"""

"""
*****************
*               *
*               *
*               *
*               *
*****************

"""

"""
for i in range(1,7):
	if i == 1 or i == 6:
		print("*"*15)
	else:
		print("*", (" "*13), "*", sep="")
"""

"""
            *
           ***
          *****
         *******
        *********
"""
"""
sayac = 1

for satir in range( 1, 6 ):
	print( " " * (5 - satir), end="" )
	print( "*" * sayac )
	sayac += 2
"""
## ÇARPIM TABLOSU
"""
1 x 1 = 1 1 x 2 = 2 1 x 3 =3
2 x 1 = 2 ....
3 x 1 = 3 """
"""
for i in range(1,11):
	
	for j in range(1,11):
		print(i , "x", j, "=", (i*j), end="\t\t")
	print()
"""
"""
# TERSTEN YAZDIRMA
for i in range(10,0,-1):
	print(i)
"""
# SORU: Kullanıcıdan personel sayısını alınız.
# Personelin kaç çocuğu olduğunu isteyelim.
# Program her çocuk için "Çocuğunuz adına 1 ağaç dikilmiştir" yazsın
# Toplam dikilen ağaç sayısınıda ekrana yazdıralım.
"""
toplam_agac = 0
per_sayi =  int(input("Personel sayınızı giriniz: "))

for i in range(1,per_sayi+1):
	
	while True:
		cocuk_sayisi =  int(input(f"{i}. personelin çocuk sayısı"))
		toplam_agac += cocuk_sayisi
		break
	
	for j in range(cocuk_sayisi):
		print("Çocuğunuz adına 1 ağaç dikilmiştir.")
"""

#### TAHMİN OYUNU ####
# Bilgisayar 1-100 arasında rastgele bir sayı üretsin.
# Kullanıcının 5 hakkı olsun ve sayıyı bilmeye çalışsın.
# Bilirse TEBRİKLER. bilemezse tekrar deneyiniz. hakkı biter hakkınız bitti yazsın.
# BONUS: tahmin değeri rastgele değerden büyük ise tahmininizi küçültünüz
#        tahmin değeri rastgele değerden küçük ise tahmininizi büyültünüz

import random

rastgele_sayi = random.randint( 1, 100 )

for hak in range( 1, 6 ):
	tahmin = int( input( f"{hak}. tahmininizi girin: " ) )
	print( rastgele_sayi )
	
	if (rastgele_sayi > tahmin and hak < 5):
		print( "Tahmini küçültün" )
	elif rastgele_sayi < tahmin and hak < 5:
		print( "Tahmini büyült" )
	elif rastgele_sayi == tahmin:
		print( "Tebrikler" )
		break
	else:
		print( rastgele_sayi )
		print( "😛 Hak bitti" )

"""
hak = 5
while hak > 0:
	hak -= 1
	tahmin  = int(input("Lütfen tahmininizi girin: "))
	
	if rastgele_sayi == tahmin:
		print("Tebrikler")
		break
	elif rastgele_sayi < tahmin:
		print("Tahmininizi küçültün")
	
	else:
		print("Tahmininizi büyültün")

if hak == 0:
	print(rastgele_sayi)
	print("Hakkınız bitti")
"""
