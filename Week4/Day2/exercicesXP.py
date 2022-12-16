########### Exercice 1 ########

my_fav_numbers={1, 2, 3, 4, 5, 6, 7}

my_fav_numbers.add(9)

my_fav_numbers.add(11)

my_fav_numbers.pop()

friend_fav_numbers=[10, 20, 30, 40, 50, 60, 70, 80, 90]

our_fav_numbers=my_fav_numbers.union(friend_fav_numbers)

print(our_fav_numbers)


########### Exercice 2 ########

mon_tuple = (4)
#mon_tuple = mon_tuple + (5,7)
# Non ce n'est pas possible#TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
print(mon_tuple)
##  Contrairement aux listes, les tuples ne sont pas modifiables.


########### Exercice 3 ########

basket = ["Banana","Apples","Oranges","Blueberries"];
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0,"Apples")
basket.count("Apples")
basket.clear()

print(basket)


########### Exercice 4 ########

nbr = 1
tableau = []
while nbr <5 :
    nbr += 0.5
    tableau.append(nbr)
print(tableau)


########### Exercice 5 ########

for i in range(1,21):
     if i%2 == 0 :
        print(i)


########### Exercice 6 ########

while(1) :
    nom = input("Entrez votre nom ")
    if nom.lower() == "Guire" :
        break  


########### Exercice 7 ########

favorite_fruit = input("Entrez vos fuits preferé,separer les par un espace")
favorite_fruit.split(" ")
fruit = input("Entrez le nom d'un fruit")
for x in favorite_fruit:
	if x == fruit:
		print("vous avez choisis un de vos fruits preferé!!prendre plaisir")
	else:
		print("Vous avez choisi un nouveau fruit. J'espère que tu apprécies")


########### Exercice 8 ########

garniture  =  "" 
serie  =  "" 
prix  =  0 ; 
while  garniture . lower ()  !=  "quitter"  : 
    garniture  =  input ( "Entrez une serie de garnitures de pizza" ) 
    if  garniture . lower ()  !=  "quitter"  : 
        print ( "Nous ajouterons cette garniture" ) 
        serie  +=  garniture  +  " " 
    prix  +=  12.5 

print ( serie , " Et le prix total est :" , prix )


########### Exercice 9 ########

age = input("Entrez l'âge de la 1 ère personne")
prix = 0
while age.lower() != "fin" :
    if int(age) < 3 :
        print("C'est gratuit pour toi")
    elif int(age) <= 12 :
        prix += 10
    else :
        prix += 15
    age = input("Entrez l'âge d'une autre personne ou 'fin' pour avoir le prix total :")
print(prix)


########### Exercice 10 ########

sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []

while 1 :
    fini = input("Ya t il un sandwich de fini? 'oui' ou 'non' ")
    if fini.lower() == "oui" and sandwich_orders != []:
       finished_sandwiches.append(sandwich_orders[0])
       sandwich_orders.remove(sandwich_orders[0])
       if len(sandwich_orders) != 0 :
            print("Plus que", len(sandwich_orders))
       else :
            print("Finish")
    elif sandwich_orders == [] :
        print("Listes des sandwich préparés :")
        for sandwich in finished_sandwiches :
            print(sandwich)
        break
    else :
        print("Ok j'attends encore un peu")



########### Exercice 11 ########

sandwich_orders = ["Pastrami sandwich", "Tuna sandwich", "Avocado sandwich","Pastrami sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []
while 1 :
    if "Pastrami sandwich" in sandwich_orders :
        sandwich_orders.remove("Pastrami sandwich")
    else :
        break
print("Plus de Pastrami sandwich")
while sandwich_orders != [] :
    fini = input("Ya t il un sandwich de fini? 'oui' ou 'non' ")
    if fini.lower() == "oui" and sandwich_orders != []:
        finished_sandwiches.append(sandwich_orders[0])
        sandwich_orders.remove(sandwich_orders[0])
        if len(sandwich_orders) != 0 :
            print("Plus que", len(sandwich_orders))
        else :
            print("Finish")
    else :
        print("Ok j'attends encore un peu")

print("Listes des sandwich préparés :",finished_sandwiches)
