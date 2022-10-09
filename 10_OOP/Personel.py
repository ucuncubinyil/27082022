# SORU:
"""
Personel isimli bir class tanımlayın
Nesne Nitelikleri: ad,soyad,tc,telefon,adres,maas
__init__ fonksiyonu ile kullanıcıdan bu özellikler sorularak doldurulsun

Kaydet() isimli method Personel.txt adında bir dosyaya kaydetsin
Bir tane sınıf üzerinden erişebilir Listele() adında bir method tanılayın dosyadaki verileri okuma işlemi gerçekleştirsin

"""

import os
class Personel( ):
	def __init__( self ):
		self.ad = input( "Personel Adı: " )
		self.soyad = input( "Personel Soyadı: " )
		self.tc = input( "Personel T.C.: " )
		self.telefon = input( "Personel Telefon: " )
		self.adres = input( "Personel Adres: " )
		self.maas = float(input( "Personel Maas: " ))
	
	def kaydet( self ):
		try:
			dizin =  "C:\\TEST\\"
			if not os.path.exists(dizin):
				os.mkdir(dizin)
			kayitli_dosya =  dizin+"Personel.txt"
			dosya = open(kayitli_dosya, mode="a+", encoding="utf-8")
			dosya.write(f"Ad: {self.ad}\tSoyad:{self.soyad}\t"
			            f"T.C.:{self.tc}\t"
			            f"Adres:{self.adres}\tMaaş:{self.maas}")
			dosya.close()
		except Exception:
			print("Dosya kayıt edilirken hata oluştu")
	
	@classmethod
	def oku( cls ):
		try:
			dosya =  open("C:\\TEST\\Personel.txt",
			              mode="r",encoding="utf-8")
			satirlar =  dosya.readlines()
			dosya.close()
			
			for satir in satirlar:
				print(satir)
		except FileNotFoundError:
			print("Dosya Bulunamadı")
		except Exception:
			print("Dosya okunurken hata oluştu")
			