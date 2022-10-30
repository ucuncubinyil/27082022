# pip install psycopg2
# pip install SQLAlchemy

# Bağlantı Formulu  "postgresql://kullanci_adi:şifre@sunucu_adresi:port/veritabanı_adi"

from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    text
)

engine = create_engine(
    "postgresql://ojerfdbw:s2sK21OrGEeHBSEzJYp5F5qs4otnr_5D@hansken.db.elephantsql.com:5432/ojerfdbw",
    echo=True)

meta = MetaData()

ogrenciler = Table(
    "ogrenciler", meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("adi", String),
    Column("soyadi", String)

)
meta.create_all(engine)


# Tekil kayıt ekleme

def ogrenci_ekle():
    baglanti = engine.connect()
    ekle = ogrenciler.insert().values(adi="Mehmet Nuri", soyadi="Öztürk")
    cikti = baglanti.execute(ekle)
    print(cikti)
    baglanti.close()


# ogrenci_ekle()


# Çoklu kayıt ekleme
def coklu_ogrenci_ekle():
    baglanti = engine.connect()

    baglanti.execute(ogrenciler.insert(), [
        {"adi": "Ali", "soyadi": "Öztürk"},
        {"adi": "Veli", "soyadi": "Kerem"},
        {"adi": "Eda", "soyadi": "Nur"}
    ])
    baglanti.close()


# coklu_ogrenci_ekle()


# select * from ogrenciler

def get_ogrenciler():
    baglanti = engine.connect()
    sorgu = ogrenciler.select()
    cikti = baglanti.execute(sorgu)
    cikti = list(cikti)
    baglanti.close()
    print(cikti)


# get_ogrenciler()


# Query
def get_ogrenci_by_id():
    baglanti = engine.connect()
    query = text("select ogrenciler.adi, ogrenciler.soyadi from ogrenciler where id = :id")
    n = baglanti.execute(query, id=3).fetchone()
    print(n)
    baglanti.close()


# get_ogrenci_by_id()


def get_ogrenci_by_id_betwen():
    baglanti = engine.connect()
    query = text("select *  from ogrenciler where id between :x and :y")
    n = baglanti.execute(query, x=3, y=6).fetchall()
    print(n)
    baglanti.close()


# get_ogrenci_by_id_betwen()

def get_ogrenci_by_adi(adi: str):
    baglanti = engine.connect()
    query = text("select * from ogrenciler where ogrenciler.adi like :adi ")
    n = baglanti.execute(query, adi="%" + adi + "%").fetchall()
    print(n)
    baglanti.close()


# get_ogrenci_by_adi("A")


# Güncelleme
def ogrenci_guncelle():
    baglanti = engine.connect()
    guncelleme = ogrenciler.update().where(ogrenciler.c.id == 3).values(adi="Burak", soyadi="Duman")
    baglanti.execute(guncelleme)
    baglanti.close()


# ogrenci_guncelle()


def ogrenci_sil():
    baglanti = engine.connect()
    silinecek =  ogrenciler.delete().where(ogrenciler.c.id ==3)
    baglanti.execute(silinecek)
    baglanti.close()

# ogrenci_sil()

def toplu_ogrenci_sil():
    baglanti =  engine.connect()
    silinecek =  ogrenciler.delete().where(ogrenciler.c.id > 3)
    baglanti.execute(silinecek)
    baglanti.close()

toplu_ogrenci_sil()