import random

#########Vars########### 
Enforcado = False
Acertou = False
palavra_secreta = ""
letras_acertadas = []
erros = 0
######################## 

# Ler arquivo txt
with open('frutas.txt') as f:
    linhas = f.readlines()

qtidade_palavras = len(linhas)
palavra_secreta = linhas[random.randrange(0, qtidade_palavras)].strip().upper()
print(palavra_secreta)

# Quantidade de caracteres da palavra secreta
qtidade_caracteres = int(len(palavra_secreta))
for i in range(qtidade_caracteres) :
    letras_acertadas.append("_")

print(letras_acertadas)
print("Bem vindo ao jogo da forca.")

while (not Enforcado and not Acertou) :
    Index = 0
    chute = input("Digite uma letra: ").upper()
    
    if chute in palavra_secreta:
        chute = chute.upper().strip()
        # Verificando se a letra já foi encontrada
        if chute in letras_acertadas:
                print("Essa letra já foi econtrada.")
                
        # Validando chute
        for letra in palavra_secreta:
            if chute == letra:
                letras_acertadas[Index] = letra
            Index = Index + 1      
        print(letras_acertadas)
        
        # Validando se faltam letras a serem descobertas
        if "_" in letras_acertadas:
            continue
        else:
            print("Você ganhou!")
            break
    # Condição para temrmino do jogo
    else:
        erros += 1
        print("Você errou! Faltam {} chances.".format(6 - erros))
        if erros == 6:
            print("Você perdeu.")
            break
            
        