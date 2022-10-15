class Personel():

    def __init__(self, parametre):
        self.__isim = parametre

    def get_isim(self):
        return self.__isim

    def set_isim(self, parmetre):
        self.__isim = parmetre

    ad = property(get_isim, set_isim)