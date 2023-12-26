
numbers = []
a = input('enter les resultats stp, stop pr arreter')
while a != 'stop':
    numbers.append(int(a))
    a = input('enter les resultats stp, stop pr arreter')

average = sum(numbers) / len(numbers)
max_result = max(numbers)

print(numbers)
print(average)
print(max_result)

