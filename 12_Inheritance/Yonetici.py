from Calisan import Calisan

class Yonetici(Calisan):
	
	def __init__(self, isim, maas,departman,kisi_sayisi):
		super().__init__(isim,maas,departman)
		self.kisi_sayisi = kisi_sayisi
	
	def bilgi_goster( self ):
		print("Çalışan bilgileri")
		print(f"İsmi:{self.ismi}\t Maaş:{self.maas}\t"
		      f"Departman:{self.departman}\t"
		      f"Kişi Sayısı:{self.kisi_sayisi}\t")
		
	def zam_yap( self, zam_miktari ):
		print("Zam uygulanıyor")
		self.maas += zam_miktari
	
	def  departman_degis( self, yeni_departman ):
		super().departman_degis(yeni_departman)