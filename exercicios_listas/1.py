numeros = [12, 7, 9, 20, 15, 4, 18, 3, 10]
pares = [n for n in numeros if n % 2 == 0]

print('lista:', *numeros)
print('pares:', *pares)
