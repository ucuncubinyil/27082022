class Ogrenci():
	ad = str( )
	soyad = str( )
	tc = 0
	dogum_tarihi = str( )
	
	# self=> nesneyi temsil ediyor ve bu methodun nesne üzerinden kullanılabileceğini gösteriyor.
	def bilgi_yaz( self ):
		print( f"AD:{self.ad} SOYAD: {self.soyad} TC: {self.tc} Doğum Tarihi: {self.dogum_tarihi}" )

	
	@classmethod  # cls => cls ifadesi Class üzerinden çağrılabileceğini belirtir.
	def ara( cls, ad, liste ):
		for i in liste:
			if i.ad == ad:
				print( f"AD:{i.ad} SOYAD: {i.soyad} TC: {i.tc} Doğum Tarihi: {i.dogum_tarihi}" )

	
