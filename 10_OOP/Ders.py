# Bir Ders class'ı oluşturunuz.
# class Ders: DersAdi,DersSaati,DersOgretmeni,DersBaslamaTarihi
# class'dan bir nesne oluşturulduğunda field'lar oluşturularak içleri doldurulsun
# ve  Dersler.txt dosyasına kayıt işlemi gerçekleştirilsin.
# Başka class başka bir dosyada tutulsun.

class Ders():
	def __init__(self):
		self.ders_adi =  input("Ders Adı: ")
		self.ders_saati =  input("Ders Saati: ")
		self.ders_ogretmeni =  input("Ders Öğretmeni: ")
		self.ders_baslama_tarihi =  input("Ders Başlama Tarihi: ")
		
	
	def ders_kaydet( self ):
		try:
			import os
			dizin =  "C:\\TEST\\"
			
			if not os.path.exists(dizin):
				os.mkdir(dizin)
				
			kayit_edilecek_dosya =  dizin +"Dersler.txt" #C:/TEST/Dersler.txt
			
			dosya =  open(kayit_edilecek_dosya, mode="a+",encoding="utf-8")
			yazi = f"""
Ders Adı                :{self.ders_adi}
Ders Öğretmeni          :{self.ders_ogretmeni}
Ders Saati              :{self.ders_saati}
Ders Başlama Tarihi     :{self.ders_baslama_tarihi}
"""
			dosya.write(yazi)
			dosya.close()
		except Exception:
			print("Dosya kayıt edilirken hata oluştu")