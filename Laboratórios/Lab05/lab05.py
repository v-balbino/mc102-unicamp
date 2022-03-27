######################################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Vacinação CoronaVac
# Nome: Vinícius Garcia Balbino
# RA: 250559
######################################################################

NV=0 #Novas Vacinas
VR=0 #Vacinas Restantes
D1 = 0
D2 = 0
D2A = 0
D1A = 0

# Leitura do número de meses

N = int(input())

# Processamento de cada mês

for i in range(N):
	NV = int(input())

	if (D1A == 0) and (D1 == 0):
		D1 = NV
	elif (D1A == 0) and (D1 > 0):
		if (NV >= D1):
			D2 = D2 + D1
			D1 = (NV - D1)
		else:
			D2 = D2 + NV
			D1A = (D1 - NV)
			D1 = D1A
	elif (D1A > 0) and (D1 == 0):
		if (NV >= D1A):
			D2 = D2 + D1A
			D2A = D2A  + D1A
			D1 = NV - D1A
			D1A = 0	
		else:
			D2 = D2 + NV
			D2A = D2A + NV
			D1A = D1A - NV
			D1 = D1A 
	elif (D1A == D1):
		if (NV >= D1A):   
			D2 = D2 + D1A   
			D2A = D2A + D1A
			VR = NV - D1A
			D1 = VR 
			D1A = 0
		else: #(NV < D1A)
			D2 = D2 + NV
			D2A = D2A + NV
			D1A = D1A - NV
			D1 = D1A

	




# Impressão da saída

print("Pessoas completamente imunizadas:", D2)
print("Pessoas imunizadas apenas com uma dose:", D1)
print("Pessoas que tomaram a segunda dose com atraso:", D2A)
print("Pessoas esperando a segunda dose com atraso:", D1A)