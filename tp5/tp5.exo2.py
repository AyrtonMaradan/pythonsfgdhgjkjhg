#initialisation des listes et variables :
s11=[]
coef=0
moy=0
rep=0
note=0
a=0
b=0
c=0

#initialisation des notes et moyennes :
rep=int(input("combien de note allez vous saisir : "))
for i in range (0,rep):
    s11=input("veuillez saisir la note du module et le coefficient correspondant :")
    s12=s11.split(" ")
    s13=float(s12[0])
    s14=float(s12[1])
    note=note+ s13*s14
    coef=coef+ s14
    if s13 < 8 :
        a=1

#clacule de la moyenne
moy=note/coef
moy=round(moy,1)

#verification de la moyenne
if moy >= 10 :
    b = 1
if moy < 10 :
    c = 1


#verification des conditions
if c==1 :
    print("l'eleve n'est pas admis car sa moyenne",moy,"est inferieur à 10")
if b==1 :
    print("l'eleve est admis avec une moyenne de ",moy)
if a==1 :
    print("l'eleve n est pas admis car il a une note inferieur à 8")


