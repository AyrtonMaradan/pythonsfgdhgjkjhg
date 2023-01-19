#intro des variable
amelioration1=0
amelioration2=0

salaire=float(input("veuillez saisir le salaire/heure :"))
heure=int(input("veuillez saisir le nombre d'heure que vous avez effectué :"))
if 201 > heure > 160 :
    salaire1=salaire*160
    amelioration1=heure-160
    salaire2=(1.25*salaire)*amelioration1
    total=salaire1+salaire2
    print("Il y a 160 heures au tarif normale , et",amelioration1," heures à +25% ce qui lui fais 160 heures pour",salaire1,"euro et",amelioration1,"heures à +25% ce qui donne",salaire2,"euro. Il a gagné un total de",total,"euro" )
elif heure > 200 :
    salaire1=salaire*160
    salaire2=(1.25*salaire)*40
    amelioration2= heure-200
    salaire3=(1.50*salaire)*amelioration2
    total=salaire1+salaire2+salaire3
    print ("Il y a 160 heures au tarif normale , et 40 heures à +25% et",amelioration2,"heures à +50% ce qui lui fais 160 heures à",salaire1,"euro et 40 heures à +25% ce qui donne",salaire2,"et",amelioration2,"heures à +50% ce qui donne",salaire3,"euro . Il a gagné un total de",total,"euro" )
elif heure < 161 :
    salaire1=salaire*heure
    print("Il y a",heure,"heures de travail au tarifs basique ce qui donne un total de",salaire1,"euro de de salaire sur toutes ces heures")