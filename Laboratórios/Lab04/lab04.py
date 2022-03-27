###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Avatar
# Nome: Vinícius Garcia Balbino
# RA: 250559
###################################################

# Inicialização das variáveis
water = 0
earth = 0
fire = 0
air = 0
aux_w = 0
aux_f = 0
aux_e = 0
aux_a = 0
element = 'x'

# Leitura da sequência de treinamento
while element != 'X':
	element = input()
	if element == 'W':
		aux_w = float(input()) 
		water = water + aux_w
		if (aux_w/2)<fire:
			fire = fire - (aux_w/2) 
		else:
			fire=0
	if element == 'F':
		aux_f = float(input())
		fire = fire + aux_f 
		if (aux_f/2)<water:
			water = water - (aux_f/2)
		else:
			water=0
	if element == 'E':
		aux_e = float(input())
		earth = earth + aux_e
		if (aux_e/2)<air:
			air = air - (aux_e/2)
		else:
			air = 0
	if element == 'A':
		aux_a = float(input())
		air = air + aux_a
		if (aux_a/2)<earth:
			earth = earth - (aux_a/2)
		else:
			earth = 0




# Impressão das informações de saída

print("Pontuacao Final")
print("Agua: {:.1f}".format(water))
print("Terra: {:.1f}".format(earth))
print("Fogo: {:.1f}".format(fire))
print("Ar: {:.1f}".format(air))

if water>0 and earth>0 and air>0 and fire>0:
	print("Treinamento realizado com sucesso.")
else:
	print("Realize mais treinamentos.")