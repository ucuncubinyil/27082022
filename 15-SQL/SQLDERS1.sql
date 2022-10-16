-- DML -> İÇ MİMAR
---> VERİ İLE İLGİLİ İŞLEMLERİ KOMUTLARI BARINDIRIR
--> INSERT DELETE UPDATE MERGE CALL EXPLAIN PLAIN LOCK TABLE

-- DDL -> İNŞAAT MÜH -> TABLONUN YAPISINI BELİRLEYEN KOMUTLARI İÇERİR
---> CREATE  ALTER DROP RENAME TRUNCATE COMMENT

--- TABLO OLUŞTURMA

CREATE TABLE accounts
(
    id         SERIAL PRIMARY KEY,
    user_name  VARCHAR(50) UNIQUE NOT NULL,
    password   VARCHAR(50)        NOT NULL,
    email      VARCHAR(50) UNIQUE,
    created_on TIMESTAMP
);


-- TABLO VERİ EKLEME
INSERT INTO accounts(user_name, password, email, created_on)
VALUES ('mehmet_nuri', 'İstanbul34', 'info@mehmetnuri.net', current_timestamp);

INSERT INTO accounts(user_name, password, email, created_on)
VALUES ('ahmet', 'İstanbul34', 'ahmet@mehmetnuri.net', current_timestamp);

INSERT INTO accounts(user_name, password, email, created_on)
VALUES ('veli', 'veli34', 'veli@34.com', current_timestamp);

INSERT INTO accounts(user_name, password, email, created_on)
VALUES ('hasan', 'hasan44', 'hasan@malatya.com', current_timestamp);

-- çoklu kayıt ekleme
INSERT INTO accounts(user_name, password, email, created_on)
VALUES
    ('kemal', 'hasan44', 'kemal@malatya.com', current_timestamp),
    ('mahmut', 'hasan44', 'mahmt@malatya.com', current_timestamp),
    ('kerim', 'hasan44', 'kerim@malatya.com', current_timestamp);


-- TABLO SEÇME
SELECT * FROM accounts; -- TÜM TABLOYU SEÇME
SELECT user_name, email FROM  accounts; -- BELİRLİ KOLONU SEÇME
SELECT user_name AS KULLANICI, email AS MAIL FROM  accounts; -- BELİRLİ KOLONU SEÇME
SELECT  user_name || '-' || email as BILGILER from accounts; -- TABLODAKİ İKİ COLONU BİRLEŞTİRME
SELECT 5*3; -- MATEMATİKSEL İŞLEM ÖRNEĞİ

-- VERİ SORGULAMA
select  * from  accounts WHERE id = 4;
select * from  accounts WHERE  user_name =  'hasan'; --tam eşleştirme
select * from  accounts WHERE  user_name LIKE  'ha%'; -- user_name kolonunda ha ile başlayan kayıtlar
select * from  accounts WHERE  user_name LIKE  '%ri'; -- user_name kolonunda ri ile biten kayıtlar
select * from  accounts WHERE  user_name LIKE  '%i%'; -- user_name kolonunda i içeren  kayıtlar

-- BİRDEN FAZLA KOŞUL
SELECT  * FROM  accounts where  id = 4  AND user_name = 'hasan' AND  email = 'hasan@malatya.com';
SELECT  * FROM  accounts where id =4 or id = 6;
SELECT * FROM  accounts WHERE id =4 OR id = 7 OR user_name LIKE  '%i%';

--ARİTMETİKSEL SORGULAMA
SELECT * FROM  accounts WHERE id = 2; -- ID 2 YE EŞİT OLAN
SELECT * FROM  accounts WHERE id > 2; -- ID 2 DEN BUYUK OLANLAR
SELECT * FROM  accounts WHERE id >= 2;-- ID 2 VE 2 DEN BUYUK OLANLAR
SELECT * FROM  accounts WHERE id < 7; -- ID 7 DEN KUCUK OLANLAR
SELECT * FROM  accounts WHERE id <= 7;-- ID 7 VE 7 DEN KUCUK OLANLAR
SELECT * FROM  accounts WHERE id != 2; -- ID 2 YE EŞİT OLMAYANLAR
SELECT * FROM  accounts WHERE id <> 2;-- ID 2 YE EŞİT OLMAYANLAR
SELECT * FROM  accounts; --KESİNLİKLE YAPILMAMALI BÜYÜK PROJELERDE
SELECT *FROM  accounts WHERE user_name IS NOT NULL; -- KULLANICI ADI BOŞ OLMAYAN BÜTÜN KAYITLARI GETİR.

--SIRALAMA İŞLEMİ
SELECT * FROM accounts ORDER BY id  ; -- ID DEĞERİ KÜÇÜKTEN BÜYÜĞE GÖRE SIRALAR
SELECT * FROM accounts ORDER BY id DESC; -- ID DEĞERİ KÜÇÜKTEN BÜYÜĞE GÖRE SIRALAR
SELECT * FROM accounts ORDER BY user_name  ; -- USERNAME DEĞERİ A-Z GÖRE SIRALAR
SELECT * FROM accounts ORDER BY user_name  DESC ; -- USERNAME DEĞERİ Z-A GÖRE SIRALAR


-- IN SORGULAMA
SELECT * FROM accounts where id IN(1,6,8) order by  user_name; -- select * from accounts where id =  1 or id =6 or id =  8;
SELECT * FROM accounts where user_name IN('mehmet_nuri', 'hasan');
SELECT * FROM accounts where id NOT IN(1,6,8) order by  id; -- içermeyen kayıtlar


--BASİT ZAMAN İŞLEMLERİ
SELECT * FROM accounts where CAST( created_on AS DATE)  > '2021-10-16'; --56464641651465165165


--- iç içe sorgu
select  * from  accounts where id in (
    select id from  accounts where  user_name like '%i%'
    );


select  * from  accounts where id in (
    select id from  accounts where id in ( select id from accounts where id in(1,3) )
    );


-- var olan bir tabloyu güncelleme
ALTER TABLE  accounts ADD COLUMN  birth_year INT; -- KOLON EKLEME

-- KAYIT GÜNCELLEME
UPDATE  accounts SET birth_year = 1993 WHERE id =8;
UPDATE  accounts SET birth_year = 2000 WHERE birth_year is null;


---TABLO İSMİ DEĞİŞME
ALTER  TABLE  accounts RENAME TO hesaplar;
ALTER  TABLE  hesaplar RENAME TO accounts;
