a=int(input("Digite um numero: "))

if a%2 == 0:
	#a é um número par
	if a <100:
		print("Numero par e menor que 100")
	else:
		print("Numero par e maior ou igual a 100")
else:
	#a é um número ímpar
	if a<100:
		print("Numero impar e menor que 100")
	else:
		print("Numero impar e maior ou igual a 100")
