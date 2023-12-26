


resultat1 = []
resultat = []
compteur = 0

val = int(input('enter values '))

while val != 0:

    if val >= 200:
        resultat1.append(val)
        compteur = compteur + 1
       
    resultat.append(val)

    val = int(input('enter values '))


print(resultat)
print(resultat1)
print(compteur)