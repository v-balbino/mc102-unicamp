###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Fuga de Nova York
# Nome: Vinícius Garcia Balbino 
# RA: 250559
###################################################

# Leitura da matriz
# DICA: o método isnumeric() pode ser útil para determinar o fim da leitura da matriz 

mapa = []
mapa_d = []
aux_mapa = input()
aux_qtd_coluna = aux_mapa.replace(" ","")
qtd_coluna = len(aux_qtd_coluna) 
qtd_linha = 1

while not aux_mapa.isnumeric():
	string = input()
	if string.isnumeric() == False:
		aux_mapa = aux_mapa + string
		qtd_linha = qtd_linha + 1
	else:
		N = int(string)
		break

mapa = list(aux_mapa)

while " " in mapa:
	mapa.remove(" ")

for d in range(0,len(mapa),qtd_coluna):
	mapa_d.append(mapa[d:d+qtd_coluna]) 

rota = []

# Leitura da(s) equipe(s) de resgate
resgate = []

for j in range(0,N):
	aux_resgate = [int(i) for i in input().split()]
	resgate.append(aux_resgate)

l = []
saida = 1

# Leitura das coordenadas e início do processamento

def analise_rota(linha,coluna):
	global qtd_linha, qtd_coluna
	rota = []
	while coluna != -1 and coluna != qtd_coluna and linha != -1 and linha != qtd_linha:
		if mapa_d[linha][coluna] == 'N' and [linha,coluna] not in rota:
			posicao = [linha,coluna]
			rota.append(posicao)
			linha = linha - 1
		elif mapa_d[linha][coluna] == 'S'and [linha,coluna] not in rota:
			posicao = [linha,coluna]
			rota.append(posicao)
			linha = linha + 1
		elif mapa_d[linha][coluna] == 'L'and [linha,coluna] not in rota:
			posicao = [linha,coluna]
			rota.append(posicao)
			coluna = coluna + 1 
		elif mapa_d[linha][coluna] == 'O'and [linha,coluna] not in rota:
			posicao = [linha,coluna]
			rota.append(posicao)
			coluna = coluna - 1 
		else:
			return [linha,coluna]
			break
	return[linha,coluna]

# Impressão do resultado para cada coordenada

for k in range(0,N):
	l = analise_rota(resgate[k][0],resgate[k][1])
	if l[0] == -1:
		print("Fuga pelo norte.")
	elif l[0] == qtd_linha:
		print("Fuga pelo sul.")
	elif l[1] == qtd_coluna:
		print("Fuga pelo leste.")
	elif l[1] == -1:
		print("Fuga pelo oeste.")
	else:
		print("Resgate aereo solicitado.")