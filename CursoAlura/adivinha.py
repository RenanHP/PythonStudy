import random

tentativas = int
nivel = 0
numero_secreto = random.randrange(1, 101) 
pontos = 1000

nivel = int(input("Digite em qual nível deseja jogar: (1) Difícil - 5 tentativas, (2) Médio - 10 tentativas, (3) Fácil - 20 tentativas: "))

if nivel == 1:
    tentativas = 5
elif nivel == 2:
    tentativas = 10
elif nivel == 3:
    tentativas = 20
    
for i in range(tentativas):
    
    print("tentativas: {} de {}".format(i+1, tentativas))
    
    chute = int(input("Digite o num entre 1 e 100: "))
    
    if chute <= 0 or chute > 100 :
        chute = int(input("Erro! Digite um número entre 1 e 100: "))
        continue
    else:
        if (chute == numero_secreto):
            print("Acertou")
            break
        else:
            if (chute > numero_secreto):
                print("Seu chute foi maior que o número")
                if nivel == 1:
                    pontos -= 200
        
                elif nivel == 2:
                    pontos -= 100
        
                elif nivel == 3:
                    pontos -= 50
            else:
                print("Seu chute foi menor que o número")
                if nivel == 1:
                    pontos -= 200
        
                elif nivel == 2:
                    pontos -= 100
        
                elif nivel == 3:
                    pontos -= 50
                
print("O número secreto é: {}".format(numero_secreto))
print("Você fez {} pontos".format(pontos))
print("Fim")
    


