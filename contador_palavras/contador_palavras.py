qtd_caracter, qtd_linhas, qtd_palavras = 0, 0, 0
dicionario_palavras = {}

with open("./contador_palavras/poema.txt", 'r', encoding="utf-8") as file:
    for linha in file.readlines():
        qtd_caracter+= len(linha)   #conta quantidade de caracteres
        
        qtd_linhas += 1             #conta quantidade de linhas
        
        linha = linha.split()
        qtd_palavras += len(linha)  #conta quantidade de palavras
        
        for palavra in linha:
            palavra_formatada = palavra.capitalize()
            palavra_formatada = palavra_formatada.strip(",;.!?")  #formatação das palavras
            
            if palavra_formatada in dicionario_palavras:
                dicionario_palavras[palavra_formatada] += 1       #conta quantidade de cada palavra individualmente
            else:
                dicionario_palavras[palavra_formatada] = 1
            
print(f"Número de Caracteres: {qtd_caracter} \nNúmero de Linhas: {qtd_linhas} \nNúmero de Palavras: {qtd_palavras} \n\nQuantidade de cada palavra:")

for key, value in dicionario_palavras.items():
    print(f"{key}: {value}")
