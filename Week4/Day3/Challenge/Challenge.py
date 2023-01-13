####Challenge 1
sortie = {}
mot = input("Veillez saisir un mot : ")
for i in range(len(mot)):
  if mot[i] in sortie :
    sortie[mot[i]].append(i)
  else :
    sortie[mot[i]] = [i]
print(sortie)

#####Challenge 2
wallet = 2000
items_purchase = {
  "Water": 1,
  "Bread": 3,
  "TV": 1000,
  "Fertilizer": 20,
"Apple": 4,
  "Honey": 3,
  "Fan": 14,
  "Bananas": 4,
  "Pan": 100,
  "Spoon": 2
}
article = [article for article in items_purchase if items_purchase[article] <= wallet]
print(article)