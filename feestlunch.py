# 17 croissantjes van elk 39 eurocent
# 2 stokbroden van elk 2,78
# 3 kortingsbonnen van 50 eurocent

prijscroissantjes = 0.39
prijsstokbroden = 2.78
waardenkortingsbonnen = 0.50

hoeveelcroissantje = float(input("Hoeveel croissantjes wilt u: "))
hoeveelstokbroden = float(input("Hoeveel stokbroden wilt u: "))
hoeveelkortingsbonnen = float(input("Hoeveel kortingsbonnen heeft u: "))



bedrag1 = hoeveelcroissantje * prijscroissantjes 
bedrag2 = hoeveelstokbroden * prijsstokbroden 
korting = waardenkortingsbonnen * hoeveelkortingsbonnen 

totaal = bedrag1 + bedrag2 - korting 

print(" De feestlunch kost je bij de bakker " + str(totaal) + " voor  " + str(hoeveelcroissantje) + " croissantjes en voor " + str(hoeveelstokbroden) + " stokbroden als de " + str(hoeveelkortingsbonnen)  + " kortingsbonnen nog geldig zijn! ")
