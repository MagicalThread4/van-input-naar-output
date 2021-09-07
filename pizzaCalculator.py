# Rob Koster Opdracht pizza calculator



print("----------------------------------------------")
print("Kosten Small = €4.00")
print("Kosten Medium = €6.00")
print("Kosten Large = €8.00")
print("----------------------------------------------")



print("Welke afmeting pizza wilt u? Small, Medium of Large")
HoeveelS = int(input("Hoeveel Small wilt u? :"))
HoeveelM = int(input("Hoeveel Medium wilt u? :"))
HoeveelL = int(input("Hoeveel Large wilt u? :"))



Totaalprijssmall = HoeveelS * 4.00
Totaalprijsmedium = HoeveelM * 6.00
Totaalprijslarge = HoeveelL * 8.00
Totaalprijs = Totaalprijssmall  + Totaalprijsmedium + Totaalprijslarge



print("--------------------------------------------------------------------------------------------")
print("U heeft " + str(HoeveelS) + " small pizza's voor €" + str(Totaalprijssmall))
print("U heeft " + str(HoeveelM) + " Medium pizza's voor €" + str(Totaalprijsmedium))
print("U heeft " + str(HoeveelL) + " Large pizza's voor €" + str(Totaalprijslarge))
print("--------------------------------------------------------------------------------------------")
print()



print("----------------------------------------------")
print("De totaal prijs is " + str(Totaalprijs))
print("----------------------------------------------")