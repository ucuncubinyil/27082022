"""
############ public Örnek ############

class Muhendis():

    ad =  "Mehmet Nuri" # public  field
    soyad =  "ÖZTÜRK" # public field

    def ekrana_yaz(self):
        print(self.ad)
        print(self.soyad)
"""


############ private Örnek ############

class Muhendis():

    ad =  "Mehmet Nuri" # public  field
    __soyad =  "ÖZTÜRK" # private field

    def ekrana_yaz(self):
        print(self.ad)
        print(self.__soyad)
