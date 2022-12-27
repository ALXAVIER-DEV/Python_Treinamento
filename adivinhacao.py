import random

def jogar():

    print("**********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("**********************************")


    numero_secreto = random.randrange(1,101)
    total_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade ?")
    print("(1 Fácil (2) Médio (3) Difícil")

    nivel = int(input("Selecione seu nível: "))
    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

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
            print("Você acertou Miseravil e fez {} pontos!!!!".format(pontos))
            break
        else:
            if(maior):
                print("Errrrrrooooouuu o seu chute foi maior que o número secreto.")
            elif(menor):
                print("Errrrrrooooouuu o seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos



    print("Game Over!!!")

if(__name__ == "__main__"):
    jogar()