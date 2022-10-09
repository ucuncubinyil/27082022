from abc import ABC, abstractmethod


class Animal( ABC ):
	
	@abstractmethod
	def drik( self ):
		pass
	
	@abstractmethod
	def walk( self ):
		pass
	
	@abstractmethod
	def sleep( self ):
		pass
