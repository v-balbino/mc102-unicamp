###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Vacinação AstraZeneca
# Nome: Vinícius Garcia Balbino
# RA: 250559
###################################################

# Leitura dos dados

N = int(input())
soma_D1 = 0
soma_D2 = 0
soma_X = 0
# Listas dos números de vacinados com a primeira e segunda dose em cada mês

D1 = []
D2 = []
for m in range(N):
    D2.append(0)

# Lista do número de vacinas devolvidas em cada mês

X = []
for m in range(N):
    X.append(0)

# Processamento dos dados

for j in range(N):
    vac = input()
    D1.append(vac)
for i in range (0,N):
    if i < N - 3:
        if (D2[i]==0):
            if int(D1[i])<=int(D1[i+3]):
                D2[i+3] = D1[i]
            else: 
                X[i] = str(int(D1[i]) - int(D1[i+3])) 
                D2[i+3] = D1[i+3]
                D1[i] = D1[i+3]
        else:
            D1[i] = int(D1[i]) - int(D2[i])
            if int(D1[i])<=int(D1[i+3]):
                D2[i+3] = D1[i]
                D1[i-3] = 0
            else: 
                X[i] = str(int(D1[i]) - int(D1[i+3])) 
                D2[i+3] = D1[i+3]
                D1[i] = D1[i+3]
                D1[i-3] = 0
    elif int(D2[i]) != 0:
            D1[i] = str(int(D1[i]) - int(D2[i]))
            D1[i-3] = 0

    # Impressão do uso das vacinas mês a mês

    print("Mes " + str(i+1) + ":")
    print("Vacinados com a primeira dose:", D1[i])
    print("Vacinados com a segunda dose:", D2[i])
    print("Vacinas devolvidas:", X[i])

# Impressão do resumo final
for h in range(N):
    soma_D1 = soma_D1 + int(D1[h])
    soma_D2 = soma_D2 + int(D2[h])
    soma_X = soma_X + int(X[h])

print("Total: ")
print("Vacinados apenas com a primeira dose:", soma_D1)
print("Vacinados com as duas doses:", soma_D2)
print("Vacinas devolvidas:", soma_X)