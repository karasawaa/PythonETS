import os
dicionario = {}
os.system("cls")

with open("./criador_tabelas/dataframe.txt", 'r', encoding="utf-8") as file:
    linha = file.readline()
        
    linha = linha.split(",")
    linha[-1] = linha[-1].replace("\n", "")
    
    for palavra in linha:
        dicionario[palavra] = []
                
    for linha in file.readlines():
        linha = linha.split(",")
        linha[-1] = linha[-1].replace("\n", "")
        
        for key, value in zip(dicionario.keys(), linha):
            dicionario[key].append(value)

print("  |  ".join(dicionario.keys()))

for i in range(len(dicionario[list(dicionario.keys())[0]]) ):
    linha_formatada = [dicionario[coluna][i] for coluna in list(dicionario.keys())]
    print("  |  ".join(linha_formatada))
