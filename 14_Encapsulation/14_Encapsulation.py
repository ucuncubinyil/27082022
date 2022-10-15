"""
from Kapsul import Kapsul

kapsul1 =  Kapsul()
kapsul1.ekrana_yaz()

kapsul1.set_gizli_ozelik_1("Kerim")
print(kapsul1.get_gizli_ozelik1())

kapsul1.set_gizli_ozellik_2("Durmaz")
kapsul1.ekrana_yaz()
"""
"""
from Banka import Banka

ahmet_bey = Banka()
ahmet_bey.yaz()

"""
"""
from Personel import Personel

nesne = Personel("Sevgi")
print(nesne.ad)

nesne.ad =  "Ayşe"
print(nesne.ad)
"""
# Öğrenci vize-final ortalaması hesaplayan programı yaz

"""
from Universite import Universite

ali_can =  Universite()
ali_can.vize = 500
ali_can.final = 300

ali_can.ortlama()

"""

from Musteri import Musteri

ali =  Musteri()
ali.ad = "Ali"
ali.soyad = "ÖZTÜRK"
ali.telefon = "5555555555"
ali.mail_adresi = "info@mehmetnuri.net"
ali.bilgi_yaz()