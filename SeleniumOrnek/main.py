import time

from Doviz import Doviz
from threading import Thread

from servis.DolarAction import DolarAction
from servis.EuroAction import  EuroAction
from servis.GramAltinAction import GramAltinAction





def getir(tip):
    if tip == "dolar":
        dolar = Doviz("dolar")
        dolar.getir()
        dolarAction = DolarAction()
        dolarAction.value = dolar.icerik
        dolarAction.add_value()

        print(dolar.icerik)
        del dolar

    elif tip =="euro":
        euro = Doviz("euro")
        euro.getir()
        euroAction =  EuroAction()
        euroAction.value = euro.icerik
        euroAction.add_value()

        print(euro.icerik)

        del  euro

    elif tip == "gram-altin":
        altin = Doviz("gram-altin")
        altin.getir()
        gramAltinAction = GramAltinAction()
        gramAltinAction.value = altin.icerik
        gramAltinAction.add_value()

        print(altin.icerik)

        del altin


def tekrarla():

    getir("dolar")
    getir("euro")
    getir("gram-altin")


while True:
    tekrarla()


