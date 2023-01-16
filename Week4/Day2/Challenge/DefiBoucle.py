#Exercice 1
number = int(input("Entrer un nombre : "))
length = int(input("Entrer une taille en nombre : "))
Liste = []
while len(Liste)<=length:
    if number%number==0 and number%1==0:
        Liste.append(number)
        number+=number
    if len(Liste)==length:
        break
print(Liste)

#Exercice 2
newChaine = input("Veillez saisir une phrase : ")
chaine = ""
for i in newChaine:
    if i not in chaine:
        chaine += i
print(f"Phrase entrée : {newChaine}")
print(f"votre phrase sans doublons {chaine}")
