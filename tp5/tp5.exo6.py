#variable :
voyelle=["a","e","i","o","u","y"]
nbvoy=0
pourvoy=0
compteur=0
occurrence=0
a=0
long=0


#saisit de la chaine de caractere et deduction de sa longeur :
T=str(input("veuillez saisir votre chaine caractere :"))
print("la chaine de caractere contient :",len(T),"caracteres de long")
T.lower()


#nombre et pourcentge de voyelle :
for i in T :
    if i in voyelle :
        nbvoy= nbvoy+1
pourvoy=(100*nbvoy)/len(T)
pourvoy=round(pourvoy,1)
print("il y a",pourvoy,"% de voyelle")

#wagon :
for i in T :
    occurrence=T.count("wagon")
    long +=1

while a < long-4:
    if T[a]=='w':
        if T[a+1] == 'a':
            if T[a+2] == 'g':
                if T[a+3] == 'o':
                    if T[a+4] == 'n':
                        print("l'indice du mot wagon est présent au",a,"ieme indice")
    a += 1
print("Le nombre de fois que le mot wagon apparait est de",occurrence)
