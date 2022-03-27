#impreimir todos os jogos da Mega-Sena considerenado que os números devem ser distintos e os jogos não podem ser repetidos
for n1 in range(1,61):
	for n2 in range(n1+1,61):
		for n3 in range (n2+1,61):
			for n4 in range(n3+1,61):
				for n5 in range(n4+1,61):
					for n6 in range(n5+1,61):
						print(n1,n2,n3,n4,n5,n6)