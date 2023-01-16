chaine = input('Veuillez entrer une chaine de caractere (La chaîne doit comporter 10 caractères): ')
longueur = len(chaine)
if (longueur > 10) : print("chaîne trop longue")
if (longueur < 10) : print("chaîne trop courte ")

print("Voici le premier caractere : \n")
print(chaine[0])
print("Voici le dernier caractere : \n")
print(chaine[-1])