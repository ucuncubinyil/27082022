class Musteri():

    def __init__(self):
        self.__ad = None
        self.__soyad = None
        self.__telefon = None
        self.__mail_adresi = None

    @property
    def  ad(self):
        return self.__ad

    @ad.setter
    def ad(self,value: str):
        self.__ad = value

    @property
    def  soyad(self):
        return self.__soyad

    @soyad.setter
    def soyad(self,value: str):
        self.__soyad = value

    @property
    def telefon(self):
        return self.__telefon

    @telefon.setter
    def telefon(self, value):

        while True:

            if len(value) !=  10:
                print("Lütfen telefon numaranızı 10 haneli ve başında sıfır olmadan giriniz:")
                gsm = input("Telefon Numaranız(5xx xxx xx xx)")

                if len(gsm) != 10:
                    continue
                else:
                    self.__telefon = gsm
                    break
            else:
                self.__telefon = value
                break

    @property
    def  mail_adresi(self):
        return self.__mail_adresi

    @mail_adresi.setter
    def mail_adresi(self,value:str):
        self.__mail_adresi = value


    def bilgi_yaz(self):
        bilgiler = f"""
AD              :{self.__ad}
SOYAD           :{self.__soyad}
GSM             :{self.__telefon}
MAIL            :{self.__mail_adresi}
        """
        print(bilgiler)