################## DICTIONARY (SOZLUK) ########################
"""
sozluk = {} # boş liste oluşturma
sozluk = dict()# boş liste oluşturma

sozluk = {"anahtar":"deger","anahtar":"deger","anahtar":"deger","anahtar":"deger" }
"""

"""
sozlugum = { "ad": "Mehmet Nuri", "soyad": "Öztürk", "dogum_tarihi": "20.11.1993" }

print( sozlugum )
print(sozlugum["dogum_tarihi"])
# print(sozlugum["dogum_tarihis"])
print(sozlugum.keys()) # anahtarlari verir
print(sozlugum.values()) # degerler
print(sozlugum.items())

if  "dogum_tarihi"  in sozlugum.keys():
	print(sozlugum["dogum_tarihi"])
	
sozlugum["ad"] = "Ahmet"
print(sozlugum)

sozlugum.clear() #sözlüğü temizler
print(sozlugum)

sozlugum = { "ad": "Mehmet Nuri", "soyad": "Öztürk", "dogum_tarihi": "20.11.1993" }
print("ad" in sozlugum)
print("ad" in sozlugum.keys())
print("Mehmet Nuri" in sozlugum.values())

"""
"""
s1 = { "ad": "Selim", "soyad": "Kaçar" }
s2 = {  "soyad": "Kaçar","ad": "Selim" }
s3 = { "soyad": "Varan", "ad": "Selim" }

print("s1 s2 ye eşit midir ? ", s1 == s2)
print("s1 s3 e eşit midir ?", s1 == s3)

sozlugum = { "ad": "Mehmet Nuri", "soyad": "Öztürk", "dogum_tarihi": "20.11.1993" }

for i in sozlugum.values():
	print(i)
"""
"""
numaralar = [ "555 666 77 88", "556 999 66 33" ]
sozlugum = { "ad": "Ahmet", "soyad": "Çam", "numaralar": numaralar }
print(sozlugum)

print(sozlugum.values())

for x in sozlugum["numaralar"]:
	print(x)

kullanici = dict()
ad =  input("AD")
kullanici["ad"] = ad

soyad =  input("SOYAD")
kullanici["soyad"] = soyad

yas =  int(input("YAŞ"))
kullanici["yas"] = yas
print(kullanici)

"""

"""
s1 = { "ad": "Selim", "soyad": "Kaçar" }
s2 = { "soyad": "Kaçar", "ad": "Selim" }
s3 = { "soyad": "Varan", "ad": "Selim" }
s4 = { "zz": "aa", "aa": "aa" }

s3.update( s1 )  # sözlüğü diğer sözlüğe göre kopyalar
print( s3 )

s4.clear( )
# for k in s4.keys():
# 	print(k)
# 	s4.pop(k)

for k, v in s1.keys( ), s1.values( ):
	s4[ k ] = v
print( s4 )

# del s4 # ram de sil
# print(s4)

s3.pop( "ad" )
print( s3 )

sozluk = { }
list1 = [ 1, 2, 3, 4, 5 ]
list2 = [ 6, 7, 8, 9, 0 ]
list3 = [ 11, 22, 33 ]

sozluk = { "x": list1, "y": list2, "z": list3 }

sozluk["x"] = list1
sozluk["y"] = list2
sozluk["z"] = list3
print(sozluk)
"""
#### SORU: Kullanıcıdan alınan ad,soyad,yas,cinsiyet
# bilgilerini Personel isimli bir sözlükte saklayın ve
# ad soyad bilgisini sözlükten alarak ekrana yazdırınız.

"""
Personel    = dict( )
ad          = input( "Ad" )
soyad       = input( "Soyad" )
yas         = int( input( "Yaş" ) )
cinsiyet    = input( "Cinsiyet" )

Personel["ad"]          = ad
Personel["soyad"]       = soyad
Personel["yas"]         = yas
Personel["cinsiyet"]    = cinsiyet

print(f"Ad: {Personel['ad']},  Soyad: {Personel['soyad']} ")
"""

# SORU: Bir firmanın İnsan kaynakları,Bilgi İşlem ve
# Muhasebe departmanlarının çalışan listelerini yöneticiden
# isteyerek bir dict atınız
# ve ekrana istenilen bölümdeki çalışanları listeyiniz.

"""
IK=list()
IT=list()
MHSB=list()
firma=dict()

for i in range(1):
    IK.append(input("İnsan Kaynakları Personel Ad Soyad"))
    IT.append(input("Bilgi İşlem Personel Ad Soyad"))
    MHSB.append(input("Muhasebe Personel Ad Soyad"))

firma["IK"] = IK
firma["IT"] = IT
firma["MHSB"] = MHSB

secim =  input("Lütfen personel listesine ulaşmak istediğiniz departmanı yazın
        IK, IT, MHSB")

for i in firma[secim]:
    print(i)
"""

yasakli_karakter = [ 'ı', 'ş', 'ğ', 'ö', 'ü', 'ç' ]
uygun_karakter = [ 'i', 's', 'g', 'o', 'u', 'c' ]

metin = input( "Test için gir: " )

for i in metin:
	if i in yasakli_karakter:
		indx = yasakli_karakter.index( i )
		krkt = uygun_karakter[ indx ]
		print( krkt )
		metin = metin.replace( i, krkt )
print( metin )

"""
# SORU: sözlük uygulaması olsun Tr-Eng
#       sözlük={"siyah":"black"...}
#       kullanıcı 4 seçenekli bir menü verelim
#          1-Arama
           2-Çıkarma
           3-Listeleme
           4-Çıkış

        Kullanıcı 1'e basarsa ->
            - Aranacak kelimeyi giriniz:
            - Bu kelime dict varsa english karşılığını yazılır.
            - Yoksa uygulamayı geliştirmek istermisiniz?
                - E ise bu kelimenin ingilizce karşılığını alırız ve sözlüğe eklenir.
                - H ise Peki.. 
        Kullanıcı 2'e basarsa -> 
            - Çıkarılmak istenen kelime:
            - Kelime sözlükte varsa çıkartılır.
            - Yoksa uyarı verilir.
        Kullanıcı 3'e basarsa ->
            - Tum key value lar listenilir.
            - KEY -> VALUE
        Kullanıcı 4'e basarsa ->
            - Döngü sonlanır..
"""

liste = [ 1, 2, 3, 4 ]

for i in range(len(liste)):
	print(i, liste[i])
