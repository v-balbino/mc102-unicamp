###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Cartões de Crédito
# Nome: Vinícius Garcia Balbino
# RA:250559
###################################################

# Leitura de dados
score = int(input())
idade = int(input())
saldo = float(input())
salario = float(input())

# Verificação se o cartão de crédito será concedido ou não
if score < 300:
	print("Cartao nao concedido")
elif (score>= 300 and score<600):
	if idade < 30:
		print("Cartao nao concedido")
	else:
		if salario < 3000:
			print("Cartao nao concedido")
		else:
			if saldo < 7000:
				print("Cartao nao concedido")
			else:
				print("Cartao concedido")
else:
	if idade >= 50:
		print("Cartao concedido")
	else:
		if salario>=2000:
			print("Cartao concedido")
		else:
			if saldo<5000:
				print("Cartao nao concedido")
			else:
				print("Cartao concedido")
		