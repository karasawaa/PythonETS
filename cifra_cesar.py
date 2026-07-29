alfabeto = 'abcdefghijklmnopqrstuvwxyz'
palavra_codificada = []

palavra = input("Digite a palavra ou frase que deseja codificar: ")
num = input("Digite o número para codificação: ")

for i in range(len(palavra)):
    posicao = alfabeto.find(palavra[i].lower()) + 3

    if palavra[i].isalpha() == True:
        if posicao == 26:
            palavra_codificada.append(alfabeto[0])
        elif posicao == 27:
            palavra_codificada.append(alfabeto[1])
        elif posicao == 28:
            palavra_codificada.append(alfabeto[2])        
        else: 
            palavra_codificada.append(alfabeto[posicao])
    else:
        palavra_codificada.append(" ")
    
palavra_codificada = ''.join(palavra_codificada)
print(palavra_codificada)