"""
from  os import getcwd

dosya_adresi =  getcwd()

dosya =  open(dosya_adresi+"/kare.txt", "r", encoding="utf8")


temiz_liste = list()


# for i in dosya.readlines():
#     print(i)
#     # temiz_liste.append(i.rstrip("\n").rstrip(" ").lstrip(" "))


for i in dosya.readlines():
    i.strip()
    temiz_liste.append(i.replace("\n", ""))



print(temiz_liste)

dosya.close()

"""


# sayi_listesi.txt dosyasını oluştur içinde tek ve çift sayılar olacak şekilde
# 10 sayı ekleyin

"""
from  os import getcwd


dosya_adresi = getcwd()+ "/sayi_listesi.txt"

dosya = open(dosya_adresi, mode="a+")

for i in range(10):

    sayi = input("Sayı girin")
    if sayi.isdigit():
        dosya.write(sayi+"\n")

dosya.close()

"""



""""

# Sinif dosyası var  içerisinde öğrenci ad soyad  puan sınıf bilgiler var
# Sınıfın ortalaması bulunması, en yüksek puan, en düşükpuanı bulan metodu yazın

from  os import getcwd, path

def oku():
    yeni_liste = list()

    dosya_yolu = getcwd()+"/sinif_notlari.txt"

    if path.exists(dosya_yolu):

        dosya = open(dosya_yolu, "r", encoding="utf8")
        satirlar =  dosya.readlines()
        dosya.close()

        for satir in satirlar:
            dd = satir.split(" ")
            yeni_liste.append(int(dd[2]))

    print(f"Ortalama { sum(yeni_liste)/len(yeni_liste)  }")
    print(f"En düşük puan {min(yeni_liste)}")
    print(f"En yüksek puan {max(yeni_liste)}")

oku()
"""


# Kullanıcıdan personel sayısını al , her personel için ad, soyad dogumyılı bilgilerini alarak personel.txt
#dosyasına yaz

from os import getcwd

personel_sayisi =  int(input("Personel sayısı"))

dosya = open(getcwd()+"/personel.txt", mode="w", encoding="utf8")

for personel in range(personel_sayisi):
    ad =  input("Personel ad")
    soyad = input("Personel soyad")
    dogum_yili = input("Personel dogum yili")

    dosya.write(f"AD: {ad}          SOYAD:{soyad}               DOĞUM YILI:{dogum_yili}\n")

dosya.close()




