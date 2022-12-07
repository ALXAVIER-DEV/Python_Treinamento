print("**********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("**********************************")

numero_secreto = 42
total_tentativas = 3
rodada = 1
for rodada in range(1, total_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute = int(input("Digite um número entre 1 e 100: "))
    print(" Você digitou ", chute)

    if(chute < 1 or chute > 100 ):
        print("Número não permitido, você deve digitar um número inteiro entre 1 e 100 !")
        continue
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou Miseravil !!!")
        break
    else:
        if(maior):
            print("Errrrrrooooouuu o seu chute foi maior que o número secreto.")
        elif(menor):
            print("Errrrrrooooouuu o seu chute foi menor que o número secreto.")



print("Game Over!!!")