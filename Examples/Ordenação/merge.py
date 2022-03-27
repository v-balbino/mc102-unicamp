'''
def merge(lista1, lista2):
	i = 0
	j = 0
	lista3 = []
	while i < len(lista1) and j < len(lista2):
		if lista1[i] <= lista2[j]:
			lista3.append(lista1[i])
			i = i + 1
		else:
			lista3.append(lista2[j])
			j = j + 1
	while i < len(lista1):
		lista3.append(lista1[i])
		i = i + 1
	while j < len(lista2):
		lista3.append(lista2[j])
		j = j + 1
	return lista3

lista1 = [1,3,4]
lista2 = [2,7,9]
print(merge(lista1,lista2))
'''

def merge(lista1,lista2):
	i = 0
	j = 0
	lista3 = []
	while i < len(lista1) and j < len(lista2):
		if lista1[i] <= lista2[j]:
			lista3.append(lista1[i])
			i = i + 1
		else:
			lista3.append(lista2[j])
			j = j + 1
	lista3 = lista3 + lista1[i:]
	lista3 = lista3 + lista2[j:]

	return lista3


def mergeSort(lista,inicio,fim):
	if fim - inicio > 1:
		meio = (inicio + fim)//2
		mergeSort(lista,inicio,meio)
		mergeSort(lista,meio,fim)

		lista1 = lista[inicio:meio]
		lista2 = lista[meio:fim]

		lista[inicio:fim] = merge(lista1,lista2)

lista = [4,5,1,0,7,6,3,2]
mergeSort(lista,0,len(lista))
print(lista)