from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    ForeignKey
)

from sqlalchemy.sql import text, select


engine = create_engine(
    "postgresql://ojerfdbw:s2sK21OrGEeHBSEzJYp5F5qs4otnr_5D@hansken.db.elephantsql.com:5432/ojerfdbw",
    echo=True)

meta = MetaData()

calisanlar = Table(
    "calisanlar", meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("ad", String),
    Column("soyad", String)
)

adresler = Table(
    "adresler", meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("c_id", Integer, ForeignKey("calisanlar.id")),
    Column("il_adi", String),
    Column("ilce_adi", String),
    Column("acik_adres", String)
)

meta.create_all(engine)


def calisan_ekle():
    baglanti = engine.connect()

    baglanti.execute(calisanlar.insert(), [
        {"ad": "Kemal", "soyad": "Unakıtan"},
        {"ad": "Ali", "soyad": "Sunal"},
        {"ad": "İbrahim", "soyad": "Kalın"}
    ])
    baglanti.close()


# calisan_ekle()


def adres_ekle():
    baglanti = engine.connect()

    adres = adresler.insert().values(
        c_id=1,
        il_adi="Ankara",
        ilce_adi="Sincan",
        acik_adres="Barbaros Mah."
    )
    baglanti.execute(adres)
    baglanti.close()


# adres_ekle()

def calisan_adres_bilgileri():
    baglanti =  engine.connect()
    calisan =  select([calisanlar, adresler] )\
        .where(calisanlar.c.id==adresler.c.c_id)
    cikti = baglanti.execute(calisan).fetchall()

    for adres in cikti:
        print(adres)

    baglanti.close()

calisan_adres_bilgileri()
