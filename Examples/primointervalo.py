n = int(input("Quantidade de primos a ser impresso: "))
cand = 2
numero_primos_impressos = 0
while numero_primos_impressos<n:
	eprimo = True

	for div in range (2,cand//2+1):
		if cand % div == 0:
			eprimo = False
			break
	if eprimo:
		print(cand)
		numero_primos_impressos = numero_primos_impressos + 1
	cand = cand+1