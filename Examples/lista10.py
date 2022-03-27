a = []
for i in range(10):
	b = int(input())
	a.append(b)
print(a)

print("O maior número é ",max(a), "e sua primeira ocorrência está na posição ",a.index(max(a)) )