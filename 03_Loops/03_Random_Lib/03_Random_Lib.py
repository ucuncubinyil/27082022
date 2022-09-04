import random as kutuphane
print(kutuphane.random()) #  0-1 arasında rastgele sayı üretir
print(kutuphane.randint(0,100)) # Verilen aralık içinde rastgele tam sayı üretir
print(kutuphane.uniform(0,100)) # Verilen aralık içinde noktalı sayı üretir
print(kutuphane.randrange(1,100)) # Verilen aralıkta  tam sayı üretir min ve max dahil değildir
print(kutuphane.randrange(1,100,3)) # Verilen aralıkta tam sayı üretir 3 e bölündüğünde kalanı 1 olanları üretir


print( kutuphane.uniform( 100000.0000, 999999.9999 ) )
