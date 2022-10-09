from  abc import ABC, abstractmethod

class Base(ABC):
	def __init__(self):
		self.id = str()
		self.ad = str()
		self.eklenme_tarihi = str()
		self.guncellenme_tarihi=str()
		self.silinme_tarihi = str()
	
	@abstractmethod
	def  kaydet( self ):
		pass
	
	@abstractmethod
	def guncelle( self ):
		pass
	
	@abstractmethod
	def  sil( self ):
		pass
	
	@abstractmethod
	def listele( self ):
		pass