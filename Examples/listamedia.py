a = []
soma=0
for i in range(10):
	b = float(input())
	a.append(b)
print(a)

for i in range(10):
	soma = soma + a[i]
media = soma/10
print("A média é: ", media)