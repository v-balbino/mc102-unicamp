import math
print("Opções: q = quadrado")
print("        r = retângulo")
print("        c = círculo")
print("")
op = input("Digite uma das opções para calcular a área (q, r ou c): ")

if op == 'q':
	#ler o lado do quadrado e computar a area
	l = float(input("Digite o lado do quadrado: "))
	print("A area do quadrado é:",l*l)
elif op == 'r':
	#ler os 2 lados do retângulo e computar a área
	l1 = float(input("Digite o lado 1 do retângulo: "))
	l2 = float(input("Digite o lado 2 do retângulo: "))
	print("A area do quadrado é:", l1*l2)
elif op == 'c':
	#ler o raio do circulo
	r = float(input("Digite o raio do círculo:"))
	print("A area do circulo é:", math.pi*r*r)
else:
	print("Opção inválida")