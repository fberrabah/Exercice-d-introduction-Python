#afficher le commentaire 
print("Exercice 1\n")
print("Hello World ")
farid="Hello World\n"
print(farid)

#afficher les résultats
print ("Exercice 2\n")
try: 12/0
except:
    print (3*3 ,"Impossible de diviser par 0" ,4+9+78 ,12-7, 5e4)

#Message de bienvenue
print("Exercice 3\n")
choix=input('Bonjour indiquer votre nom et prénom :')
print(" Bienvenue " ""  + choix)    
#Nom et prenom
print("Exercice 4\n")
nom = "Berrabah"
prenom = "Farid"
print("Bonjour {} {}" .format(nom,prenom))
#interger!
print("Exercice 5\n")
myNumber = "123"
print(int (myNumber))
#majuscule MINUSCULE 
print("Exercice 6\n")
mot=input('Bonjour écriver votre text :')
print(mot.upper())
print(mot.lower())