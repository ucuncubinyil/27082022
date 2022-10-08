###################################################################
############### OOP: Object Oriented Programming ##################
################ Nesneli Yöneliklik Programlama ###################
###################################################################

'''
OOP: büyük projeler yazılacağı zamanlarda, proje temelini oluşturma aşamasından
başlayarak analiz sentez kodlama sınama ve onarım gibi yaşam döngüsü adımlarında daimi olarak
uyugulanması ve takip edilmesi gerekli bir yapıdır.
En büyük kazancı proje temelini oluşturan yapıların bir bütün halinde(object)
tutulması ve yapınların özelliklerinin(field) alt başlıklar halinde yapıya özel olmasını sağlar.
Kayıt güncelleme,silme veya okuma işlemlerinde object (nesne) sayesinde veri bütünlüğü sağlanmış
ve tek bir işlemle manipüle edeilmiş olur.
'''

## Bir okulunuz olduğunu ve öğrenci kaydı yapılacağını düşünelim.
# Her öğrencinin ad,soyad,tc,dogumtarihi gibi bilgileri kayıt edilecektir.

"""
ad = "Mehmet Nuri"
soyad =  "Öztürk"
tc = 246545
dogum_tarihi =  "20.11.1993"


ad = "Ferdi"
soyad =  "Arslandaş"
tc = 654646541635
dogum_tarihi =  "21.09.1974"
"""
"""

from Ogrenci import Ogrenci


ogrenci_listesi =  list()



ahmet =  Ogrenci()
ahmet.ad = "Ahmet"
ahmet.soyad =  "Kalas"
ahmet.tc =  1365476
ahmet.dogum_tarihi = "10.10.1965"
ahmet.bilgi_yaz()
ogrenci_listesi.append(ahmet)


kerim =  Ogrenci()
kerim.ad = "Kerim"
kerim.soyad =  "Kalas"
kerim.tc =  1365476
kerim.dogum_tarihi = "10.10.1965"
kerim.bilgi_yaz()
ogrenci_listesi.append(kerim)

Ogrenci.ara("Kerim", ogrenci_listesi)

"""

"""
from Insan import Insan


bebek_listesi =  list()

a = Insan()
a.ad = input("Bebeğin Adı")
a.soyad = input("Bebeğin Soyadı")
bebek_listesi.append(a)
Insan.yazdir(bebek_listesi)


while True:
	Insan.kaydet(bebek_listesi)
	cevap =  input("Eklemeye devam etmek istiyor musunuz?(E/H)").upper()
	if cevap == 'E':
		continue
	else:
		break

Insan.yazdir(bebek_listesi)
Insan.kaydet(bebek_listesi)
Insan.yazdir(bebek_listesi)

"""
"""
from Buzdolabi import Buzdolabi

arcelik = Buzdolabi( ) # instance alıyoruz
arcelik.marka = "Arçelik"
arcelik.model = "AXGH656"
arcelik.fiyat = 7652.36

arcelik.bilgi_yaz()
arcelik.fiyat_hesapla(arcelik.fiyat, 2)

Buzdolabi.fiyat_hesapla(arcelik.fiyat,2)
"""
"""
from  Matematik import Matematik


topla = Matematik.topla(1,2,3,4,5,6,7,8,9,10)
print(topla)

cikar =  Matematik.cikar(2,3)
print(cikar)

carp = Matematik.carp(1,6,2)
print(carp)

bol =  Matematik.bol(1,2)
print(bol)

"""

from Ders import Ders

ders =  Ders()
ders.ders_kaydet()