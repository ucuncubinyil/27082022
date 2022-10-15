class Uye():
    isim = str()#public field
    soy_isim = str() #public field
    __tc = "" # private field

    def kaydet(self):
        self.isim = input("İsim: ")
        self.soy_isim = input("Soyisim")
        TC = input("T.C.")

        if (len(TC) == 11 and TC.isnumeric()):
            self.__tc = TC
        else:
            self.__tc = "00000000000"

    def yaz(self):
        print(f"İsim {self.isim}, Soyisim: "
              f"{self.soy_isim}, TC: {self.__tc}")
