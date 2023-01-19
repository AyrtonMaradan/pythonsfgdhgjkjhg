#nom prénom demandé :
nom1=input("veuillez saisir votre nom ? ")
prenom1=input("veuillez saisir votre prenom ? ")
nom2=input("veuillez saisir votre nom 2 ? ")
prenom2=input("veuillez saisir votre prenom 2 ? ")

#changement de la chaine de caractere :
nom1=str.upper(nom1)
prenom1=str.capitalize(prenom1)
nom2=str.upper(nom2)
prenom2=str.capitalize(prenom2)

#ordre alphabetique :
if nom1 < nom2:
    print(nom1,prenom1,"\n",nom2,prenom2)
elif nom1 == nom2 :
    if prenom1 < prenom2 :
        print(nom1, prenom1, "\n", nom2, prenom2)
    else :
        print(nom2, prenom2, "\n", nom1, prenom1)
else :
    print(nom2, prenom2,"\n",nom1, prenom1)
