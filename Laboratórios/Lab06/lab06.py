###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - O Porteiro do Castelo
# Nome: Vinícius Garcia Balbino
# RA: 250559
###################################################

# Declaração de variáveis

ordem_crescente = False 

# Leitura de dados

sequencia = [int(i) for i in input().split()]
a = sequencia[0]


# Rotação Circular

for n in range(0,len(sequencia)):
	if ordem_crescente == True:
		break
	for i in range(0,len(sequencia)):
		if i == len(sequencia)-1:
			sequencia[len(sequencia)-1] = a
		else:
			sequencia[i] = sequencia[i+1]
		for k in range(1,len(sequencia)): # Verifica se a senha possui alguma possibilidade de estar em ordem crescente uma rotação circular 
			if (sequencia[k-1]>sequencia[k]):
				ordem_crescente = False
				break
			else:
				ordem_crescente = True
		if ordem_crescente == True:
			break	
	a = sequencia[0]

	

# Impressão da saída

if ordem_crescente == True:
	print("Klift, Kloft, Still, a porta se abriu")
else:
	print("Senha incorreta")