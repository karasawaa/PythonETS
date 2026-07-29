produtos = {"Mouse": 80, "Teclado": 150, "Monitor": 900, "Headset": 200}
prod_10 = {i: round(produtos[i]*1.1, 2) for i in produtos}

print('produtos:', produtos)
print('aumento de 10%:', prod_10)
