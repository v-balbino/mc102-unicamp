n = int(input("Digite um número para calcular o fatorial do mesmo: "))
fat = 1
for i in range(1, n+1):
	fat = fat * i
print("O fatorial desse número é:",fat)