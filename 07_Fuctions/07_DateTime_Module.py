# Date Time Kütüphanesi

import datetime
from datetime import datetime, date, timedelta
import locale

# Pythonun varsayılan dilini Türkçeye ayarlıyoruz
locale.setlocale(locale.LC_ALL, "tr_TR.utf8")

zaman = datetime.now()
# print(zaman)  # şuanki zamanı verir
# print(zaman.day)  # şuanki günü verir
# print(zaman.month)  # şuanki ayı verir
# print(zaman.year)  # şuanki yılı verir
#
# print(zaman.hour) #Şuanki saati verir
# print(zaman.minute) #Şuanki dakikayı verir
# print(zaman.second) #Şuanki saniyeyi verir
#
#
# #Dışardan bir veriyi date time kullanarak dönüştürme işlemi
# zaman2 = datetime(1993,11,20)
# print(zaman2.date())
# print(zaman2.year)
#


#### ZAMAN FORMATLAMA #####

"""
%d      :   RAKAM İLE GÜNÜ
%m      :   RAKAM İLE AYI
%Y      :   RAKAM İLE 4 HANELİ YILI VERİR
%y      :   RAKAM İLE 2 HANELİ YILI VERİR
%b      :   YAZI ILE 3 HANELİ AYI VERİR
%H      :   RAKAM İLE SAATİ VERİR
%M      :   RAKAM İLE DAKİKAYI VERİR
%S      :   RAKAM İLE SANİYEYİ VERİR
%a      :   YAZI İLE 3 HANELİ GÜNÜ VERİR
%A      :   YAZI İLE TAM GÜN ADINI VERİR
%D      :   AY/GÜN/YIL OLARAK ZAMANI VERİR

"""

print(zaman.strftime("Bu gün günlerden : %A"))
print(zaman.strftime("Bu gün günlerden : %D"))
print(zaman.strftime("Bu gün günlerden : %a"))

# YIL-AY-GUN--SAAT:DAKİKA:SANİYE--GÜNADI
formatlanmis_zaman = zaman.strftime("%Y-%m-%d--%H:%M:%S--%A")
print(formatlanmis_zaman)


zlist = formatlanmis_zaman.split("--")

print(zlist)

# for z in zlist:
#     print(z)

print(zlist[0])
print(zlist[1])
print(zlist[2])

zamanList = zlist[1].split(":")

print(zamanList[0])
print(zamanList[1])
print(zamanList[2])



bu_gun =  date.today()
print(bu_gun)

bir_hafa_once =  bu_gun - timedelta(7)
print(bir_hafa_once)











