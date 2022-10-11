import json
import adivinha_function
import random

Continue = True

while Continue == True:

    nome = input("Qual seu nome?: ").capitalize()
    data = adivinha_function.LoadData()
    adivinha_function.VerifyUser(nome, data)
    saldo_atual = adivinha_function.GetSaldo(nome, data)
    print("Bem vindo {}, seu saldo atual é de {}".format(nome, saldo_atual))
    aposta = adivinha_function.VerifySaldo(nome, data)
    adivinha_function.GetPremio(aposta)
    tentativas = int
    nivel = 0
    numero_secreto = random.randrange(1, 101) 
    nivel = int(input("Digite em qual nível deseja jogar:\n (1) Extremo - 1 tentativa - Prêmio = {} \n (2) Muito difícil - 3 tentativas - Prêmio = {}\n (3) Difícil - 5 tentativas - Prêmio = {}\n (4) Médio - 10 tentativas - Prêmio = {}\n (5) Fácil - 20 tentativas - Prêmio = {} : ".format(adivinha_function.PremioCase1, adivinha_function.PremioCase2, adivinha_function.PremioCase3, adivinha_function.PremioCase4, adivinha_function.PremioCase5)))

    if nivel == 1:
        tentativas = 1
    elif nivel == 2:
        tentativas = 3
    elif nivel == 3:
        tentativas = 5
    elif nivel == 4:
        tentativas = 10
    elif nivel == 5:
        tentativas = 20    
    
    Loop = 1
    while True:
        
        if Loop > tentativas:
            print("Você perdeu")
            saldo_atual = saldo_atual - aposta
            break
        
        print("tentativas: {} de {}".format(Loop, tentativas))    
        chute = int(input("Digite o num entre 1 e 100: "))
        
        if chute <= 0 or chute > 100 :
            chute = int(input("Erro! Digite um número entre 1 e 100: "))
            continue
        else:
            if (chute == numero_secreto):
                print("Acertou")
                if nivel == 1:
                    saldo_atual = saldo_atual + aposta * 100
                elif nivel == 2:
                    saldo_atual = saldo_atual + aposta * 25
                elif nivel == 3:
                    saldo_atual = saldo_atual + aposta * 2
                elif nivel == 4:
                    saldo_atual = saldo_atual + aposta * 0.05
                elif nivel == 5:
                    saldo_atual = saldo_atual + aposta * 0.02
                break
            elif (chute > numero_secreto):
                print("Seu chute foi maior que o número")
                Loop += 1
            elif (chute < numero_secreto):
                print("Seu chute foi menor que o número")
                Loop += 1
            
    print("O número secreto é: {}".format(numero_secreto))
    print("Seu saldo atual é de: {}".format(saldo_atual))
    adivinha_function.UpdateSaldo(nome, saldo_atual, data)
    adivinha_function.SaveData(data)
    print("Fim")
    YouN = input("Deseja jogar novamente? [Y/N]: ").upper() 
    if YouN == "N":
        Continue = False
    elif YouN == "Y":
        Continue = True
    elif YouN != "Y" and YouN != "N" :
        YouN = input("Erro! Digite Y ou N: ")
        if YouN == "N":
            Continue = False
        elif YouN == "Y":
            Continue = True