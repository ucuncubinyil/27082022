# SORU:
# 1 1-15 arasında 5'er adet sayı üretip 2 farklı kümeye kaydediniz.
# Daha Sonra iki kümeyi ekrana yazdırınız.

from random import randint

# 1. yöntem
kume1 = set( )
kume2 = set( )

for i in range( 5 ):
	
	while True:
		sayi = randint( 1, 15 )
		if len( kume1 ) < 6:
			if sayi not in kume1:
				kume1.add( sayi )
				break
			else:
				print( "Bu sayı kümede var" )
		else:
			continue
	
	while True:
		sayi = randint( 1, 15 )
		if len( kume2 ) < 6:
			if sayi not in kume2:
				kume2.add( sayi )
				break
			else:
				print( "Bu sayı kümede var" )
		else:
			continue

print( kume1 )
print( kume2 )

## 2. yöntem
kume1 = set( )
kume2 = set( )

while len( kume1 ) < 5:
	sayi = randint( 1, 15 )
	if sayi not in kume1:
		kume1.add( sayi )

while len( kume2 ) < 5:
	sayi = randint( 1, 15 )
	if sayi not in kume2:
		kume2.add( sayi )

print( kume1 )
print( kume2 )
