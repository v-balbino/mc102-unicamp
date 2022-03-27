def fatorial(n):
	total = 1
	k = 1
	while k <= n:
		total = total * k
		k = k+1
	return total

#print(fatorial(4))

def fatorial_r(n):
	if n == 1:
		return 1
	else:
		return n * fatorial_r(n-1)

print(fatorial_r(4))