########### Exercice 1 ########

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dico=dict(zip(keys,values))
print(dico)


########### Exercice 2 ########

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
prix = 0
for x,y in family.items():
    if y< 3 :
        print("C'est gratuit pour : ",x)
    elif y <= 12 :
        print(x,"devra payer :",10)
        prix += 10
    else :
        print(x, "devra payer :", 15)
        prix += 15
        
print("Coût total :",prix)


########### Exercice 3 ########

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": ["Amancio", "Ortega", "Gaona"],
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}
print(brand)

brand["number_stores"] = 2

print("Les clients de Zara sont tous ceux voulant faire "
      "des achats de \nvêtements pour : ", brand["type_of_clothes"])

brand["country_creation"] = "Spain"

if brand["international_competitors"] :
    brand["international_competitors"].append("Desigual")

del brand["creation_date"]

print(brand["international_competitors"][-1])

print(brand["major_color"]["US"])

print(len(brand.keys()))

print(brand.keys())

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

brand.update(more_on_zara)

print(brand["number_stores"])



########### Exercice 4 ########

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
#1
num =[z for z,y in enumerate(users)]
disney_users_A = dict(zip(users,num))
print(disney_users_A)
#2
disney_users_B = dict(zip(num,users))
print(disney_users_B)
#3
disney_users_C = dict(zip(sorted(users),num))
print(disney_users_C)
#4
#1
users1 = []
for x in users :
    if "i" in x :
        users1.append(x)
disney_users_A = dict(zip(users1,num))
print(disney_users_A)
#2
users2 = []
for x in users :
    if "m" == x[0].lower() or "p" == x[0].lower() :
        users2.append(x)
disney_users_A = dict(zip(users2,num))
print(disney_users_A)