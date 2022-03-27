###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Ordenação de Panquecas
# Nome: Vinícius Garcia Balbino
# RA: 250559
###################################################

# Dada uma sequência de números de inteiros, gera
# uma string representando a pilha de panquecas
def str_panquecas(lista):
  return(" ".join(map(str, lista)))

def indiceMaior(lista, fim):
  maior = fim-1
  for j in range(0, fim-1):
    if int(lista[maior]) < int(lista[j]):
      maior = j
  return maior

def reverter(lista,fim):
  l = lista[0:fim]
  l.reverse()
  return l

def ordenacao(lista):
  lista_ord = sorted(lista, key=int)
  for i in range(0,len(lista)-1):
    if lista != lista_ord:
      ind = indiceMaior(lista,len(lista)-i)
      if ind != len(lista)-1-i and ind != int(lista[ind])-1:
        print("Posicionando a panqueca", lista[ind])
        if ind != 0:
          l = reverter(lista,ind+1)
          for y in range(0,len(l)):
            lista[y] = l[y]
          print("Primeira inversao:", str_panquecas(lista))
        l = reverter(lista,len(lista)-i)
        for y in range(0,len(l)):
          lista[y] = l[y]
        print("Segunda inversao:", str_panquecas(lista))
    else:
      if i == 0:
        return print("Panquecas ja ordenadas")
      else:
        return 0
  return 0

sequencia = input().split()
ordenacao(sequencia)
