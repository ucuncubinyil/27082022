#### ARMSTRONG SAYISI ####
"""
'''
armstrong sayısı
1634 -> 1^4 + 6^4 + 3^4 + 4^4 =1634 --> armstrong sayısıdır.
25 -> 2^2 + 5^2 = 29 --> armstrong sayı değildir.
'''
sayi = input("Sayi girin") #1634
toplam = 0

if sayi.isdigit():
	uzunluk =  len(sayi)
	for rakam in sayi:
		toplam +=  int(rakam)**uzunluk
	
if toplam == int(sayi):
	print("Sayı bir amstrong sayısıdır")
else:
	print("Amstrong sayısı değildir")
"""

################# FONKSİYONLAR #####################

"""
Programımızda belirli bir işi yapan kod bloklarının tekrar kullanılması durumunda
tekrar yazılmadan çağrılmasını
sağlayan modüllerdir.
Yani bir modülü 1 defa tanımlayıp istediğimiz zaman istediğimiz kadar kullanabilmemizi sağlar.
Fonksiyonlar yazdığımız programın modüler olmasını sağlar, ayrıca okunabilirliği artırır.
Fonsksiyonlar 2'ye ayrılır.
    Değer Döndüren Fonk. => parametreli ve parametresiz
    Değer Döndürmeyen Fonk. => parametreli ve parametresiz
"""
"""
#Parametre almayan ve değer döndürmeyen foksiyon
def snake_case_foksiyon_ismi():
	yapılacak islem
	
#Parametre alan ve değer döndürmeyen foksiyon
def snake_case_foksiyon_ismi(parametre1, parametre2):
	yapılacak islem

#Parametre almayan ve değer donduren foksiyon
def snake_case_foksiyon_ismi():
	return donecek_deger
	
#Parametre almayan ve değer donduren foksiyon
def snake_case_foksiyon_ismi(parametre1,parametre2):
	return donecek_deger
"""

"""
def  merhaba():
	print("Merhaba")
	

#Fonksiyon çağırma
merhaba()

"""

# global keyword; fonksiyon içerisindeki değişkenleri local olmaktan çıkartır.
"""
sayi1, sayi2 = 10, 20
ad =  "Mehmet Nuri" # global değişken

def  degistir():
	global  sayi1,sayi2
	global  ad
	
	ad = "Mehmet"# localdi global ile değişti
	sayi1,sayi2 = 45,55
	print(ad)
	print(sayi1,sayi2)
	

degistir()
print(sayi1,sayi2,ad)
"""
"""
def topla():
	sayi1= int(input("Sayi1"))
	sayi2= int(input("Sayi2"))
	print(sayi1+sayi2)

topla()
"""
"""
def topla_deger():
	sayi1= int(input("Sayi1"))
	sayi2= int(input("Sayi2"))
	return  (sayi1+sayi2)

sonuc = topla_deger()
print(sonuc)
"""
"""
#Parametre alan değer döndürmeyen
def islem(sayi1, sayi2):
	
	print(sayi1+sayi2)
	
islem(3,5)
"""
"""
def islem( sayi1, sayi2 ):
	
	return ( sayi1 + sayi2 )


sayi1 =  int(input("Sayi1"))
sayi2 =  int(input("Sayi2"))

sonuc = islem( sayi1,sayi2 )
print(sonuc)

"""

"""
def dort_islem( s1: int, s2: int, islem: str ):
	
	if islem == "+":
		return s1 + s2
	elif islem == "-":
		return s1 - s2
	elif islem == "*":
		return s1 * s2
	elif islem == "/":
		if s2 != 0:
			return s1 / s2
		else:
			return 0
	else:
		return 0


cevap = input("İşlem yapmak ister misiniz? ").upper()
while True:
	if cevap == "E":
		sayi1 =  int(input("Sayi1"))
		sayi2 =  int(input("Sayi2"))
		islem =  input("İşlem (+,-,*,/)")
		print(dort_islem(sayi1,sayi2,islem))
		cevap = input( "İşlem yapmak ister misiniz? " ).upper( )
		if cevap == "E":
			continue
	
	else:
		break
"""

## SORU: Kendisine gönderilen sayı adedince klavyeden
# girilen ismi alıp listeye atan fonksiyonu yazınız.
"""
def  isim_yaz():
	isim_liste = list()
	
	sayi =  int(input("Kaç kişi kayıt edilecek"))
	for i in range(sayi):
		isim = input(f"{i+1}. isim")
		isim_liste.append(isim)
	
	print(isim_liste)

isim_yaz()



sayi = int(input("Kaç kişi kayıt edilecek"))
isim_listesi = list()


def isimleri_yaz(kisi_sayisi:int, liste:list):
	
	for i in range(kisi_sayisi):
		isim = input(f"{i+1}. isim")
		liste.append(isim)
	
	return liste

sonuc = isimleri_yaz(sayi,isim_listesi)
print(sonuc)


"""

"""
### Belirsiz sayıda parametre alan fonksiyon ###

def  topla(*sayilar):# '*' ifadesi n sayıda parametre alınacağını tanımlar.
	toplam = 0
	
	for sayi in sayilar:
		toplam += sayi
		
	return  toplam


sonuc = topla(44,55,66,99,33,22,44)
print(sonuc)

"""

# Kendisine gönderilen karakter,en,boy parametrelerine göre
# ekrana karakterden oluşan bir dikdörtgen oluşturan fonksiyonu yazınız.
"""
oooooooo
oooooooo
oooooooo
oooooooo


def  ciz(en,boy):
	for i in range(en):
		print("#"*boy)
		
ciz(10,50)

"""
"""
kare = pow(4,2)
print(kare)
def kare_al(s1:int, s2:int):
	return  s1 ** s2


kare2 =  kare_al(4,2)
print(kare2)
"""
## Bir müşterim dolar'ını euro'ya çevirmek
# istiyor ben dolar/euro endeksini bilmediğim için doları tl => tl euro
# 1 $ => 16.83₺
# 1€ => 17.55 TL
"""
dolar_kur = 18.43
euro_kur = 17.84

def dolar_to_tl( dolar, kur ):
	return dolar * kur

def tl_to_euro( tl, kur ):
	return (tl / kur)

tl = dolar_to_tl( 100, dolar_kur )
print( "100 $ => ", tl )

euro = tl_to_euro( 100, euro_kur )
print( "100 ₺  => ", euro )
"""
# Kendisine gönderilen sınırsız sayının ortalamasını döndüren fonksiyonu yazınız..
## 1,2,3 => 1+2+3 /3
def ortalama(*sayilar):
	toplam = 0
	
	for sayi in sayilar:
		toplam += sayi
	
	return toplam / len(sayilar)


sonuc =  ortalama(1,2,3)
print(sonuc)