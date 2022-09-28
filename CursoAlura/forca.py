import random

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")    

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

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

# Quantidade de caracteres da palavra secreta
letras_acertadas = ["_" for letra in palavra_secreta]

print("Bem vindo ao jogo da forca.")
print(letras_acertadas)

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
            imprime_mensagem_vencedor()
            break
    # Condição para temrmino do jogo
    else:
        erros += 1
        desenha_forca(erros)
        if erros == 7:
            imprime_mensagem_perdedor(palavra_secreta)
            break
        
        
