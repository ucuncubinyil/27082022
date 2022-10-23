# pip install psycopg2

import psycopg2
from Config import config


def connect( ):
	conn = None
	try:
		params = config( )
		print( params )
		print( "Veri tabanına bağlanıyorum" )
		conn = psycopg2.connect( **params )
		cursor = conn.cursor( )
		cursor.execute( " select version() " )
		db_version = cursor.fetchone( )
		print( f"DB VERSION: {db_version}" )
		conn.close( )
	except(Exception, psycopg2.DataError) as err:
		print( err )


def insert_account( user_name: str, password: str, email: str, birth_year: int ):
	sql = """INSERT INTO accounts(user_name, password, email,created_on, birth_year)
				VALUES (%s, %s, %s,current_timestamp, %s) RETURNING id"""
	conn = None
	id = None
	
	try:
		params = config( )
		print( "Veritabanına bağlanıyorum" )
		
		conn = psycopg2.connect( **params )
		cursor = conn.cursor( )
		
		cursor.execute( sql, (user_name, password, email, birth_year) )
		id = cursor.fetchone( )
		print( f"Ekleme işlemi başarılı. Eklenen son kaydın id si: {id}" )
		conn.commit( )
	except(Exception, psycopg2.DataError) as err:
		print( err )
	
	finally:
		if conn is not None:
			conn.close( )


# insert_account("cemal_ozturk2", "cemal442", "cemal2@ozturk.com", 1965)

def list_accounts( ):
	conn = None
	account_list = tuple( )
	
	try:
		params = config( )
		print( "Veritabanına bağlanıyorum" )
		
		conn = psycopg2.connect( **params )
		cursor = conn.cursor( )
		
		cursor.execute( "select  * from accounts" )
		
		account_list = cursor.fetchall( )
		conn.commit( )
	except (Exception, psycopg2.DataError) as err:
		print( err )
	
	finally:
		if conn is not None:
			conn.close( )
			return account_list


# liste = list_accounts()
#
# for i in liste:
# 	for z in i:
# 		print(z)


def insert_account_list( account_list ):
	sql = """INSERT INTO accounts(user_name, password, email,created_on, birth_year)
					VALUES (%s, %s, %s,current_timestamp, %s) """
	conn = None
	try:
		params = config( )
		print( "Veritabanına bağlanıyorum" )
		conn = psycopg2.connect( **params )
		cursor = conn.cursor( )
		cursor.executemany( sql, account_list ) # çoklu kayıt
		conn.commit( )
		print("Kayıtlar eklendi")
	except (Exception, psycopg2.DataError) as err:
		print( err )
	finally:
		if conn is not None:
			conn.close( )

kullanici_listesi = [
		
		("murat_kaya", "murat34", "murat@murat.com", 1995),
		("ahmet_yildirim", "sıvasspor", "ahmet@sivasli.com", 1992)
		]

insert_account_list(kullanici_listesi)