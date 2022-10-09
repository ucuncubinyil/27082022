from Arac import Arac

class Kamyon(Arac):
	
	def __init__(self):
		super().__init__()
		self.tasima_kapasitesi =  int()
		self.yakit_depo_sayisi =  int()
	
	def  bilgi_yaz( self ):
		super().bilgi_yaz()
		print(f"""
Taşıma Kapasitesi                   :{self.tasima_kapasitesi}
Depo Sayısı                         :{self.yakit_depo_sayisi}
		""")