def indiceMenor(lista, inicio):
	menor = inicio
	for j in range(inicio, len(lista)):
		if lista[menor]>lista[j]:
			menor = j
	return menor

def selectionSort(lista):
	for i in range(len(lista)-1):
		menor = indiceMenor(lista,i)
		lista[i], lista[menor] = lista[menor],lista[i]
	return lista

l = [3,2,1]
selectionSort(l)
print(l)