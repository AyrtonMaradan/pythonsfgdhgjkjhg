nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
notes = []
for i in range (nombreEtudiants) :
    print("note étudiant {} : ".format(i))
    a = float(input())
    while True:
        while a<0 or a>20 :
            print("veuillez saisir une note comprise entre 0 et 20 : ")
            a = float(input())
        break
    notes.append(a)
    moyenne=moyenne+notes[i]
moyenne=moyenne/nombreEtudiants
print("moyenne de classe :" ,moyenne)
print("Numéro de l'Etudiant | note | ecart a la moyenne")
for i in range (nombreEtudiants):
    x=notes[i]-moyenne
    print ("{}".format(i) , "| {}".format(notes[i]), "| {}".format(x))