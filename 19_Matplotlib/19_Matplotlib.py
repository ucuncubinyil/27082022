# pip install  matplotlib
from matplotlib import pyplot as plt

"""
plt.plot( [1,2,3],[4,5,6] )
plt.ylabel("Sayılar")
plt.xlabel("Değerler")
plt.show()

"""
"""
x = [4, 16, 81]
y = [2, 8, 9]
plt.plot(x, y)
plt.title("Python Grafik Çizdirme")
plt.ylabel("Y EKSENİ")
plt.xlabel("X EKSENİ")
plt.show()
"""

from matplotlib import style

style.use("ggplot")
"""
x1 = [5, 8, 10]
y1 = [12, 16, 6]

x2 = [6, 9, 11]
y2 = [6, 15, 7]

plt.plot(x1, y1, 'yellow', label="birinci_cizgi", linewidth=5)
plt.plot(x2, y2, 'r', label="ikinci_cizgi", linewidth=3)

plt.title("Epic Info")
plt.xlabel("X Ekseni")
plt.ylabel("Y Ekseni")

plt.grid(True, color='b')
plt.legend()
plt.show()
"""
"""
x = [0.25, 1.25, 2.25, 3.25, 4.25]
y = [50, 40, 70, 80, 20]
plt.bar(x, y, label="BMW", width=.5, color='blue')

x2 = [.75, 1.75, 2.75, 3.75, 4.75]
y2 = [80, 20, 20, 50, 60]
plt.bar(x2,y2, label="AUDI", width=.5, color='r')

plt.legend()
plt.xlabel("Günler")
plt.ylabel("Mesafa(km-h)")
plt.title("Araç Hız Grafiği")
plt.savefig("test.pdf")
plt.show()
"""
"""
x = [1, 1.5, 2, 2.5, 3, 3.5, 3.6]
y = [7.5, 8, 8.5, 9, 9.5, 10, 10.5]

x2 = [8, 8.5, 9, 9.5, 10, 10.5, 11]
y2 = [3, 3.5, 3.7, 4, 4.5, 5, 5.2]

plt.scatter(x,y, label="Yüksek Gelir-Düşük Tasarruf", color="red")
plt.scatter(x2,y2, label="Düşük Gelir-Yüksek Tasarruf", color="blue")
plt.xlabel("Tasarruf*100")
plt.ylabel("Gelir *1000")
plt.title("Nokta Grafiği")
plt.show()
"""

"""
gunler = [1, 2, 3, 4, 5]
uyku = [7, 8, 6, 11, 7]
yemek = [2, 3, 4, 3, 2]
calisma = [7, 8, 7, 2, 2]
eglence = [8, 5, 7, 8, 13]

plt.plot( [],[], color='m', label="Uyku", linewidth=5 )
plt.plot( [],[], color='c', label="Yemek", linewidth=5 )
plt.plot( [],[], color='r', label="Çalışma", linewidth=5 )
plt.plot( [],[], color='k', label="Eğlence", linewidth=5 )

plt.stackplot(gunler,uyku,yemek,calisma,eglence,  colors=['m','c','r','k'])
plt.xlabel("Günler")
plt.ylabel("Saat")
plt.title("Yığın Grafiği")
plt.legend()
plt.show()

"""
"""
gunler = [ 1, 2, 3, 4, 5 ]
uyku = [ 7, 8, 6, 11, 7 ]
yemek = [ 2, 3, 4, 3, 2 ]
calisma = [ 7, 8, 7, 2, 2 ]
eglenme = [ 8, 5, 7, 8, 13 ]
dilimler = [ 7, 2, 2, 13 ]
aktiviteler = [ 'uyku', 'yemek', 'calisma', 'oynama' ]
renkler = [ 'c', 'm', 'r', 'b' ]
plt.pie( dilimler,
         labels=aktiviteler,
         colors=renkler,
         startangle=90,
         shadow=True,
         explode=(0, 0.1, 0, 0),
         autopct='%1.1f%%'
         )
plt.savefig("oranlar.pdf")
plt.show( )

"""
"""
# pip install numpy
import numpy as np
from matplotlib import pyplot as plt


def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)


t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.subplot(221)
plt.plot(t1, f(t1), "bo", t2, f(t2))

plt.subplot(222)
plt.plot(t2, np.cos(2*np.pi *t2))

plt.show()

import  numpy as np

# 0-5 arasında eşit olarak 0.2 aralıklarla sayı dizisi üret
t = np.arange(0, 5, 0.2)

plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.xlabel("x")
plt.ylabel("y")
plt.show()
"""
"""
import  numpy as np
t  = np.arange(0,2, 0.1)

plt.plot(t, t, 'r--')
plt.plot(t, t**2, 'b--')
plt.plot(t, t**3, 'g--')
plt.xlabel("x")
plt.ylabel("y")
plt.show()


import numpy as np

# Bir Histogram cizmek uzere verimizi olusturalim
# Ortalama (mu) ve standart sapma (sigma)
# degerlerimizi verelim
mu, sigma = 100, 15
# np.random fonksiyonu randn ile 10000 tane
# rastgele sayidan olusan bir dizi yaratalim
iq = mu + sigma * np.random.randn(10000)

# verimizden bir histogram olusturalim
n, bins, patches = plt.hist(iq, 50, density=1,
                            facecolor='g', alpha=0.75)


plt.grid(True)
plt.text(60,.025, r'$\mu=100,\ \sigma=15$')
plt.show()
"""

import numpy as np

t = np.arange(0, 5, 0.01)
cost = np.cos((2 * np.pi * t)) # s = cos(2 * PI * t) ifadesiyle fonksiyonumuzu olusturalim
# grafigimizi cizdirelim
plt.plot(t, cost, lw=2)
# noktamizi etiketleyelim
plt.annotate('Dönüm Noktası',
             xy=(2, 1),
             xytext=(3, 1.5),
             arrowprops=dict(facecolor='green', shrink=0.05), )
plt.ylim(-2.2)# y ekseninin limitlerini belirleyelim
plt.show()
