#### ABSTRACTION (Abstract,Interface) #####
'''
Abstract class(soyut sınıf): Abstract sınıfların kullanım amacı tanımlanan
bir class'ın sadece base class özelliği taşıması sağlamaktır.
Python dilinde diğer dillerden farklı olarak abstract yapısı hazır
olarak tanımlıdır ve import edilmesi gereklidir.
Abstract class'lar da tanımlanan field(özellik,attribute)'lara değer
atanmaz ve metotların gövdeleri doldurulmaz.
Yani amac sadece tanımlama(miras alındığında türeyen sınıfa aktarılması
istenen özellikler).

Abstract methodlar sadece Abstract(ABC) class'larda bulunurlar ama class
Abstract diye bütün methodlar @abstractmethod olmak zorunda değil.
'''

"""
from Product import Product

computer = Product()
computer.id = "1"
computer.ad = "Mac"
computer.price = 57000.00
computer.stock = 2

computer.kaydet()"""

from Bird import Bird

b = Bird()
b.drik()
b.walk()
b.sleep()