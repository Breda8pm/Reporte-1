pos_jugador = (0, 0)
pos_porteria = (3, 1)
pos_delanteros = {'D1': (2, 1), 'D2': (1, 3)}
pos_defensas = [(0, 3), (2, 2)]

def distancia_manhattan(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def contar_defensas(pos_delantero, pos_defensas):
    pos_adyacentes = [(pos_delantero[0] + i, pos_delantero[1] + j)
                             for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0)]
    return sum(1 for pos in pos_adyacentes if pos in pos_defensas)

sumas = {}
for delantero, pos in pos_delanteros.items():
    distancia_jugador = distancia_manhattan(pos_jugador, pos)
    distancia_porteria = distancia_manhattan(pos, pos_porteria)
    defensas_adyacentes = contar_defensas(pos, pos_defensas)
    sumas[delantero] = distancia_jugador + distancia_porteria + defensas_adyacentes

delantero_sel = min(sumas, key=sumas.get)

print("Sumas calculadas para cada delantero:", sumas)
print("Delantero seleccionado para llevar a cabo la tarea:", delantero_sel)
