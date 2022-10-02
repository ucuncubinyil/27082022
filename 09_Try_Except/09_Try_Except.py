# TRY EXCEPT  HATA YAKALAMA


"""
try:
    hata çıkabilecek kod bloğu
except:
    Hata olursa yapılacak işlemler
"""

"""
try:
    sayi = int(input("Sayı gir"))
except ValueError:
    print("Sadece rakam girilmelidir")

finally:
    print("Hata olsa da olmasada çalışır")
"""

"""


from os import getcwd
while True:

    try:
        dosya = open(getcwd()+"/tr_except.txt", "a+")
        sayi = int(input("Lütfen bir sayı girin"))

        dosya.write(str(sayi)+"\n")
        dosya.close()
        break
    except ValueError:
        print("Sadece sayısal rakam girilmelidir")
        continue
    except FileNotFoundError:
        print("Dosya bulunamadı")
    except TypeError:
        print("Dosyaya sadece string basılmalıdır")
        continue
    except ZeroDivisionError:
        print("Hiç bir sayı sıfıra bölünemez")
    except OverflowError:
        print("Değişkenin kapasitesi aşıldı")
    except ImportError:
        print("Import hatası mevcut")
    except IndexError:
        print("Liste boyutu aşıldı")

    except:
        print("Bir hata oluştu")
    finally:
        dosya.close()


"""


"""

# HATA FIRLATMA  raise()


try:
    not1 = int(input("Notunuzu girin"))

    if not1 <0 or not1 >100:
        raise Exception #Manuel olarak hata patlıyoruz
except ValueError:
    print("Sadece rakam girilmelidir")
except Exception:
    print("Notlar  0-100 aralığında olmalıdır")
    
"""


#ASSERT idaa edilen

"""
try:
    kontrol_eposta = "info@mehmetnuri.net"
    eposta = input("Lütfen email adresinizi girin")
    assert  eposta == kontrol_eposta
except AssertionError:
    print("E-posta adresleri uyuşmuyor")

"""


# Kullanıcıdan 2 sayı 1 işlem al  işlemler daha önce tanımlanmış metodlar olsun
# işlemler +-*/ den biri değil ise assert fırlatsın
# ValueErorr olduğunda tekrar veri istesin
# ZeroDivision için tekrar veri istenmesin

def topla(s1,s2):
    return  s1+s2

def cikar (s1,s2):
    return  s1-s2

def bol(s1,s2):
    return  s1/s2

def carp(s1,s2):
    return  s1*s2


def islem_yap():
    s1 = int(input("1. Sayı"))
    s2 = int(input("2. Sayı"))

    islem =  input("Toplama(+), Çıkarma(-), Çarpma(*), Bölme(/)")

    assert  islem == "+" or islem == "-" or islem == "*" or islem == "/"

    if islem == "+":
        print(topla(s1,s2))
    elif islem == "-":
        print(cikar(s1,s2))

    elif islem == "*":
        print(carp(s1,s2))

    elif islem == "/":
        print(bol(s1,s2))


while True:

    try:
        islem_yap()
        break
    except ValueError:
        print("Sadece rakam girilmelidir")
        continue
    except ZeroDivisionError:
        print("Hiç bir sayı sıfıra  bölünemez")
        break
    except AssertionError:
        print("İşlem bulunamadı")
        continue
    except Exception:
        print("Bir hata oluştu")















