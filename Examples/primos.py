n = int(input("Digite um número: "))

div=2
eprimo = True
while div <=(n-1):
	if n%div == 0:
		eprimo=False
		break
	div = div + 1
if eprimo:
	print("Esse número é primo")
else:
	print("Esse número não é primo")