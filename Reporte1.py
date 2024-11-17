import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def costo(x):
    return (x - 3) ** 2 + 5

def generar_poblacion(tam_poblacion, lim_inferior, lim_superior):
    return np.random.uniform(lim_inferior, lim_superior, tam_poblacion)

def evaluar_poblacion(poblacion):
    return np.array([costo(individuo) for individuo in poblacion])

def seleccion(poblacion, fitness, k=3):
    seleccionados = np.random.choice(len(poblacion), k, replace=False)
    mejor = seleccionados[np.argmin(fitness[seleccionados])]
    return poblacion[mejor]

def cruce(padre1, padre2):
    alfa = np.random.rand()
    return alfa * padre1 + (1 - alfa) * padre2

def mutacion(individuo, prob_mutacion, lim_inferior, lim_superior):
    if np.random.rand() < prob_mutacion:
        individuo += np.random.uniform(-0.5, 0.5)
        individuo = max(lim_inferior, min(lim_superior, individuo))
    return individuo

def algoritmo_genetico(tam_poblacion, lim_inferior, lim_superior, generaciones, prob_mutacion):
    poblacion = generar_poblacion(tam_poblacion, lim_inferior, lim_superior)
    tabla_resultados = []

    for generacion in range(generaciones):
        fitness = evaluar_poblacion(poblacion)

        mejor_individuo = poblacion[np.argmin(fitness)]
        mejor_costo = np.min(fitness)
        tabla_resultados.append(
            {'Generación': generacion + 1, 'Parámetro óptimo': mejor_individuo, 'Costo mínimo': mejor_costo})

        nueva_poblacion = []
        for _ in range(tam_poblacion):

            padre1 = seleccion(poblacion, fitness)
            padre2 = seleccion(poblacion, fitness)
            hijo = cruce(padre1, padre2)

            hijo = mutacion(hijo, prob_mutacion, lim_inferior, lim_superior)
            nueva_poblacion.append(hijo)

        poblacion = np.array(nueva_poblacion)

    df_resultados = pd.DataFrame(tabla_resultados)
    return mejor_individuo, mejor_costo, df_resultados

tam_poblacion = 20
lim_inferior = 0
lim_superior = 10
generaciones = 30
prob_mutacion = 0.1

mejor_parametro, costo_minimo, resultados = algoritmo_genetico(tam_poblacion, lim_inferior, lim_superior, generaciones,
                                                               prob_mutacion)

print("\nParametro optimo encontrado:", mejor_parametro)
print("Valor minimo de la funcion de costo:", costo_minimo)
print("\nTabulacion de resultados:\n")
print(resultados)

resultados.to_csv('output.csv', index=False)

x = np.linspace(0, 10, 100)
y = costo(x)
plt.plot(x, y)
plt.scatter(mejor_parametro, costo(mejor_parametro), color='red', label='Parametro optimo encontrado')
plt.legend()
plt.xlabel('Parametro')
plt.ylabel('Funcion de costo')
plt.title('Algoritmo Genetico - optimizacion de parametros')
plt.show()
