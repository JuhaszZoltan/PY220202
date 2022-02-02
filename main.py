import random

lista = []

for n in range(10):
    lista.append(random.randint(34, 333) * 3)

for e in lista:
    print(e, end=' ')
print()

db_500nal_nagyobb = 0
for e in lista:
    if e > 500:
        db_500nal_nagyobb += 1
print(f'500nál nagyobb elemek száma: {db_500nal_nagyobb}')

db_500nal_kisebb = 0
sum_500nal_kisebb = 0
for e in lista:
    if e < 500:
        db_500nal_kisebb += 1
        sum_500nal_kisebb += e
avg_500nal_kisebb = sum_500nal_kisebb / db_500nal_kisebb
print(f'500nál kisebb elemek átlaga: {avg_500nal_kisebb}')

maxi = 0
for i in range(1, len(lista)):
    if lista[maxi] < lista[i]:
        maxi = i

print(f'legnagyobb elem: {lista[maxi]}')

i = 0
while i < len(lista) and lista[i] % 10 != 0:
    i += 1
if i < len(lista):
    print('van 0-ra végződő elem')
else:
    print('nincs 0ra végződő elem')

keresett_szam = int(input('írj be egy számot: '))
i = 0
while i < len(lista) and keresett_szam != lista[i]:
    i += 1
if i < len(lista):
    print(f'a keresett szám a lista {i} indexű eleme')
else:
    print(f'a keresett szám nincs benne a listában')