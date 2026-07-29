produtos = ["Mouse", "Teclado", "Monitor", "Headset"]
precos = [80, 150, 900, 200]
dic = {produtos[i]:precos[i] for i in range(len(precos))}
acima_150 = {produtos[i]:precos[i] for i in range(len(precos)) if precos[i] > 150}

print('produtos:', dic)
print('produtos acima de R$150:', acima_150)
