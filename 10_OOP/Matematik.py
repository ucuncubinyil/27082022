class Matematik( ):
	
	@classmethod
	def topla( cls, *sayilar ):
		toplam = 0
		for sayi in sayilar:
			toplam += sayi
		return toplam
	
	@classmethod
	def cikar( cls, s1: int, s2: int ):
		return s2 - s1
	
	@classmethod
	def carp( cls, *sayilar ):
		carpim = 1
		for sayi in sayilar:
			try:
				if sayi == 0:
					raise RuntimeError( "Sayı Sıfır Olamaz !" )
				carpim *= sayi
			except RuntimeError:
				print( "Sayı Sıfır Olamaz !" )
		return carpim
	
	@classmethod
	def bol( cls, s1: int, s2: int ):
		sonuc = 0
		try:
			sonuc = s1 / s2
		except ZeroDivisionError:
			print( "Hiç bir sayı sıfıra bölünemez" )
		
		return sonuc
