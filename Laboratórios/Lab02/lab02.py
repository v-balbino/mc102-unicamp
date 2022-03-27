###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Fórmula 1
# Nome: Vinícius Garcia Balbino
# RA: 250559
###################################################

# Leitura de dados
t = float(input())
dist_a = int(input())
vel_a = float(input())
t_pit_stop = float(input())
dist_b = int(input())
vel_b = float(input())

# Cálculo do tempo total gasto para realizar o pit stop
t_carro_pit = (dist_a/(vel_a/3.6)) + (dist_b/(vel_b/3.6)) + t_pit_stop


# Impressão da resposta
if t >= t_carro_pit:
	print("True")
else:
	print("False")