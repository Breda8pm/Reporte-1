U = [5, 40]
V = [2, 3]

Caliente = {5: 0.2, 40: 0.9}
Alto = {2: 0.5, 3: 0.9}

def implicacion_producto_mamdani(U, V, Caliente, Alto):
    implicacion = {}
    for x in U:
        for y in V:
            mu_QMP = Caliente[x] * Alto[y]
            implicacion[(x, y)] = mu_QMP
    return implicacion

resultado = implicacion_producto_mamdani(U, V, Caliente, Alto)

for (x, y), mu_QMP in resultado.items():
    print(f"μ_QMP({x}, {y}) = {mu_QMP:.2f}")
