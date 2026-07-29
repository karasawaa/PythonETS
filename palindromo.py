palavra = input("Digite uma Palavra: ")
palavra = palavra.replace(" ", "")
palavra = palavra.lower()

tamanho = len(palavra)
inverso = []

for i in range(tamanho-1,-1,-1):
    inverso.append(palavra[i])
        
inverso = ''.join(inverso)
print(f"A palavra ao contrário é {inverso}")

if palavra == inverso:
    print("\nÉ UM PALÍNDROMO!!!!!!!🎉🎉🎉")
else: 
    print("\nNão é um palíndromo.👎👎👎👎")