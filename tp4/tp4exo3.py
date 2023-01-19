nMax= int(input("Donnez la taille maximum de vos vecteur : "))
v1 = []
v2 = []
ps=0.0
print("Saisie du premier vecteur :")
for i in range (nMax) :
    a = float(input("v1 {} =".format(i)))
    v1.append(a)

print("Saisie du deuxieme vecteur :")
for i in range (nMax) :
    b = float(input("v2 {} =".format(i)))
    v2.append(b)

for i in range (nMax) :
    ps=ps+(v1[i]*v2[i])

print("Le produit scalaire de v1 par v2 vaut {}" .format(ps) )

