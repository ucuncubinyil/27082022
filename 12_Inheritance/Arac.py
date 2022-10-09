from datetime import datetime as dt

class Arac():
	
	def __init__(self):
		self.marka = str()
		self.model = str()
		self.renk =  str()
		self.uretim_yili = int()
		self.fiyat =  float()
		self.ilan_tarihi = dt.today().date()
		
	def bilgi_yaz( self ):
		print(f"""
Marka                               :{self.marka}
Model                               :{self.model}
Renk                                :{self.renk}
Üretim Yılı                         :{self.uretim_yili}
Fiyat                               :{self.fiyat}
İlan Tarihi                         :{self.ilan_tarihi}""")

