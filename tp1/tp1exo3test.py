from random import randint
a=randint(1,31)
b=randint(1,24)
c=randint(0,59)
jour=a
heure=b
minute=c
total=0
total=((((jour*24)+heure)*60)+minute)
print( total , " est le nombre de minute écoulés depuis le début du mois " , total/60 , " est le nombre d'heure écoulé depuis le début du mois " , total/60/24, " est le nombre de jour écoulé depuis le début du mois " )
