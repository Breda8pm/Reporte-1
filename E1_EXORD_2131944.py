import numpy as np
distancias = np.array([
    [3, 2, 1],
    [2, 1, 0],
    [3, 2, 1]
])
inicio = (0, 0)
meta = (1, 2)
def obt_vecinos(posicion):
    vecinos = []
    x, y = posicion
    if x > 0:
        vecinos.append((x-1, y))
    if x < 2:
        vecinos.append((x+1, y))
    if y > 0:
        vecinos.append((x, y-1))
    if y < 2:
        vecinos.append((x, y+1))
    return vecinos

def bus_avariciosa(inicio, meta):
    pos_actual = inicio
    ruta = [pos_actual]
    while pos_actual != meta:
        vecinos = obt_vecinos(pos_actual)
        sig_posicion = min(vecinos, key=lambda pos: distancias[pos[0], pos[1]])
        ruta.append(sig_posicion)
        pos_actual = sig_posicion
    return ruta

ruta = bus_avariciosa(inicio, meta)

print("Ruta que seguira el agente:", ruta)

