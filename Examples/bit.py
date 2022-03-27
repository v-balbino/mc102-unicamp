n = int(input("Digite um número binário para converter: "))
pot = 1 
decimal = 0 #a cada interação i, tem a soma b_0*2^1 + ... + b_i-1 * 2^(i-1) + b_i * 2^i

while n > 0:
	dig = n%10 #obtém o digito menos significativo de n
	decimal = decimal + dig*pot
	n = n // 10 #remove este digito
	pot = 2 * pot
print(decimal) #número convertido