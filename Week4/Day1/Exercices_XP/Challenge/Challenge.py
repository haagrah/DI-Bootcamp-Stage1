Caracteres = input("Saisir un text : ")
Caracteres = Caracteres.replace(" ", "")
print(Caracteres)
taille = len(Caracteres)
if taille<10:
    print(f"Chaine pas assez longue {taille} caractere") 
else:
    print(f"Chaine trop longue {taille} caractere") 
print(f"le premier caractere est {Caracteres[0]} et le dernier {Caracteres[-1]}") 

for i in range(taille+1):
    print(Caracteres[:+i])

