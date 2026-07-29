import random

saldo = 500

def compra(total, mao):
    carta = random.randint(0, 13)
    mao.append(baralho[carta])
    
    if type(baralho[carta]) == int:
        total += baralho[carta]
    else:
        if baralho[carta] == "A":
            total += 1
        elif (baralho[carta] == "J") or (baralho[carta] == "Q") or (baralho[carta] == "K") :
            total += 10
    
    baralho.pop(carta) 
    return total
    
class opcaoinvalida(Exception):
    pass

iniciar = input(f"Seu saldo é: {saldo}\nDeseja iniciar o jogo? (y/n): ")
while saldo > 0:
    if saldo != 500:
        iniciar = input(f"Seu saldo é: {saldo}\nDeseja jogar novamente? (y/n): ")
    try:        
        if iniciar in ["y", "n", "Y", "N"]:
            if iniciar == "n" or iniciar == "N":
                break
            if iniciar == "y" or iniciar == "Y":
                baralho = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] * 4
                mao_jogador = []
                mao_mesa = []
                total_jogador = 0
                total_mesa = 0
                        
                aposta = int(input("Qual será sua aposta em R$: "))
                if aposta > saldo:
                    raise Exception
                elif aposta < 1:
                    print("Digite um valor válido")
                else:   
                    for i in range(2):
                        total_jogador = compra(total_jogador, mao_jogador)
                        total_mesa = compra(total_mesa, mao_mesa)

                    print(f'Suas cartas são: {mao_jogador[0]} e {mao_jogador[1]}. Total: {total_jogador}\nUma das cartas da mesa é: {mao_mesa[random.randint(0, 1)]}')

                    while True:
                        if (mao_jogador[0] == "A" and ((mao_jogador[1] == "J") or (mao_jogador[1] == "Q") or (mao_jogador[1] == "K"))) or (mao_jogador[1] == "A" and ((mao_jogador[1] == "J") or (mao_jogador[1] == "Q") or (mao_jogador[1] == "K"))):
                            print("BLACKJACK!!\nVocê ganhou!")
                            saldo += aposta
                            break
                        else:
                            if total_mesa < 13:
                                print("Mesa compra uma carta..")
                                total_mesa = compra(total_mesa, mao_mesa)
                                
                            if total_jogador > 21:
                                saldo = saldo - aposta
                                print(f"Passou de 21. Você PERDEU. \nTotal da mesa: {total_mesa} Cartas da mesa: {mao_mesa} \nSeu total: {total_jogador} Sua mão: {mao_jogador}")
                                break
                            if total_mesa > 21:
                                print(f"A mesa passou de 21, VOCÊ VENCEU!!!!!!!!\nTotal da mesa: {total_mesa} Cartas da mesa: {mao_mesa} \nSeu total: {total_jogador} Sua mão: {mao_jogador}")
                                saldo += aposta
                                break
                            if total_mesa == 21:
                                print(f"A mesa fez BLACKJACK!! você perdeu. \nTotal da mesa: {total_mesa} Cartas da mesa: {mao_mesa} \nSeu total: {total_jogador} Sua mão: {mao_jogador}")
                                saldo -= aposta
                                break
                            if total_jogador == 21:
                                print(f"21 PONTOS. Você venceu!! \nTotal da mesa: {total_mesa} Cartas da mesa: {mao_mesa} \nSeu total: {total_jogador} Sua mão: {mao_jogador}")
                                saldo += aposta
                                break
                            
                            continuar = input("\n1 - HIT  |  2 - PARAR: ")

                            if continuar in ["1", "2"]:
                                if continuar == "2":
                                    if total_jogador > total_mesa:
                                        print(f"Parabéns você venceu!!! \nTotal da mesa: {total_mesa} Cartas da mesa: {mao_mesa} \nSeu total: {total_jogador} Sua mão: {mao_jogador}")
                                        saldo += aposta
                                    elif total_jogador == total_mesa:
                                        print(f"EMPATE!! \nTotal da mesa: {total_mesa} Cartas da mesa: {mao_mesa} \nSeu total: {total_jogador} Sua mão: {mao_jogador}")
                                    elif total_mesa > total_jogador:
                                        print(f"Você PERDEU \nTotal da mesa: {total_mesa} Cartas da mesa: {mao_mesa} \nSeu total: {total_jogador} Sua mão: {mao_jogador}")
                                        saldo -= aposta
                                    break
                                if continuar == "1":
                                    total_jogador = compra(total_jogador, mao_jogador)
                                    print(f"Suas cartas são: {mao_jogador}. Total: {total_jogador}")
                            else:
                                print("\nOpção Inválida\n")
        else:
            raise opcaoinvalida           

    except opcaoinvalida:
        print("\nOpção Inválida\n")
    except:
        print(f"Saldo inválido! Seu saldo é: {saldo}")
    
if saldo <= 0: 
    print("Saldo = 0. Fim de jogo")
if saldo >= 1:
    print(f"Saldo Final: {saldo}")