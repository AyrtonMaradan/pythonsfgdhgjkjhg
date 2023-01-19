money=int(input("veuillez saisir une somme :"))
if money!= 0 :
    a=int(money/100)
    money=money%100
    if money!=0 :
        b=int(money/50)
        money=money%50
        if money !=0 :
            c=int(money/10)
            money=money%10
            if money != 0:
                d=int(money/2)
                money=money%2
                if money !=0 :
                    e=int(money/1)
                    money= money%1
                    if money==0 :
                        print("il y a",a,"billets de 100, il y a",b,"billets de 50, il y a",c,"billets de 10, il y a",d,"piece de 2, il y a",e,"piece de 1.")
