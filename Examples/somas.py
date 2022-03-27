n = int(input("Quantos números vc quer digitar para somar? "))
i=1
soma =0
while i<=n:
	f=int(input("Digite um número para somar:"))
	i = i + 1
	soma = soma + f
print("------------------------")
print("A soma resultou em:",soma)