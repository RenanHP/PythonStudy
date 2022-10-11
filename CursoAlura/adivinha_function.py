import json

def LoadData ():
    with open('bet.json') as f:
        return json.load(f)

def VerifyUser(nome, data):
    match = next((x for x in data if x["name"] == nome), None)
    if match == None:
        data.append({"name":nome, "saldo":1000}) 
        print("Jogador adicionado, seu saldo é de 1000R$.")

def GetSaldo (nome, data):
    match = next((x for x in data if x["name"] == nome), None)
    resultado = 0
    if match != None:
        resultado = match["saldo"]
    return resultado
    
    
def UpdateSaldo(nome, saldo, data):
    match = next((x for x in data if x["name"] == nome), None)
    if match != None:
        match["saldo"] = saldo 

def SaveData(data):
    with open('bet.json', "w") as f:
        json.dump(data, f)

def VerifySaldo(nome, data):
    global aposta
    aposta = int(input("Quanto você vai apostar: "))
    match = next((x for x in data if x["name"] == nome), None)
    if aposta > match["saldo"]:
        print("Você não tem esse dinheiro.")
        VerifySaldo(nome, data)
    return aposta

def GetPremio(aposta):
    global PremioCase1
    global PremioCase2
    global PremioCase3
    global PremioCase4
    global PremioCase5

    PremioCase1 = aposta * 100
    PremioCase2 = aposta * 25
    PremioCase3 = aposta * 2
    PremioCase4 = aposta * 0.05
    PremioCase5 = aposta * 0.02
