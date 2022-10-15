#### KAPSULLEME

# getter  metotları private  özelliklerin değirini
# okumamızı sağlar readyonly(sadece  okunabilir)

#setter  metotları private özelliklerin değerini
# değişmemizi sağlar

class Kapsul():

    def __init__(self):
        self.__gizli_ozellik1 =  "Gizli Özellik 1 Değeri"
        self.__gizli_ozellik2 =  "Gizli Özellik 2 Değeri"

    def get_gizli_ozelik1(self):
        return  self.__gizli_ozellik1

    def set_gizli_ozelik_1(self, value):
        self.__gizli_ozellik1 = value


    def  get_gizli_ozellik_2(self):
        return self.__gizli_ozellik2

    def set_gizli_ozellik_2(self, value):
        self.__gizli_ozellik2 = value


    def  ekrana_yaz(self):
        print(self.__gizli_ozellik1, self.__gizli_ozellik2)