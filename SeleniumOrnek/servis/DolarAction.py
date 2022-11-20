from entity.Dolar import Dolar

from entity.base import session_factory


class DolarAction():

    def __init__(self):
        self.value = str()
        self.sesion = session_factory()


    def add_value(self):
        dolar = Dolar()
        dolar.value = self.value
        self.sesion.add(dolar)
        self.sesion.commit()
        self.sesion.close()

    def get_records(self):
        records = self.sesion.query(Dolar)
        self.sesion.close()
        return records.all()
