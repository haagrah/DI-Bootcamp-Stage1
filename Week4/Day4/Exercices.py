class Voiture:
    marque = "Kia"
    def __init__(self):
        self.couleur = "Noir"
    def changeColor(self,coleur):
        self.couleur =coleur
    def delColor(self):
        self.couleur=""
voiture1 =Voiture()
voiture1.couleur
print(voiture1.couleur)
voiture1.changeColor("Red")
voiture1.couleur
print(voiture1.couleur)

voiture1.delColor()
voiture1.couleur
print(voiture1.couleur)




#######################################"""""

age = input("entrer votre age : ")
try:
    age = int(age)
except:
    print("Vous ne pouvez pas convertir un string en int")
print(age)