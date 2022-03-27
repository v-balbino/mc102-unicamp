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
    

# Leitura da imagem A

P2_A = input() #P2 - linha a ser ignorada
m_A, n_A = [int(x) for x in input().split()]
pixelmax_A = input() #255 - linha a ser ignorada

A = []
A_d = []
for i in range(n_A):
    linha = [int(x) for x in input().split()]
    A.append(linha)

# Leitura da imagem B

P2_B = input() #P2 - linha a ser ignorada
m_B, n_B = [int(x) for x in input().split()]
pixelmax_B = input() #255 - linha a ser ignorada

B = []
for i in range(n_B):
    linha = [int(x) for x in input().split()]
    B.append(linha)

# Verificando se a imagem B original está contida em A


original_continuo = False
for r in range(0,n_A-len(B)+1):
    if original_continuo == True:
        break
    for s in range(0,m_A-len(B[0])+1):
        if original_continuo == True:
            break
        for x in range(0,len(B)):
            for y in range(0,len(B[0])):
                if A[x+r][y+s] == B[x][y]:
                    original_continuo = True
                    continue
                else:
                    original_continuo = False
                    break
            if original_continuo != False:
                original_continuo = True 
if original_continuo == True:
    print("Original: Contido")
else:
    print("Original: Nao contido")

