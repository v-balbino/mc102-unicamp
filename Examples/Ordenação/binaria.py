def buscaBinaria(lista,chave):
	inicio = 0
	fim = len(lista)-1
	while inicio <= fim:
		meio = (inicio + fim)//2
		if lista[meio] == chave:
			return meio
		elif lista[meio] > chave:
			fim = meio - 1
		else:
			inicio = meio +1
	return -1

l = [20,5,15,24,67,45,1,76]
l.sort()
print(l)
print(buscaBinaria(l,7))