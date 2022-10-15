## Bir banka müşteri kayıot sistemi oluşturulurken kayıt
# esnasında ad, soyad tc(11 hane) ve ıban(TR+12) bilgileri
# alınıyor. Gerekli kontrolleri sağlayarak kayıt platformunu
# oluşturun

class Banka():

    def __init__(self):
        self.__tc = None
        self.__iban = None
        self.isim = input("İsminiz: ")
        self.soyisim = input("Soyisminiz: ")
        self.__set_iban()
        self.__set_tc()

    def get_iban(self):
        return self.__iban

    def __set_iban(self):
         # TR231354654654
        while True:
            IBAN = input("IBAN Adresiniz: ") #tr54656
            ulke_kodu =  IBAN[0].upper()+IBAN[1].upper()

            if ulke_kodu == "TR":
                iban =  IBAN[2:]

                if len(iban) == 12 and  iban.isnumeric():
                    self.__iban =  ulke_kodu+iban
                    break
                else:
                    print("Lütfen IBAN bilginizi 12 haneli olacak şekilde girin")
                    continue
            else:
                print("Lütfen IBAN bilginizin başına TR ülke kodunu girin ")
                continue

    def get_tc(self):
        return self.__tc


    def __set_tc(self):
        while True:
            TC = input("T.C. Kimlik Numaranız")
            if len(TC) == 11 and TC.isnumeric():
                self.__tc = TC
                break
            else:
                print("Lütfen T.C. Kimlik Numaranızı Doğru Giriniz !")
                continue

    def  yaz(self):
        bilgiler = f"""
AD          :{self.isim}
SOYAD       :{self.soyisim}
T.C.        : {self.__tc}
IBAN        : {self.__iban}
        """
        print(bilgiler)