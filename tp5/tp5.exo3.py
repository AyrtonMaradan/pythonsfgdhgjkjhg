#palindrome
corriger=""
a=0
b=0

#introduction du mots :
mots=str(input("entrez un mots ou une phrase :"))
mots=str.lower(mots)

#verification du mots
for i in mots:
    if (i.isalpha()) == True :
        corriger += i

#verification palyndrome
if corriger == str(corriger)[::-1] :
    print("c'est un palindrome")
else :
    print("ce n'est pas un palindrome")
