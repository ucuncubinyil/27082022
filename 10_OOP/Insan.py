class Insan():
	ad = str()
	soyad = str()
	
	@classmethod
	def konus( cls, insan):
		print(f" Ad: {insan.ad} Soyad: {insan.soyad} ")
		
	
	def konusma( self ):
		print(f" Ad: {self.ad} Soyad: {self.soyad} ")
	
	@classmethod
	def yazdir( cls, liste: list):
		for insan in liste:
			print(insan.ad, insan.soyad)

	@classmethod
	def kaydet( cls, liste: list):
		a = Insan()
		a.ad = input("Bebeğin Adı: ")
		a.soyad = input("Bebeğin Soyadı: ")
		liste.append(a)