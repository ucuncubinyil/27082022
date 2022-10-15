# ACCESS MODIFIERS : public, private , protected

#public:  Yazılım dillerinde genel erişime
# açık anlamına gelir. Herhangi bir erişim
# belirleyicisi verilmez ise default olarak
# public verilir.

from  Muhendis import Muhendis

"""
############ public Örnek ############
ahmet =  Muhendis()
ahmet.ad = "Ahmet"
ahmet.soyad =  "Kerim"
ahmet.ekrana_yaz()
"""

#private: Yazılım dillerinde saddece
# tanımlandığı sınıf içerisinden erişilebilir
# anlamına gelir. '__' iki altçizgi öne koyularak
# tanımlanır

"""
############ private Örnek ############
ahmet =  Muhendis()
ahmet.ad = "Ahmet"
ahmet.ekrana_yaz()
"""

"""
from Uye import Uye

uye1 =  Uye()
uye1.kaydet()
uye1.yaz()

"""

# protected:  Sınıf içinde public ama sınıf dışında sadece miras alınan
# (inheritance) sınfılardan erişilebilir. '_' tek alt çizgi ile tanımlanır.

from Calisan import Calisan

ahmet =  Calisan()
ahmet.ad = "Kerim"
ahmet.soyad ="Durmaz"
ahmet._ekranayaz()