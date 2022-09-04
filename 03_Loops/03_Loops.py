# DÖNGÜLER
# WHILE  -  FOR

# 1 ile 10 arasındaki sayıları ekrana yazdırınız.
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)

"""
while(kosul):
    kosul true olduğu sürece bu kod bloğu çalışır.
"""
"""
i = 1
while (i < 11):
	print( i )
	i += 1
"""
# BREAK => Bu komut döngüyü kırmaya yarar.
"""
while True: # program kapatılana kadar yada döngü kırılana kadar çalıştırr
	print("Mehmet Nuri")
	break
"""
# 90 ile 100 arasındaki sayıları ekrana yazdırınız.

# Ödev 1-1000 arasındaki tek ve çift sayıların toplamlarını ayrıü
# ayrı hesaplayan kodu yazınız if else ve while kullanın sadece
"""
sayi= 90

while (sayi <=100):
	print(sayi)
	sayi += 1
"""
# 70 ile 55 arasındaki sayılarda 3'e tam bölünenleri ekrana yazdırınız
"""
sayi = 70

while (sayi > 55):
	if sayi % 3 == 0:
		print( sayi )
	sayi -= 1
"""
# SORU: 7 - 77 arasındaki tüm sayıların toplamını ekrana yazdırınız.
"""
toplam = 0
sayi = 7
while (sayi <= 77):
	toplam += sayi
	print(sayi)
	sayi += 1
print(toplam)
"""
# SORU: 1'den kullanıcının girdiği sayıya kadar
# olan sayıların karesini ekrana yazdıran program.
"""
baslangic = 1
bitis = int(input("Lütfen sayı giriniz: "))
while (baslangic < bitis):
	print(baslangic **2)
	baslangic += 1
"""
# Ödev: 1'den kullanıcının girdiği sayıya kadar
# olan sayıların eğer tek ise karesini , çift ise küpünün
# toplamını ayrı ayrı hesaplayan kod parçacığı

# CONTINUE: Run time da continue keyword'ü çalışırsa program
# bulunduğu yerden döngüye geri döner
"""
sayi = 1

while (sayi < 10):
	if sayi == 2:
		continue
	if sayi  == 5:
		break
	print(sayi)
	sayi += 1
"""

"""
sayi = 1

while (sayi < 10):
	if sayi == 2:
		pass
	if sayi  == 5:
		break
	print(sayi)
	sayi += 1
"""
# SORU: Klavyeden girilen deger 'çık' ise döngüden
# çıkılacak. değilse toplama işlemi gerçekleştirilecek.
"""
toplam = 0
while True:
	cevap =  input("Bir sayı girin veya çıkmak için çık yazın")
	if cevap == "çık":
		break
	else:
		toplam += int(cevap)
		continue
print(toplam)
"""

# SORU: 1-100 arasındaki sayıların toplayan program.
# Ancak aşağıdak durumlarda sayıyı toplama eklemeyecek
# * Sayı 7'nin katı ise toplama eklenmesin
# * Sayı'nın 3 katının 7 fazlası 37'nın katı ise döngüden çıkılsın.
"""
sayi = 1
toplam = 0
while sayi <= 100:
	if sayi % 7 == 0:
		sayi += 1
		continue
	kat = 3 * sayi + 7
	if kat % 37 == 0:
		print( "Kat", kat )
		print( kat )
		break
	toplam += sayi
	sayi += 1

print( f"Toplam  : {toplam}" )
"""
# SORU: Klavyeden girilen sayının faktöriyelini hesaplayan program
# Faktoriyel => 5! => 1*2*3*4*5=120
"""
sayi = int( input( "Faktöryeli hesaplanacak sayıyı giriniz " ) )
sonuc = 1
sayac = 1
while sayac <= sayi:
	sonuc *= sayac  # sonuc = sonuc * sayac
	sayac += 1
print( sonuc )
"""

# SORU:
"""
    Kullanıcıadı/Email ve şifre ile giriş sağlanacak. 3 defa giriş hakkı vardır.
        Giriş Başarılı ise ekrana "Giriş Başarılı" yazsın
        Değilse
            Kullanıcıya kayıt olmak ister misiniz?
                Hayır ise PEKİ!!!
                Evet Kullanıcıadı, ad, soyad,email,şifre ve şifre tekrarı
                alarak kayıt yapalım.
                    şifre ve şifretekrarın aynı olması
"""
"""
kmail = "info@mehmetnuri.net"
kadi = "mehmetnuri"
ksifre = "123456"
hak = 3
giris_basarili =  False

while True:
	
	print( "########## KULLANICI GİRİŞİ ##########" )
	
	while hak > 0:
		
		username = input( "Kullanıcı adınızı veya email adresinizi giriniz: " )
		password = input( "Şifrenizi giriniz: " )
		
		hak -= 1
		if (kadi == username or kadi == kmail) and (password == ksifre):
			print( "Giriş başarılı" )
			giris_basarili =  True
			
			break
		else:
			print( f"Giriş bilgileriniz hatalı kalan giriş hakkı {hak}  " )
			continue
	if hak == 0:
		print( "Giriş hakkınız kalmadı" )
		break
		
	if giris_basarili == True:
		break
		
"""

# SORU: Kullanıcıdan alınan sayının asal olup olmadığını ekran yazdırınız.
# Asal sayı 1 ve kendisinden başka hiç bir sayıya bölünmeyen sayıdır. 13

asal_mi = True
i = 2
s = int( input( "Asallık kontrolü yapılacak olan sayıyı giriniz:" ) )

while i < s:
	if s % i == 0:
		asal_mi = False
		break
	i += 1

if asal_mi == True:
	print( "Sayı alasal" )
else:
	print( "Sayı alasal değil" )
