#Condition True False 
print("Exercice 1\n")

Paris = ""
Marseille = "NUL"

print(len(Paris)==0)
print(len(Marseille)==0)

#Calculer l'age
print("Exercice 2\n")

date = input('Veuillez entrer l année en cours : ')
naissance = input ('Ainsi que votre année de naissance : ')

date = int(date)
naissance = int(naissance)
s=date - naissance

print(s)

voisin = input ("Quel âge à votre voisin :")

voisin = int(voisin)
v=s + voisin
v=str(v)

print("Vous avez " + v +"ans avec votre voisin")

#calculer le cout total avec %
print("Exercice 3\n")

chaussure = 70 
jean = 59  
tshirt = 20
total = chaussure+jean+tshirt

print("Le cout total de votre shooping est de {}".format(total *0.80))

#Faire une calculatrice
print("Exercice 4\n")

calcul = float(input ("Entrer votre donnée :"))
calcul1 = float(input ("Entrer votre nouvelle donnée :"))

print("Voici le résultat de vos 2 données : {}".format(calcul+calcul1))

#demande de nom sur le programme
print("Exercice 5\n")
prénom = input ("Entrer votre prénom :").upper()
nom = input ("Entrer votre nom :").upper()

print(prénom[0]+prénom[-1])
print(nom[0]+nom[-1]) 
print(prénom[0]+prénom[-1]+nom[0]+nom[-1])

age = float(input ("Entrer votre age:"))
total=round(age/33)
print("votre age divisé par 33 est :{}".format(total))