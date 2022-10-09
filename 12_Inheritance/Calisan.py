class Calisan( ):
	
	def __init__( self, ismi:str, maas, departman ):
		self.ismi = ismi
		self.maas = maas
		self.departman = departman
	
	def bilgi_goster( self ):
		print( "Çalışan bilgileri" )
		print( f"İsim: {self.ismi} Maaş:{self.maas} Departman: {self.departman}" )
	
	def departman_degis( self, yeni_departman ):
		print( "Departman değiştiriliyor" )
		self.departman = yeni_departman
