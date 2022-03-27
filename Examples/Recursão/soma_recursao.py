def somaLista(numeros):
	if len(numeros) == 1:
		return numeros[0]
	else:
		return numeros[0] + somaLista(numeros[1:])
lista = [1,5,6,8,9]
print(somaLista(lista))