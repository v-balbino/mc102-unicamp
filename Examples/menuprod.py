import os

while True:
	print("1 - Cadastrar um produto.")
	print("2 - Buscar informações de produto.")
	print("3 - Remover um produto´.")
	print("4 - Sair do Programa.")
	escolha = int(input("Digite uma opção 1-4: "))
	if escolha == 1:
		os.system('cls' if os.name == 'nt' else 'clear')
		print("Cadastrando um produto...")
	elif escolha == 2:
		os.system('cls' if os.name == 'nt' else 'clear')
		print("Buscando informações...")
	elif escolha == 3:
		os.system('cls' if os.name == 'nt' else 'clear')
		print("Removendo um produto")
	elif escolha == 4:
		break
	else:
		os.system('cls' if os.name == 'nt' else 'clear')
		print("Opção inválida.")