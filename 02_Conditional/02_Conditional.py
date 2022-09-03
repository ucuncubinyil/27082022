##################### AKIŞ KONTROL : IF ELIF ELSE ########################################
# Program akışında bir sonuc,durum ve değere göre program akışı
# devam edecek ise if elif else deyimleri kullanılır.
# Karar yapıların if ve else 1 kez tanımlanır.
# alternatif bütün durumlar elif keyword'ü tekrar tekrar
# yazılarak kullanılablir

"""
if koşul:
	yapılmak istenilen
else:
	eğer koşul doğru değil ise

"""
#
# sayi = 6
#
# if sayi > 6:
# 	print( "Sayı değişkeni 6 dan büyüktür" )
# elif sayi == 6:
# 	print( "Sayı değişkeni 6 ya eşittir" )
# else:
# 	print( "Sayı değişkeni 6 dan küçüktür" )

# Haftanın kaçıncı günüdeyiz? ekrana gün adını yazdıralım

# gun = int( input( "Haftanın gün sayısını yazın(1-7)" ) )
# if gun == 1:
# 	print( "Pazartesi" )
# elif gun == 2:
# 	print( "Salı" )
# elif gun == 3:
# 	print( "Çarşamba" )
# elif gun == 4:
# 	print( "Perşembe" )
# elif gun == 5:
# 	print( "Cuma" )
# elif gun == 6 or gun == 7:
# 	print( "Haftasonu" )
# else:
# 	print( "Hatalı gün girişi" )

# SORU: Klavyeden girilen değer: 100'den büyükse karesini,
# küçükse küpünü ekrana yazdıran prog.
# x =  int(input("Sayi giriniz:"))
# if x > 100:
# 	print(x**2) # x**2 demek x in karesini al demektir
# elif x < 100:
# 	print(x**3)# x**3 demek x in küpünü al demektir
# else:
# 	print("x 100 e eşittir") # eğer sayi 100 den buyuk veya küçük değil ise

## MOD ALMA
# sayi = 5
#
# print(5%2)


# Klavyeden girilen sayı çift ise:
# Ekrana sayı çifttir yazılacak,
# değilse tektir yazılacak
# çift ise 4 ile çarpsın, tek ise 9 ile toplasın
"""
sayi =  int(input("Sayı: "))

if sayi % 2 == 0:
	print("Sayı çiftir")
	print(sayi*4)
else:
	print("Sayı tektir")
	print(sayi+9)
"""

# Kullanıcıdan alınan sayının aralığını belirleyiniz
#  0-10  11-20
"""
sayi = int( input( "Sayı: " ) )

if 0 < sayi and sayi < 11:
	print( "Sayı 0-10 aralığındadır" )
elif 10 < sayi and sayi < 21:
	print( "Sayı 10-20 aralığındadır" )
"""

# Klavyeden girilen 4 sayıdan tek ve çift olanları ayrı
# ayrı toplayarak ekrana yazdırınız..
"""
tek_toplam = 0
cift_toplam = 0

s1 = int( input( "Sayi1" ) )
if s1 % 2 == 0:
	cift_toplam += s1  # cift_toplam =  cift_toplam + s1
else:
	tek_toplam += s1

s2 = int( input( "Sayi2" ) )
if s2 % 2 == 0:
	cift_toplam += s2
else:
	tek_toplam += s2

s3 = int( input( "Sayi3" ) )
if s3 % 2 == 0:
	cift_toplam += s3
else:
	tek_toplam += s3

s4 = int( input( "Sayi4" ) )
if s4 % 2 == 0:
	cift_toplam += s4
else:
	tek_toplam += s4
	
print(f"Tek sayıların toplamı {tek_toplam}")
print(f"Çift sayıların toplamı {cift_toplam}")
"""

## Kullanıcıdan vize final not girilmesi istensin
# not aralığı 0 ile 100 arasında olmalıdır.
## vize ve finalin ortalaması alınsın.
## 0-44 : Kaldınız
## 45-69: Geçtiniz
##7 0-84: İyi
## 85-100: Pekiyi
"""
vize = float( input( "Lütfen vize notunuzu giriniz:" ) )
final = float( input( "Lütfen final notunuzu giriniz:" ) )

if (vize <= 100 and vize >= 0) and (final <= 100 and final >= 0):
	ortalama = (vize * 0.4) + (final * 0.6)
	
	if ortalama >= 0 and ortalama < 45:
		print( "Kaldınız" )
	elif ortalama >= 45 and ortalama < 70:
		print( "Geçtiniz" )
	elif ortalama >= 70 and ortalama < 85:
		print( "İyi" )
	else:
		print( "Pekiyi" )
else:
	print( "Vize ve final notları  0-100 aralığında olmalıdır" )
print( ortalama )
"""

# Kullanıcıdan isim,yaş,maaşve çocuk sayısı alalım

"""
    Eğer kullanıcının yaşı 45'in altındaysa;
        çocuk sayısına bakılacak ve çocuk sayısı 3^ten az ise çocuk başına 250₺,
         değilse çocuk başına 200₺ maaşa eklenecek
    Eğer kullanıcının yaşı 45 ve üzerinde ise:
        çocuk başına para verilmeyecek direk 500₺ maaşa eklenecek.
    Ekrana "Nesrin Yılmaz Maaşınız: 4000₺" yazılacak.
"""

"""
isim = input( "İsminiz: " )
yas = int( input( "Yaşınız: " ) )
maas = float( input( "Maaşınız " ) )
cocuk_sayisi = int( input( "Çocuk saysı" ) )

if yas < 45 and yas > 18:
	
	if cocuk_sayisi < 3 and cocuk_sayisi >= 0:
		maas += cocuk_sayisi * 250
	else:
		maas += cocuk_sayisi * 200

elif yas >= 45:
	maas += 500

else:
	print( "Belirtilen yaş aralığında değilsiniz." )

print( f"İsim :{isim}, Yaş: {yas}, Maaş: {maas} ₺, Çocuk Sayısı: {cocuk_sayisi}" )
"""

# Kullanıcı Gİriş Paneli Tasarlayınız.

"""
    Kullanıcıadı/Email ve şifre ile giriş sağlanacak
        Giriş Başarılı ise ekrana "Giriş Başarılı" yazsın
        Değilse
            Kullanıcıya kayıt olmak ister misiniz?
                Hayır ise PEKİ!!!
                Evet Kullanıcıadı, ad, soyad,email,şifre ve şifre tekrarı alarak kayıt yapalım.
                    şifre ve şifretekrarın aynı olması
"""

"""
kadi = "mehmetnuri"
ksifre = "123456"
email = "info@mehmetnuri.net"

print( "------------------------------KULLANICI GİRİŞİ------------------------------" )

user_name = input( "Kullanıcı Adı /  Email: ")
password =  input("Şifreniz: ")

if (  (user_name == kadi or email == user_name)  and (password == ksifre)  ):
	print("Hoş geldiniz!")
else:
	cevap = input("Kayıt olmak ister misiniz ? (E/H)").upper()
	
	if cevap == "E":
		kullanici_adi =  input("Kullanıcı adı giriniz: ")
		email = input("E-Mail adresinizi giriniz: ")
		sifre1 = input("Şifreniz: ")
		sifre2 =  input("Şifreniz Tekarar: ")
		
		if sifre1 == sifre2:
			print("Hoş geldiniz")
		else:
			print("Girilen şifreler eşleşmiyor")
	elif cevap == "H":
		print("Peki! Hoşçakalın")
	
	else:
		print("Hatalı seçim")
	"""

# Girilen 3 sayıyı büyüklük olarak karşılaştıran python uygulamasını yapınız.

a = int( input( "1." ) )
b = int( input( "2." ) )
c = int( input( "3." ) )

if a > b and a > c:
	print( f"En büyük sayı{a}" )
elif b > a and b > c:
	print( f"En büyük sayı{b}" )
else:
	print( f"En büyük sayı{c}" )
