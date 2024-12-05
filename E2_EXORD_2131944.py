import numpy as np
datos = [
    ((-1, 0, 0), 0),
    ((-1, 0, 1), 1),
    ((-1, 1, 0), 1),
    ((-1, 1, 1), 1)
]
pesos = np.array([1.0, 0.0, 0.0])
tasa_aprendizaje = 0.1
def activacion(entradas, pesos):
    suma_ponderada = np.dot(entradas, pesos)
    return 1 if suma_ponderada >= 0 else 0

for entradas, objetivo in datos[:2]:
    salida = activacion(entradas, pesos)
    error = objetivo - salida
    ajuste = tasa_aprendizaje * error * np.array(entradas)
    pesos += ajuste
    print(f"Entradas: {entradas}, Salida: {salida}, Error: {error}, Ajuste: {ajuste}, Pesos: {pesos}")
