import os.path
import datetime
path=input("veuillez saisir le nom d'un fichier :")
path2=input("veuillez saisir le nom d'un autre fichier :")
if os.path.isfile(path)==True :
    print("Le fichier",path,"existe bien.")
else :
    print("le fichier",path,"n'existe pas.")
if os.path.isfile(path2)==True:
    print("le fichier",path2,"existe bien.")
else:
    print("le fichier",path2,"n'existe pas.")
if os.path.isfile(path2)==True:
    if os.path.isfile(path) == True:
        if os.path.getmtime(path)> os.path.getmtime(path2):
            print("LE fichier qui a été modifié recemment est le",path,". Il a été modifié le",datetime.datetime.fromtimestamp(os.path.getmtime(path)))
        else:
            print("LE fichier qui a été modifié recemment est le", path2, ". Il a éé modifié le",datetime.datetime.fromtimestamp(os.path.getmtime(path2)))