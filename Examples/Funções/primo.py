#programa que computava os n primeiros números primos

def eprimo(cand):
	for div in range(2,cand//2 + 1):
		if cand % div == 0:
			return False
	return True

def n_primos(n): #devolve uma lista com os n primeiros números primos
	l=[] #lista l tem os números primos
	cand = 2
	while len(l)<n:
		if eprimo(cand):
			l.append(cand)
		cand = cand + 1
	return 1

def main():
	n = int(input('Digite o número de primos: '))
	res = n_primos(n)
	print(res)

main()