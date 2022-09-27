print("Escolha qual jogo você quer jogar:")
jogo = int(input("Jogo (1) - Adivinha, (2) - Forca: "))

def adivinha():
    import adivinha


if jogo == 1:
    print("Adivinha")
    adivinha()
elif jogo == 2:
    print("Forca")
else:
    print("Erro")