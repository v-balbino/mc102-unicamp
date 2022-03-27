#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Jogos Olímpicos
# Nome: Vinícius Garcia Balbino
# RA: 250559
#####################################################

# Leitura da primeira linha
N, O, P, B = [int(x) for x in input().split()]
p_ouro = []
p_prata = []
p_bronze = []
modalidade = []
paises = []
paises_c = []
l = []
dados = []
resultado = []
soma = 0
soma_resultado = []
r_vencedor = []


# Leitura e processamento das provas
for i in range(0,N):
	mod, ouro, pra, bro = [str(y) for y in input().split()]
	l = [mod,ouro,pra,bro]
	paises.append(ouro)
	paises.append(pra)
	paises.append(bro)
	modalidade.append(mod)
	p_ouro.append(ouro)
	p_prata.append(pra)
	p_bronze.append(bro)
	dados.append(l)

for j in range(len(paises)): # Criando uma lista ordenada e retirando os países repetidos 
	if (paises[j] in paises) and paises[j] not in paises_c:
		paises_c.append(paises[j])
paises_c.sort()

k = 0
while (k<len(paises_c)):
	if paises_c[k] in p_ouro:
		r = p_ouro.count(paises_c[k]) * O
		resultado.append(r)
	else:
		resultado.append(0)
	if paises_c[k] in p_prata:
		r = p_prata.count(paises_c[k]) * P
		resultado.append(r)
	else:
		resultado.append(0)
	if paises_c[k] in p_bronze:
		r = p_bronze.count(paises_c[k]) * B
		resultado.append(r)
	else:
		resultado.append(0)
	k = k + 1

for e in range(0,len(resultado),3):
	soma = resultado[e]+resultado[e+1]+resultado[e+2]
	soma_resultado.append(soma)

# Impressão da saída

maior = soma_resultado.index(max(soma_resultado))
r_vencedor.append(maior)

for t in range(0,len(soma_resultado)-1):
	if soma_resultado[t] == max(soma_resultado) and t != maior:
		r_vencedor.append(t)

for g in range(0,len(r_vencedor)):
	print(paises_c[int(r_vencedor[g])], end=' ')
	print(soma_resultado[int(r_vencedor[g])])
	for w in range(0,len(p_ouro)):
		if p_ouro[w] == paises_c[int(r_vencedor[g])]:
			print(modalidade[w])