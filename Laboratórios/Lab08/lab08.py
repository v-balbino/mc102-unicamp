###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Emparelhamento de Primers
# Nome: Vinícius Garcia Balbino
# RA: 250559
###################################################


# Leitura de dados

dna = list(input())
primer = list(input())
dna_d = []
indices_lig = []


# Revertendo o primer e removendo os 5' e 3'

primer.reverse() # Revertendo a lista do código primer
# Removendo o 5' e 3' do DNA e do Primer
if '5' in primer:
	primer.remove('5') 
if '3' in primer:
	primer.remove('3')
if '5' in dna:
	dna.remove('5')
if '3' in dna:
	dna.remove('3')

# Verificação da ligação dos primers na fita

for i in range(0,len(primer)): # Encontrando o base complementar do Primer 
	if primer[i] == 'C':
		primer[i] = 'G'
	elif primer[i] == 'G':
		primer[i] = 'C'
	elif primer[i] == 'A':
		primer[i] = 'T'
	else:
		primer[i] = 'A'

for k in range(0,len(dna)-len(primer)+1): # Subdividindo o dna em código com o memso tamanho do Primer
	dna_d.append(dna[k:k+len(primer)])


# Impressão da saída do programa

if list(primer) in list(dna_d): # Encontrando pares iguais nas listas dnd_d e primer
	for m in range(len(dna_d)):
		if dna_d[m] == primer:
			indices_lig.append(m+1)
	for h in range(len(indices_lig)):
		print("Ligacao na posicao", indices_lig[h])
else:
	print("Nenhuma ligacao")
