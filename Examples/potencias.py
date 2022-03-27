n = int(input("Digite a potência máxima para calcular: "))
i = 0
p=1
while i <= n:
	p = 2**i
	print("2^",i,"=",p)
	i = i+1
	