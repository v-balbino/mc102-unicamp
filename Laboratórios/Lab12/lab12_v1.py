###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Busca em Imagens
# Nome: Vinícius Garcia Balbino
# RA: 250559 
###################################################

def flip_horizontal(imagem_original):
    for i in range(0,m_B):
        for k in range(0,m_B//2):
            imagem_original[i][m_B-1-k], imagem_original[i][k] = imagem_original[i][k],imagem_original[i][m_B-1-k]
    return imagem_original

def flip_vertical(imagem_original):
    for i in range(0,n_B//2):
            imagem_original[n_B-1-i], imagem_original[i] = imagem_original[i],imagem_original[n_B-1-i]
    return imagem_original

    

def rotacao_90(imagem_original):
    matriz_auxiliar = [[0 for j in range(len(imagem_original))] for l in range(len(imagem_original[0]))]
    for n in range(len(imagem_original)):
        for m in range(len(imagem_original[0])):
            matriz_auxiliar[m][len(imagem_original)-1-n] = imagem_original[n][m]
    return matriz_auxiliar


def rotacao_180(imagem_original):
    return rotacao_90(rotacao_90(imagem_original))
    

# leitura da imagem A
P2_A = input() #P2 - linha a ser ignorada
m_A, n_A = [int(x) for x in input().split()]
pixelmax_A = input() #255 - linha a ser ignorada

A = []
for i in range(n_A):
    linha = [int(x) for x in input().split()]
    A.append(linha)

# leitura da imagem B
P2_B = input() #P2 - linha a ser ignorada
m_B, n_B = [int(x) for x in input().split()]
pixelmax_B = input() #255 - linha a ser ignorada

B = []
for i in range(n_B):
    linha = [int(x) for x in input().split()]
    B.append(linha)

A_set = list(set(A))
print(A_set)