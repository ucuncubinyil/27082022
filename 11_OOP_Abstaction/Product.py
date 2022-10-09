from Base import Base
#CRUD(Create Read Update Delete)

class Product(Base):
	
	def __init__( self ):
		super( ).__init__( )
		self.price = 0.0
		self.stock =  0
	
	def kaydet( self ):
		print(self.id)
		print(self.ad)
		print(self.price)
		print(self.stock)
	
	def guncelle( self ):
		pass
	
	def sil( self ):
		pass
	
	def listele( self ):
		pass