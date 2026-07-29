while True:
    try:
        num = input("Digite um número inteiro maior que 0: ")
        soma = 0

        if int(num[1]) < 1:
            raise Exception
        else:
            tamanho = len(num)

            for i in range(tamanho):
                soma = soma + int(num[i])

            print(f"A soma dos algarismos é: {soma}")
            break
    except:
        print("\nTente novamente.\n")