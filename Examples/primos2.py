n = int(input("Digite um número: "))
num_divisores = 0

for div in range (2,n):
	if n%div == 0 :
		num_divisores = num_divisores + 1
		break
if num_divisores == 0:
	print("PRIMO!")
else:
	print("NÃO É PRIMO")