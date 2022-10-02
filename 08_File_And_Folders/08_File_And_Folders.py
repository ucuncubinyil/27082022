# DİZİN İŞLEMLERİ

"""
system() => Kullanırken son derece dikkatli olunması gereken bir metot
getcwd() => Pythonun hangi dizinde çalıştığı bilgisini verir
chdir() => Dizin değiştirmeye yarar
listdir() => Bulunduğumuz dizindeki elemanları ve klasörleri listeler
mkdir() => Dizin oluşturmaya yarar
rmdir() => Dizin silmeye yarar son derece dikkatli olunması gerek
rename() => Dizini yeniden adlanıdırmak için
path() => Dizinin veya dosyanın var olup olmadığını kontrol eder

"""

import os
# from  os import *
#
# #Hangi dizindeyim ?
# print(getcwd()) # C:\sada\asd
#
# #Dizin değiştirme
# chdir("/home/mehmet/PycharmProjects")
# # chdir("C:\\")
# print(getcwd())
# print(listdir())
#
#
# # mkdir(getcwd()+"\\TEST") #Windows kullanıcıları için
# mkdir(getcwd()+"/TEST")
# print(listdir())


# C -> TEST -> GUN-AY-YIL klasör oluşturun

from datetime import *

# def  klasor_olustur():
#
#
#     zaman =  date.today()
#
#     klasor_adi = zaman.strftime("%Y-%m-%d")
#     dosya_yolu =  "/home/mehmet/PycharmProjects/TEST/"+klasor_adi
#
#     if not path.exists("/home/mehmet/PycharmProjects/TEST"):
#         os.mkdir("/home/mehmet/PycharmProjects/TEST")
#         print("TEST isimli klasör yoktu oluşturdum")
#
#
#     if not path.exists(dosya_yolu):
#         os.mkdir(dosya_yolu)
#
#
# klasor_olustur()
#
#

# DOSYA İŞLEMLERİ


"""
DOSYA YETKİ MODLARI

w:(write)  Sadece yazma yetkisi ile dosyayı açar. Dosya var ise siler yeniden oluşturur.
r: (read) Sadece okuma yetkisi ile açar
a: Sona ekleme yetkisi ile açar. Dosya yoksa oluşturur
x: Yazma yetkisi ile açar dosya yoksa oluşturur varsa hata verir.


w+ = yazma + okuma yetkisi ile açar . Dosya var ise siler ve yeniden oluşturur.
r+ = okuma+yazma yetkisi ile açar
a+ =  ekleme+okuma yetkisi ile açar
"""

# from  datetime import *
# # from os import chdir,getcwd, path
# zaman = datetime.today()
# import os
#
# klasor_adi = zaman.strftime("%Y-%m-%d")
# klasor_yolu = "/home/mehmet/PycharmProjects/TEST/" + klasor_adi
#
# dosya_yolu =  klasor_yolu + "/dosya.txt"
#
# os.chdir(klasor_yolu)
#
#
# #/home/mehmet/PycharmProjects/TEST/02-10-2022/dosya.txt
#
# if not os.path.exists( dosya_yolu ):
# 	dosya = open( dosya_yolu, mode="a+" )
#
# dosya = open( dosya_yolu, mode="a+" )
# dosya.write( "Merhaba Python" )
# dosya.close()


# 1-10 arasındaki sayılarının karalerini kare.txt dosyasına yazın.

"""
import os

dosya_yolu = os.getcwd()+"/kare.txt"

if not os.path.exists(dosya_yolu):

	dosya =  open(dosya_yolu, mode="a+")

dosya = open(dosya_yolu, mode="a+")


for sayi in range(1,11):
	dosya.write(str(sayi)+ " saysının karesi "+ str(sayi**2) + " !\n")

dosya.close()


"""

# 1-100 arasında rastgele üretilen 10 sayıyı rast geke .txt dosyasına aşağıdaki formatta
# yazdırın


"""
	Zaman					Olay Sırası				Rastgele Sayı

	afa							sad							545
"""

#
# from os import chdir,mkdir,path
# from datetime import datetime
# from random import randint
#
#
# dosya_yolu= "/home/mehmet/PycharmProjects/TEST"
#
# if not path.exists(dosya_yolu):
# 	mkdir(dosya_yolu)
#
#
# dosya_adresi = dosya_yolu+"/rastgele_sayi.txt"
#
#
# if not path.exists(dosya_adresi):
# 	dosya = open(dosya_adresi, mode="a+")
# 	dosya.write("""
# 		Zaman									Olay Sırası					Rastgele Sayı
# 		------									-----------					-------------
# 	""")
# 	dosya.close()
#
#
# dosya = open(dosya_adresi, mode="a+")
#
# for i in range(1,101):
# 	rastgele_sayi =  randint(1,100)
# 	zaman = datetime.now()
# 	dosya.write(f"""
# 		{str(zaman)}							{str(i)}					{str(rastgele_sayi)}""")
#
# dosya.close()

from os import mkdir, chdir, path

kucuk_sayi = int(input("Küçük sayıyı girin"))
buyuk_sayi = int(input("Büyük sayıyı giriniz"))

if kucuk_sayi > buyuk_sayi:
    kucuk_sayi, buyuk_sayi = buyuk_sayi, kucuk_sayi

elif buyuk_sayi > kucuk_sayi:
    pass

else:
    print("Değerler eşit olamaz")

dosya_yolu = "/home/mehmet/PycharmProjects/TEST"
if not path.exists(dosya_yolu):
    mkdir(dosya_yolu)
dosya_adresi = dosya_yolu + "/sayilar.txt"
dosya =  open(dosya_adresi, mode="a+")

for i in range(kucuk_sayi, buyuk_sayi):
    dosya.write(f"{i}\n")

dosya.close()