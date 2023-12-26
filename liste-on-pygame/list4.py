



resultats = input('Enter the marks ')
resultats=resultats.split(' ')

amount = 0

for result in resultats:
    if int(result) >= 200:
        amount += 1

print(resultats)
print(amount)