########### Exercice1 ########
print("Hello world\n"*4)

########### Exercice2 ########
print((99^3)*8)

######### Exercice 3 #########
5<3 #sortie false
3==3 #sortie true
3 == "3" #sortie false
# "3" > 3 affiche une erreur
"Hello" == "hello" #sortie false

######### Exercice 4 #########
computer_brand = "HP ProBook"
print("I have a " + computer_brand + " ""computer")

######### Exercice 5 #########
name="GUIRE"
age=21
shoe_size="XL"
info="je suis"" "+name+" " "j'ai"" ",age,"ans et ma pointure est"" "+shoe_size
print(info)

######### Exercice 6 #########
a=11
b=6
if a>b:
      print("hello world")


######### Exercice 7 #########
a= int(input("entrer un nombre " ""))
if (a%2==0):
      print("vous avez entrer un nombre pair")
else:
          print("vous avez entrer un nombre impair")


######### Exercice 8 #########

myname="Tatiana"
n=input("quel est votre nom ?" "")
if n==myname:
      print("nous avons les meme nom")
else:
      print("nous n'avons pas les meme nom")

######### Exercice  9 #########
m=float(input("Entrer votre taille" ""))
if m<145:
      print('Vous devez grandir un peu plus pour rouler')
else:
      print("Vous estes assez grand")
