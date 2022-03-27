#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Linha do Tempo Sagrada
# Nome: Vinícius Garcia Balbino
# RA: 250559
#####################################################

# Leitura da matriz
matriz = []
matriz_inferior = [[0] * 50 for o in range(5)]
matriz_superior= [[0] * 50 for q in range(5)]
ramos = []
indices = []
l = []
instavel_s = []
instavel_i = []
instavel = []
instavel_org = []
nexus = []
coluna_inicial_s = []
coluna_inicial_i = []
for j in range(11):
    matriz.append(list(input()))

for i in range(0,5):
    for k in range(0,50):
        matriz_superior[i][k] = matriz[i][k]

for t in range(6,11):
    for f in range(0,50):
        matriz_inferior[t-6][f] = matriz[t][f]

for b in range(1,49):        
    if matriz_superior[4][b] == '+':
        ramos.append(b)
    if matriz_inferior[0][b] == '+':
        ramos.append(b)


# Deteção dos eventos nexus para a parte superior da linha do tempo
    
for y in range(1,49):
    coluna = y
    linha = 4
    e_nexus = True
    while not linha == 0 or coluna == 0 or coluna == 49:
        if matriz_superior[linha][coluna] == '+':
            coluna_inicial_s.append(coluna)
            if matriz_superior[linha][coluna+1] == '+' and [linha,coluna+1] not in indices :
                l = [linha,coluna+1]
                indices.append(l)
                coluna = coluna +1
            elif matriz_superior[linha][coluna-1] == '+' and [linha,coluna-1] not in indices:
                l = [linha,coluna-1]
                indices.append(l)
                coluna = coluna -1
            elif matriz_superior[linha-1][coluna] == '+' and [linha - 1,coluna] not in indices:
                l = [linha - 1,coluna]
                indices.append(l)
                linha = linha - 1
            else:
                instavel_s.append(coluna_inicial_s[0])
                e_nexus = False
                linha = 0
        else:
            break          


# Deteção dos eventos nexus para a parte inferior da linha do tempo
indices = []
for m in range(1,49):
    coluna = m
    linha = 0
    e_nexus = True
    while not linha == 4 or coluna == 0 or coluna == 49:
        if matriz_inferior[linha][coluna] == '+':
            coluna_inicial_i.append(coluna)
            if matriz_inferior[linha][coluna+1] == '+' and [linha,coluna+1] not in indices :
                l = [linha,coluna+1]
                indices.append(l)
                coluna = coluna +1
            elif matriz_inferior[linha][coluna-1] == '+' and [linha,coluna-1] not in indices:
                l = [linha,coluna-1]
                indices.append(l)
                coluna = coluna -1
            elif matriz_inferior[linha+1][coluna] == '+' and [linha + 1,coluna] not in indices:
                l = [linha + 1,coluna]
                indices.append(l)
                linha = linha + 1
            else:
                instavel_i.append(coluna_inicial_i[0])
                e_nexus = False
                linha = 4
        else:
            break    

ramos_org = sorted(list(set(ramos)))

nexus = sorted(list(set(ramos)))

for c in range(len(instavel_s)):
    if instavel_s[c] in nexus:
        nexus.remove(instavel_s[c])
for d in range(len(instavel_i)):
    if instavel_i[d] in nexus:
        nexus.remove(instavel_i[d])
instavel = instavel_i + instavel_s
instavel_org = sorted(instavel)
# Impressão da resposta   
print(instavel_i)
print(instavel_s)
print(nexus)

for z in range (len(ramos_org)):
    if ramos_org[z] in instavel_org:
        print("Bifurcacao {ramos}: Instavel".format(ramos = ramos_org[z]))
    if ramos_org[z] in nexus:
        print("Bifurcacao {ramos}: Evento Nexus".format(ramos = ramos_org[z]))       



