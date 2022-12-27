def jogar():
    print("**********************************")
    print("Bem vindo ao jogo de Forca!")
    print("**********************************")

    palavra_secreta = "windows".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    letras_faltando = str(letras_acertadas.count('_'))
    print('Ainda faltam acertar {} letras'.format(letras_faltando))

    enforcou = False
    acertou = False
    tentativas = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):

        chute = input("Qual a letra ? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index += 1
        else:
            tentativas += 1

        enforcou = tentativas == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        print("jogando ...")

    if (acertou):
        print("Acertou miseravil")
    else:
        print("EEEEERRRRRRRRoooooooouuuuuuuu")
    print("Game Over!!!")


if (__name__ == "__main__"):
    jogar()
