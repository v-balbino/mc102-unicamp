n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
n3 = float(input("Digite outro número: "))

if ((n1>n2) and (n1>n3)):
	print("O número %.2f é o maior número" %(n1))
else:
	if ((n2>n1) and (n2>n3)):
		print("O número %.2f é o maior número" %(n2))
	else:
		print("O némro %.2f é o maior número" %(n3))		