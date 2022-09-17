meyveler    = list( )
sebzeler    = list( )
musteriler  = [ ]

ELMA        = 0
ARMUT       = 0
MUZ         = 0
KIRAZ       = 0
CILEK       = 0
PATLICAN    = 0
PADDES      = 0
DOMAT       = 0
BIBER       = 0
SOGAN       = 0

print("************     PYTHON MANAVINA HOŞ GELDİNİZ       ************")
while True:
	print("Meyve mi, Sebze mi istersiniz?(M/S). Çıkmak için (Ç)")
	secim =  input("Seçiminiz: ").upper()
	
	if secim == "M":
		while True:
			print("""
				1- Elma
				2- Armut
				3- Muz
				4- Kiraz
				5- Çilek
				6- Anamenü
			""")
			meyve = input("Seçiminiz: ")
			if meyve.isdigit() == False:
				print("Hatalı seçim")
				continue
			else:
				if meyve == "1":
					if "ELMA" not in meyveler:
						meyveler.append("ELMA")
						ELMA += int(input("Kaç kilo elma istersiniz ?"))
						donus =  input("Başka bir arzunuz var mı ?(E/H)").upper()
						if donus == "E":
							continue
						else:
							break
							
				elif meyve == "2":
					if "ARMUT" not in meyveler:
						meyveler.append( "ARMUT" )
						ARMUT += int( input( "Kaç kilo armut istersiniz ?" ) )
						donus = input( "Başka bir arzunuz var mı ?(E/H)" ).upper( )
						if donus == "E":
							continue
						else:
							break
				elif meyve == "3":
					if "MUZ" not in meyveler:
						meyveler.append( "MUZ" )
						MUZ += int( input( "Kaç kilo muz istersiniz ?" ) )
						donus = input( "Başka bir arzunuz var mı ?(E/H)" ).upper( )
						if donus == "E":
							continue
						else:
							break
				elif meyve == "4":
					if "KIRAZ" not in meyveler:
						meyveler.append( "KIRAZ" )
						KIRAZ += int( input( "Kaç kilo kiraz istersiniz ?" ) )
						donus = input( "Başka bir arzunuz var mı ?(E/H)" ).upper( )
						if donus == "E":
							continue
						else:
							break
				elif meyve == "5":
					if "CILEK" not in meyveler:
						meyveler.append( "CILEK" )
						CILEK += int( input( "Kaç kilo çilek istersiniz ?" ) )
						donus = input( "Başka bir arzunuz var mı ?(E/H)" ).upper( )
						if donus == "E":
							continue
						else:
							break
				elif meyve == "6":
					break
					
		
		
	elif secim == "S":
		pass
	elif secim == "Ç":
		break
	else:
		print("Hatalı seçim !")
		continue




