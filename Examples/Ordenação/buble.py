def troca(lista,k):
	if lista[k] > lista[k+1]:
		lista[k],lista[k+1] = lista[k+1],lista[k]
l = [5,3,2]

def bubble(lista):
	for i in range(len(lista)-1,0,-1):
		for j in range(i):
			troca(lista,j)
bubble(l)
print(l)