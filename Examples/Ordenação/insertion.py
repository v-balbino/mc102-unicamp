def insertionSort(lista):
	for i in range(1,len(lista)):
		aux = lista[i]
		j = i-1
		while (j>=0 and lista[j]>aux):
			lista[j+1] = lista[j]
			j = j-1
		lista[j+1] = aux

l = [4,2,5,4,8,6]
insertionSort(l)
print(l)