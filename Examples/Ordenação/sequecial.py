def buscaSequecial(lista,chave):
	for i in range(0,len(lista)-1):
		if chave == lista[i]:
			return i
	return -1
l = [20,5,15,24,67,45,1,76]
print(buscaSequecial(l,24))
print(buscaSequecial(l,100))
