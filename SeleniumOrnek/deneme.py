from datetime import datetime


from servis.DolarAction import DolarAction


hepsi =  DolarAction()
records = hepsi.get_records()

del hepsi

for i in records:
    print(i.value)

