from entity.Euro import Euro

from entity.base import session_factory


class EuroAction():

    def __init__(self):
        self.value = str()
        self.sesion = session_factory()


    def add_value(self):
        euro = Euro()
        euro.value = self.value
        self.sesion.add(euro)
        self.sesion.commit()
        self.sesion.close()

    def get_records(self):
        all_records = self.sesion.query(Euro)
        self.sesion.close()
        return all_records.all()
