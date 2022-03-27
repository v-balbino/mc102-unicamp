def ind_menor(l, ini):
	ind_menor = ini
	for i in range(ini,len(l)):
		if l[i] < l[ind_menor]:
			ind_menor = i
	return ind_menor

def selection_sort(l):
	for i in range(len(l)):
		ind_m = ind_menor(l,i)
		l[i], l[ind_m] = l[ind_m], l[i]

l = [9,-1,10,-5,6,-10,8]
selection_sort(l)
print(l)

