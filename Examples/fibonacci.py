n = int(input("Digite a quantidade de números que vc quer ver na série de Fibonacci: "))

f1 = 0
f2 = 1

for i in range(n):
	print(f2)
	aux = f2
	f2 = f2 + f1
	f1 = aux
