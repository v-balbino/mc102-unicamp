print("1- Parmegiana")
print("2- Picanha")
print("3- Frango Grelhado")
print("4- Escondidinho de Batata")
print("5- Sair")
print("")
n = int(input("Digite um número para escolher seu prato: "))

while n != 5:
	if n == 1:
		print("Parmegiana")
	elif n == 2:
		print("Picanha")
	elif n == 3:
		print("Frango Grelhado")
	elif n == 4:
		print("Escondidinho de Batata")
	else:
		print("Esse prato não está em nosso cardápio")
	n = int(input("Deseja escolher outro prato? Digite um número: "))
print("Você saiu")