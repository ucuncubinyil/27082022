# OPERATÖRLER

# Karşılaştırma Operatörleri

# 1.  Eşit mi ?  ==
# 2. Eşit değil mi ? !=
# 3.  > Büyüktür
# 4. < Küçüktür
# 5. >=  Büyük Eşit (Büyük veya Eşit)
# 6. <= Küçük Eşit (Küçük veya Eşit)
#

a = 5
b = 6

print(a > b)  # sadece True yada False
print(a < b)
print(a == b)  # Eşitlik kontrolü
print(a != b)  # Eşitsizlik kontrolü
print(b >= a)
print(a <= b)

# Matematiksel Operatörler
# Aritmatik Operatörler

"""
    +,-,* :toplama,çıkarma,çarpma
    /     :ondalıklı bölme (10/4=2.5)
    //    :bölümün tamsayı kısmını verir (10//4=2)
    %     : Moda alma
"""

c = 5
d = 3

print(c + d)  # toplama
print(c - d)
print(c * d)
print(c / d)
print(c // d)
print(c % d)

# Tek Çift Kontrolü
print(20 % 2)  # ciftir
print(15 % 2)  # tek

cift_mi = 22
kalan = cift_mi % 2
cevap = kalan == 0
print(cevap)

# Mantıksal Operatörler AND (VE)

# 00 = 0
# 01 = 0
# 10 = 0
# 11 = 1
kullani_adi = "mehmet"
sifre = "65"

kontrol = kullani_adi == "mehmet" and sifre == "123"
print(kontrol)

# MANTIKSAL VEYA (OR) (VEYA)# 00 = 0
# # 01 = 1
# # 10 = 1
# # 11 = 1

sayi = 36
# kontrol = sayi > 86 or sayi > 35
# print(kontrol)

kontrol = not sayi > 2 or sayi > 35 and sayi == 36  # not başıan gelen ifadeyi terse çevirir
print(kontrol)

# sayi = 21
# sayi =  not sayi
# print(sayi)

sayi = 25
sayi2 = 25

kontol = sayi is sayi2
kontol2 = sayi2 == sayi
print(kontol)
print(kontol2)
