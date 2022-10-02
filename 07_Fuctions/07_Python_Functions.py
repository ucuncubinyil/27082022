#Hazır Fonksiyonlar

"""
capitalize()    İlk harfi büyüğe çevirir
count()         Bir dizide belirtilen değerin kaç defa tekrarlandığının sayısını döner
endswith()      Bir dizide belirtilen değer ile bittiğini kontrol eder Boolean
find()          Dizide belirtilen değeri bulur ve index numarasını da verir
isalpha()       Metnin tamamen karakterlerden oluşup oluşmadığını kontrol eder
isdecimal()     Metnin noktalı sayı olup olmadığını kontrol eder

isdigit()       Metinin sayısal olup olmadığını kontrol eder

lstrip()        Yazının soldaki boşluğunu siler
rstrip()        Yazının sağdaki boşluğunu siler
strip()        Yazının hem sağdan hem soldan boşluğunu siler
split()         Metni belirtilen ayraca göre böler  ve diziye çevirir





"""
# a_listesi = [ "ahmet", "mehmet", "kemal"]
# print(a_listesi.count("ahmet"))
#
# metin  =  "denemepdf"
# print(metin.capitalize())

# deneme.pdf
# print(metin.find("deneme"))
# print(metin.isalpha())
#
# a = "\u0030" #unicode for 0
#
# print(a.isdecimal())
#
#
# b =  "5465465"
# print(b.isdigit())
#
# metin =  " ahmet turan "
# print(metin.lstrip())
# print(metin.rstrip())
# print(metin.strip())


dosya_adi =  "deneme,jkad,hajsd.pdf"

parcalanamis =  dosya_adi.split(".")
print(parcalanamis)

kelimeler = "Bugün.hava.çok.sıcak.değildi"

print(kelimeler.split(".", 4)) # listeye en fazla  baştan 5 eleman seç


universite = "Yıldız Teknik Üniversitesi"
print(universite.split(" "))