class Universite():

    def __init__(self):
        self.__vize = 0
        self.__final = 0

    def get_vize(self):
        return self.__vize

    def set_vize(self, parametre: int):

        if (parametre < 0 or parametre > 100):
            while True:
                print("Hatalı vize not girişi !!! Vize notu 0-100 "
                      "Arasında girilmelidir...")
                vize_not =  input("Vize Notunuz : ")
                if (int(vize_not) < 0 or int(vize_not)>100):
                    continue
                else:
                    self.__vize =  int(vize_not)
                    break
        else:
            self.__vize =  parametre

    vize = property(get_vize, set_vize)

    @property
    def final(self):
        return self.__final

    @final.setter
    def final(self, parametre:int):

        if(parametre <0 or parametre >100):
            while True:
                print("Hatalı final notu girişi !!! Final notunuz 0-100 aralığında olmalıdır")
                final_not =  int(input("Final Notunuz"))

                if final_not <0 or final_not >100:
                    continue
                else:
                    self.__final = final_not
                    break
        else:
            self.__final = parametre


    def  ortlama(self):
        hesap =  (self.__vize*0.4) + (self.__final*0.6)
        print(f"Ortlamanız {hesap}")