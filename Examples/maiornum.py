n = int(input("Digite o valor de n: "))
maior = int(input())

for i in range(n-1):
	aux = int(input())
	if aux > maior:
		maior = aux
print("Maior número é", maior)