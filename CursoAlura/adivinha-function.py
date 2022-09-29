import json

def LoadData ():
    with open('bet.json') as f:
        return json.load(f)

def VerifyUser(nome, data):
    match = next((x for x in data if x["name"] == nome), None)
    if match == None:
        data.append({"name":nome, "saldo":1000}) 

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

data = LoadData()
VerifyUser("João", data)
UpdateSaldo("João", 16000, data)
saldo = GetSaldo("João", data)
print(saldo)
SaveData(data)
