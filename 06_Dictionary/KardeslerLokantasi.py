masalar = {
		"Masa-1": "F", "Masa-2": "F",
		"Masa-3": "F", "Masa-4": "F",
		"Masa-5": "F"
		}
corbalar = {
		"1-Mercimek": "7.00", "2-Ezogelin": "7.00",
		"3-Yayla":    "6.00"
		}

baliklar = { "1-Mezgit": "27.00", "2-Palamut": "32.00", "3-Çupra": "40.00" }
etler = { "1-Pirzola": "56.00", "2-Biftek": "65.00", "3-Lokum": "45.00" }
makarnalar = {
		"1-Bonolezli": "35.00", "2-Körili": "35.00",
		"3-Spagetti":  "35.00"
		}
ara_sicaklar = {
		"1-İçli Köfte": "20.00", "2-Sigara Böreği": "40.00",
		"3-Patso":      "10.00"
		}

salata = { "1-Çoban": "20.00", "2-Sezar": "45.00", "3-Mevsim": "20.00" }

icecekler = { "1-Kola": "10.00", "2-Ayran": "8.00", "3-Su": "5.00", "4-Şalgam": "15.00" }

siparisler = dict( )

while True:
	
	menu = int( input( """
				SİPARİŞ ALMAK İÇİN          1
				HESAP ALMAK İÇİN            2
				MENÜ GÖRMEK İÇİN            3
				ÇIKIŞ İÇİN                  4
				Seçiminiz:"""
	                   )
	            )
	
	if menu == 4:
		print( "Hoşçakalın ..." )
		break
	elif menu == 1:
		kisi_sayisi = int( input( "Kaç kişiyiz?" ) )
		musteri_masasi = str( )
		for masa in masalar:
			if masalar[ masa ] == "F":
				musteri_masasi = masa
				print( musteri_masasi )
				masalar[ masa ] = "T"
				break
		
		siparis = dict( )
		
		for i in range( kisi_sayisi ):
			print( i + 1, ". müşteri siparişi" )
			
			while True:
				print( """
					1- Çorba çeşitleri
					2- Balık çeşitleri
					3- Et çeşitleri
					4- Makarna çeşitleri
					5- Arasıcak çeşitleri
					6- Salata çeşitleri
					7- İçeçek çeşitleri
				"""
				       )
				secim = int( input( "Seçiminiz: " ) )
				
				if secim == 1:
					for corba, fiyat in corbalar.items( ):
						print( corba, "\t\t", fiyat )
					
					secim_corba = int( input( "Çorba seçiminiz" ) )
					
					if secim_corba == 1:
						siparis[ "Mercimek Çorbası" ] = "7.00"
					elif secim_corba == 2:
						siparis[ "Ezo Gelin" ] = "7.00"
					else:
						siparis[ "Yayla" ] = "6.00"
				
				elif secim == 2:
					for balik, fiyat in baliklar.items( ):
						print( f"{balik}     {fiyat}" )
					secim_balik = int( input( "Balık Seçiminiz: " ) )
					
					if secim_balik == 1:
						siparis[ "Mezgit" ] = "27.00"
					elif secim_balik == 2:
						siparis[ "Palamut" ] = "32.00"
					else:
						siparis[ "Çupra" ] = "40.00"
				
				cevap = input( "Başka bir arzunuz var mı ?(E/H)" ).upper( )
				if cevap == "E":
					continue
				else:
					siparisler[ masa ] = siparis
					break
	
	
	
	elif menu == 2:
		print( "Hesap Bölümü" )
		for i in siparisler:
			print( i, "==========>", siparisler[ i ] )
		hesap = 0
		
		masa_hesabi =  input("Hangi masa hesabı isteniliyor ?")
		for i in siparisler["Masa-"+ masa_hesabi].values():
			hesap += float(i)
		print(hesap)
		
		hesap_odendi_mi =  input("Hesap ödendi mi ? (E/H)").upper()
		
		if hesap_odendi_mi == "E":
			masalar["Masa-"+masa_hesabi] = "F"
		
		for masa, deger in masalar.items( ):
			print( masa, "\t\t", deger )
			