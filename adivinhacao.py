import random

print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = round(random.randrange(1, 11))
total_tentativas = 0
rodada = 1

print("Qual nível de dificuldade?")
print("1-Fácil 2-Médio 3-Difícil")
nivel = int(input("Escolha o nível: "))

if(nivel==1):
    total_tentativas = 5
elif(nivel==2):
    total_tentativas = 3
else:
    total_tentativas = 1


for rodada in range(1, total_tentativas+1):

    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute_str = input("Digite um número entre 1 e 10: ")
    chute = int(chute_str)

    if(chute <1 or chute >10):
        print("Você deve digitar um número entre 1 e 10")
        continue

    print("Você digitou " , chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou! Parabéns!!")
        break

    else:
        if(maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor que o número secreto.")


print(f"O número secreto era: *{numero_secreto}*")
print("Fim de jogo.")

