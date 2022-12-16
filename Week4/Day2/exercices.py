####boucle While################
i=0
while i<10:
    print(i)
    i=i+1
    
    
############Boucle for###########

for i in range(10):
    print(i)
    
    
    
############Exercice###########
listes=["Armand","Roland","Pacome","Salif","Fanta","Sali","Armel"]

# for i in listes:
#     print(i)

######
liste=[{x**2:listes[x]} for x in range(len(listes))]
print(liste)
# listes=["Armand","Roland","Pacome","Salif","Fanta","Sali","Armel"]
diction = {}
for i in range(len(listes)):
   diction[i**i] = listes[i]
print(diction)

for i in diction:
    print(i,diction)