CREATE TABLE yazarlar
(
    id           SERIAL PRIMARY KEY,
    yazar_adi    varchar(100),
    yazar_soyadi varchar(100)
);


CREATE TABLE kitaplar
(
    id         SERIAL PRIMARY KEY,
    kitap_adi  varchar,
    basim_yili int,
    yazar_id   int,

    CONSTRAINT FK_YAZARLAR
        FOREIGN KEY (yazar_id)
            REFERENCES yazarlar (id)
);

INSERT INTO yazarlar(YAZAR_ADI, YAZAR_SOYADI)
VALUES ('ORHAN', 'PAMUK'),
       ('REŞAT NURİ', 'GÜLTEKİN');

INSERT INTO kitaplar(kitap_adi, basim_yili, yazar_id)
VALUES ('VEBA GECELERİ', '2021', 1);

INSERT INTO kitaplar(KITAP_ADI, BASIM_YILI, YAZAR_ID)
values ('KARA KİTAP', 1993, 2);

INSERT INTO kitaplar(kitap_adi, basim_yili)
VALUES ('DEMİR EV', '2022');

SELECT *
FROM yazarlar
         LEFT JOIN kitaplar k on yazarlar.id = k.yazar_id;

-- reşat nuri gültekinin kitaplarını yazar ve kitap adı şekinde getir
SELECT concat(y.yazar_adi, ' ', y.yazar_soyadi) AS YAZAR_AD_SOYAD, k.kitap_adi
FROM yazarlar y
         LEFT JOIN kitaplar k on k.yazar_id = y.id
where k.yazar_id = 2;


CREATE TABLE yayin_evi
(
    id       serial primary key,
    ad       VARCHAR,
    vergi_no int
);

insert into yayin_evi(ad, vergi_no)
values ('PAPATYA YAYIN EVİ', 1234),
       ('PEGASUS YAYIN EVİ', 5678);


alter table kitaplar
    add column yayin_evi_id int;
ALTER TABLE kitaplar
    add constraint fk_yayi_evi foreign key (yayin_evi_id)
        references yayin_evi (id);

-- yanlış kullanım
-- select ad
-- from yayin_evi
--          left join kitaplar k on yayin_evi.id = k.yayin_evi_id;

select y.ad
from kitaplar
         left join yayin_evi y on y.id = kitaplar.yayin_evi_id;

select concat(y.yazar_adi, ' ', y.yazar_soyadi) as yazar,
       kitaplar.kitap_adi as KITAP_ADI,
       yayin_evi.ad as YAYIN_EVI
from kitaplar
         inner join yayin_evi on kitaplar.yayin_evi_id = yayin_evi.id
         inner join yazarlar y on kitaplar.yazar_id = y.id
        where y.yazar_adi LIKE  '%A%' or y.yazar_adi LIKE  '%a%';


SELECT concat(y.yazar_adi, ' ', y.yazar_soyadi) AS YAZAR_AD_SOYAD, k.kitap_adi
FROM yazarlar y
         LEFT JOIN kitaplar k on k.yazar_id = y.id;

-- update kitaplar
-- set yayin_evi_id = 1
-- where id = 2;


CREATE  TABLE sepet_a(
    id serial primary key ,
    meyve_a  varchar(100) not null
);

CREATE  TABLE sepet_b(
    id serial primary key ,
    meyve_b  varchar(100) not null
);


insert into sepet_a(meyve_a)
values ('Elma'), ('Portakal'), ('Muz'), ('Salatalık');


insert into sepet_b(meyve_b)
values ('Portakal'), ('Elma'), ('Kiwi'), ('Kayısı');


select a.id, b.id,meyve_a, meyve_b from sepet_a a
inner join sepet_b  b on a.id = b.id;

select  * from  sepet_a a
left join  sepet_b b  on b.id =  a.id;

select * from  sepet_a a
left join sepet_b b on b.id =  a.id where  b is not null;

select  * from  sepet_a a
right join   sepet_b b  on b.id =  a.id;

select  * from  sepet_a a
right join   sepet_b b  on b.id =  a.id where  b is not null;

select  * from  sepet_a a
full outer join   sepet_b b  on b.id =  a.id  where  b is not null;

