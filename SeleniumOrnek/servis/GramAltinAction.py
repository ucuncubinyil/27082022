from entity.GramAltin import GramAltin

from entity.base import session_factory


class GramAltinAction():

    def __init__(self):
        self.value = str()
        self.session = session_factory()

    def add_value(self):
        gram_altin = GramAltin()
        gram_altin.value = self.value
        self.session.add(gram_altin)
        self.session.commit()
        self.session.close()

    def get_records(self):
        all_records = self.session.query(GramAltin)
        self.session.close()
        return all_records.all()
