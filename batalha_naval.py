import random
import os

navio, linha, coluna = 0, 0, 0
tiros = 20
jogador = [['𝟏','𓂃','𓂃','𓂃','𓂃','𓂃','𓂃'],
           ['𝟐','𓂃','𓂃','𓂃','𓂃','𓂃','𓂃'],
           ['𝟑','𓂃','𓂃','𓂃','𓂃','𓂃','𓂃'],
           ['𝟒','𓂃','𓂃','𓂃','𓂃','𓂃','𓂃'],
           ['𝟓','𓂃','𓂃','𓂃','𓂃','𓂃','𓂃'],
           ['𝟔','𓂃','𓂃','𓂃','𓂃','𓂃','𓂃']]
mesa =    [['𝟏','𓂃','𓂃','𓂃','𓂃','𓂃','𓂃'],
           ['𝟐','𓂃','𓂃','𓂃','𓂃','𓂃','𓂃'],
           ['𝟑','𓂃','𓂃','𓂃','𓂃','𓂃','𓂃'],
           ['𝟒','𓂃','𓂃','𓂃','𓂃','𓂃','𓂃'],
           ['𝟓','𓂃','𓂃','𓂃','𓂃','𓂃','𓂃'],
           ['𝟔','𓂃','𓂃','𓂃','𓂃','𓂃','𓂃']]

def exibe_tabuleiro(tabuleiro):
    print("\033[38;5;39m")
    print('𝟎 𝟏 𝟐 𝟑 𝟒 𝟓 𝟔')
    for i in tabuleiro: 
        for j in i:
            print(j, end=' ')
        print('')  
    print("\033[0m")

def posição(navio):
    direcao = random.randint(0, 1)
    x = 0
    
    match direcao: 
        case 0: #HORIZONTAL
            if navio == 4:
                while x < 4:
                    linha, coluna = random.randint(0, 2), random.randint(1, 6)
                    if mesa[linha+1][coluna] != "𓂃" or mesa[linha+2][coluna] != "𓂃" or mesa[linha+3][coluna] != "𓂃":
                        None                
                    elif mesa[linha][coluna] == "𓂃":
                        for i in range(4):
                            mesa[linha][coluna] = "4⃣" 
                            linha += 1
                            x += 1
                    else:
                        None
            if navio == 3:
                while x < 3:
                    linha, coluna = random.randint(0, 3), random.randint(1, 6)
                    if mesa[linha+1][coluna] != "𓂃" or mesa[linha+2][coluna] != "𓂃":
                        None      
                    elif mesa[linha][coluna] == "𓂃":
                        for i in range(3):
                            mesa[linha][coluna] = "3⃣" 
                            linha += 1
                            x += 1
                    else:
                        None
            if navio == 2:
                while x < 2:
                    linha, coluna = random.randint(0, 4), random.randint(1, 6)
                    if mesa[linha+1][coluna] != "𓂃":
                        None      
                    elif mesa[linha][coluna] == "𓂃":
                        for i in range(2):
                            mesa[linha][coluna] = "2⃣" 
                            linha += 1
                            x += 1
                    else:
                        None
        case 1: #VERTICAL
            if navio == 4:
                while x < 4:
                    linha, coluna = random.randint(0, 5), random.randint(1, 3)
                    if mesa[linha][coluna+1] != "𓂃" or mesa[linha][coluna+2] != "𓂃" or mesa[linha][coluna+3] != "𓂃":
                        None      
                    elif mesa[linha][coluna] == "𓂃":
                        for i in range(4):
                            mesa[linha][coluna] = "4⃣" 
                            coluna += 1
                            x += 1
                    else:
                        None
            if navio == 3:
                while x < 3:
                    linha, coluna = random.randint(0, 5), random.randint(1, 4)
                    if mesa[linha][coluna+1] != "𓂃" or mesa[linha][coluna+2] != "𓂃":
                        None      
                    elif mesa[linha][coluna] == "𓂃":
                        for i in range(3):
                            mesa[linha][coluna] = "3⃣" 
                            coluna += 1
                            x += 1
                    else:
                        None
            if navio == 2:
                while x < 2:
                    linha, coluna = random.randint(0, 5), random.randint(1, 5)
                    if mesa[linha][coluna+1] != "𓂃":
                        None      
                    elif mesa[linha][coluna] == "𓂃":
                        for i in range(2):
                            mesa[linha][coluna] = "2⃣" 
                            coluna += 1
                            x += 1
                    else:
                        None
os.system("cls")

posição(4)
posição(3)
posição(3)
posição(2)


 
print('''\033[38;5;130m
            ⣀⠀⠤⠴⠶⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣾⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠂⠉⡇⠀⠀⠀⢰⣿⣿⣿⣿⣧⠀⠀⢀⣄⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣶⣶⣷⠀⠀⠀⠸⠟⠁⠀⡇⠀⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⠟⢹⣋⣀⡀⢀⣤⣶⣿⣿⣿⣿⣿⡿⠛⣠⣼⣿⡟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣴⣾⣿⣿⣿⣿⢁⣾⣿⣿⣿⣿⣿⣿⡿⢁⣾⣿⣿⣿⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⠿⠇⠀⠀⠀⠀
⠀⠀⠀⠳⣤⣙⠟⠛⢻⠿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣇⠘⠉⠀⢸⠀⢀⣠⠀⠀⠀
⠀⠀⠀⠀⠈⠻⣷⣦⣼⠀⠀⠀⢻⣿⣿⠿⢿⡿⠿⣿⡄⠀⠀⣼⣷⣿⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣶⣄⡈⠉⠀⠀⢸⡇⠀⠀⠉⠂⠀⣿⣿⣿⣧⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣷⣤⣀⣸⣧⣠⣤⣴⣶⣾⣿⣿⣿⡿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[0m''')
print("<------> BATALHA NAVAL <------>")
exibe_tabuleiro(jogador)

while tiros > 0:
    pontos = 0
    
    for i in range(len(mesa)): 
        for j in range(len(mesa[i])):
            if (mesa[i][j] == "2⃣" and jogador[i][j] == "2⃣") or (mesa[i][j] == "3⃣" and jogador[i][j] == "3⃣") or (mesa[i][j] == "4⃣" and jogador[i][j] == "4⃣") :
                pontos+=1
    
    if pontos >= 12:
                print("Parabéns!!!! Ganhou!!!")
                break
                
    try:
        linha = int(input(f"Você possui {tiros} tiros \nDigite em qual linha gostaria de atirar: "))
        coluna = int(input("Digite em qual coluna gostaria de atirar: ")) + 1

        if (mesa[linha-1][coluna-1] == "2⃣" and jogador[linha-1][coluna-1] == "𓂃"):
            jogador[linha-1][coluna-1] = "2⃣"
            tiros -= 1
        elif (mesa[linha-1][coluna-1] == "3⃣" and jogador[linha-1][coluna-1] == "𓂃"):
            jogador[linha-1][coluna-1] = "3⃣"
            tiros -= 1
        elif (mesa[linha-1][coluna-1] == "4⃣" and jogador[linha-1][coluna-1] == "𓂃"):
            jogador[linha-1][coluna-1] = "4⃣"
            tiros -= 1
        elif mesa[linha-1][coluna-1] == "𓂃" and jogador[linha-1][coluna-1] == "𓂃":
            jogador[linha-1][coluna-1] = "𖦹"
            tiros -= 1
        elif jogador[linha-1][coluna-1] == "𖦹" or jogador[linha-1][coluna-1] != "𓂃":
            print("Ja foi ai amigão")

        exibe_tabuleiro(jogador)
        
        if pontos >= 12:
            print("Parabéns!!!! Ganhou!!!")
            break
    except:
        print("Opção inválida! Digite novamente")
        
if (tiros <= 0 and pontos < 12):
    print("Voce perdeu!!!!!!\n Tabuleiro:")
    exibe_tabuleiro(mesa)