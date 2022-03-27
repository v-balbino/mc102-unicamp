n = int(input("Quantos números você vai digitar: "))
ant = int(input("Digite um número: "))
i=0
em_ordem = True

while i < n-1:
	atual = int(input("Digite um número: "))
	if ant >=atual:
		em_ordem = False
	ant = atual
	i = i + 1
if em_ordem:
	print("Sequência em ordem")
else:
	print("Sequência fora de ordem")
	
