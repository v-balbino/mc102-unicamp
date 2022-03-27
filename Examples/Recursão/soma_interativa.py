def somaLista(numeros):
	soma = 0
	for i in numeros:
		soma = soma + i
	return soma
lista = [1,3,5,7,9]
print(somaLista(lista))