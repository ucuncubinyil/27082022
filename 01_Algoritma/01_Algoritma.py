# Algoritma

# Psucode
# İki sayıyı toplayan algoritmayı yazınız

# 1. Başla
# 2. Birinci sayıyı al
# 3. İkinci sayıyı al
# 4. BirinciSayi + İkinci Sayı
# 5. Sonucu Yazıdır
# 6. Bitir

# birinci_sayi =  input("Birinci sayıyı yazın")
# ikinci_sayi =  input("İkinci sayıyı yazın")
# toplam = int(birinci_sayi) + int(ikinci_sayi)
# print(toplam)


# DEĞİŞKEN KAVRAMI ( VARIABLE)

# degiskenin_adi =  değişkenin değeri

# kaleci  =  "Mehmet Nuri"
#
# # Yazım Standartları
# # camelCase
# # PascalCase
# # FULLCASE
# # kebab-case
# # snake_case
#
# # TAM SAYI (INT)
#
# #  - sonsuz  + sonsuza kadar gider
# sayi1 =  15
# sayi2 = 999999999999999
# print( sayi1 )
# print( type(sayi1)  )
# print( sayi2 )
#
# # Noktalı Sayılar (Float)
# sayi3 =  25.3
# print(sayi3)
# print( type(sayi3) )
#
# # Metinsel Veri Tipi (STRING)
# ad = "Mehmet Nuri"
# soyad =  'ÖZTÜRK'
# print(ad)
# print(soyad)
# print( type(ad)  )
#
# # Mantıksal Veri Tipi (Boolean ) True False
# arabasi_var_mi =  True
# ucagi_var_mi =  False
#
# int ve float örneği
# bir öğrencinin iki notunun ortalamasını ekrana yazdıran program.

# not1 = 75
# not2 = 95
# sonuc = (not1+not2)/2 # Float çıkar
#
# print(sonuc)
# print(int(sonuc))
#
# sayi =  "120"
# sayi2 =  "3910"
#
# toplam =  sayi + sayi2 # birleştirir
#
# print(toplam)
#
# c1 = c2 = c3 = 15  # 1. yöntem
# d1, d2, d3 = 12, 15, 18  # 2.yöntem
# a1, a2 = a3 = 55, 44 # 3. yöntem
#
# print(c1)
# print(c2)
# print(c3)
#
# print(d1)
# print(d2)
# print(d3)
#
# print(a1)
# print(a2)
# print(a3)
#
#
# print("C1 in değeri: ", c1) # 1. yöntem
# print("C1 in değeri: {}".format(c1)) # 2. yöntem
# print(f"C1 in değeri:{c1}") # 3. yöntem
#
# adi, soyadi, yasi = "Mehmet Nuri", "Öztürk", 28
# print(f"Adı :{adi}, Soyadı:{soyadi}, Yaşı:{yasi}")
# print("Adı Soyadi Yasi", adi, soyadi, yasi)
#
# x1 = 5
# x2 = 7
#
# print("Önceki Durum")
# print(x1,x2) # 5-7 # adresler farklı
#
# print("Sonraki Durum")
# x2 = x1
# print(x1,x2) # 5-5 #x2 nin adresine x1 in adresi kopyalandı
#
# x2 = 99
# print(x1,x2) # 5 - 99 #x2 ye yeni adres verildi


##### KAÇIŞ KARAKTERLERİ #####
# \n new line
# \t TAB

yazi = "Merhaba\nPython\n\n\nDünyası"
print(yazi)

yazi =  "Merhaba\t\t\tPython\t\t\tDünyası           Güneşli"
print(yazi)

print("Bu", "gün", "hava", "güneşli", sep=" ") # sep birden fazla string in arasına değer atar
print("Bu", "gün", "hava", "güneşli", end="!") # end birden fazla string in son değerine verilen ifadeyi ekler


ad = "Mehmet Nuri"
soyad =  'ÖZTÜRK'
yas =  29

bilgilerim =  f"""
            Merhaba, ben {ad}, {soyad}
yaşım   {yas}
"""
print(bilgilerim)

# Kullanıcıdan veri alma

kullanici_adi =  input("Kullanıcı Adınızı Giriniz : ")
print(kullanici_adi)


