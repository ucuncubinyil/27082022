############## KALITIM-INHERITANCE ###############

'''
Inheritance veya kalıtım bir sınıfın başka bir sınıfan özelliklerini(attribute)
 ve metodlarını miras almasıdır.
Bu yapı aslında bizim kend anne babamızdan değişik özelliklerive davranışları miras almamıza benzetilebilir.

Örneğin, bir şirketin çalışanlarını tasarlamak için sınıflar oluşturuyoruz.
 Bunun için Yönetici, Proje Direktörü, İşçi gibi sınıflar oluşturmamız gerekiyor.
Aslında baktığımız zaman bu sınıfların hepsinin belli ortak metodları ve özellikleri bulunuyor.
O zaman bu ortak özellikleri ve metotları tekrar tekrar bu sınfıların içinde
tanımlamak yerine, bir tane ana-temel(base) class tanımlayıp ortak özellik ve metotları bu class'ta yazıp
 diğer classların bu base classı miras almasını sağlayabiliriz. Inheritance'ın temel amacı budur.
'''
"""
from Yonetici import Yonetici

yonet =  Yonetici("Murat", "12000","Bilgi İşlem",25)
yonet.bilgi_goster()

yonet.departman_degis("IK")
yonet.bilgi_goster()
"""
### OVERRIDING (iptal Etme-Revize)
"""
Eğer biz miras aldığımız methodları aynı isimle kendi sınıfımızda tekrar tanımlarsak,
 artık metodu çağırdığımızda base class'dan değil kendi türettiğimiz class'tan çalıştırmış oluyoruz.
Bu işleme OOP override etme denir.

Örneğin artık çalışan sınıfının init metodunu kullanmak yerine Yönetici sınıfında init metodunu override edebiliriz.
Böylece Yönetici sınıfına ekstra bir attribute ekleyebiliriz.
"""


##SUPER Anahtar Kelimesi
"""
super anahtar kelimesi: türemiş sınıfta base sınıftan de miras alınan bir
methodu tekrar tanımladığımızda override işlemi gerçekleşiyordu.
Super keyword ü ile bu methodu override edip yok etmek yerine basedeki gerçekleşen
 işlemi alıp sadece türemiş sınıfta atanan özelliği eklemizi sağlar.
  Böyle Base classdaki method komple yok sayılmak yerine yeni özellikle revize edilmiş olur.
"""


from Kamyon import Kamyon

bmc = Kamyon()
bmc.renk = "Beyaz"
bmc.fiyat = 16322546.00
bmc.marka = "BMC"
bmc.model = "XCVW"
bmc.uretim_yili = 2022
bmc.tasima_kapasitesi = 60000
bmc.yakit_depo_sayisi = 2

bmc.bilgi_yaz()