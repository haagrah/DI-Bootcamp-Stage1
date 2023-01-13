Caractere = input("Saisir un text : ")
Caractere = Caractere.replace(" ", "")
print(Caractere)
taille = len(Caractere)
if taille<10:
    print(f"Chaine pas assez longue {taille} caractere") 
else:
    print(f"Chaine trop longue {taille} caractere") 
print(f"le premier caractere est {Caractere[0]} et le dernier {Caractere[-1]}") 
for i in range(taille+1):
    print(Caractere[:+i])