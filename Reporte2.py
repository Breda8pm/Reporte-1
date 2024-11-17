import networkx as nx
import matplotlib.pyplot as plt

def crear_red_erdos_renyi(n, p):
    return nx.erdos_renyi_graph(n, p)

def crear_red_watts_strogatz(n, k, p):
    return nx.watts_strogatz_graph(n, k, p)

def crear_red_barabasi_albert(n, m):
    return nx.barabasi_albert_graph(n, m)

def analizar_red(G):
    print("Numero de nodos:", G.number_of_nodes())
    print("Numero de enlaces:", G.number_of_edges())
    print("Coeficiente de clustering promedio:", nx.average_clustering(G))
    print("Grado promedio:", sum(dict(G.degree()).values()) / G.number_of_nodes())
    print("-" * 40)

n = 20

p = 0.2
print("Red aleatoria (Erdos-Renyi):")
G_erdos = crear_red_erdos_renyi(n, p)
analizar_red(G_erdos)
plt.figure()
nx.draw(G_erdos, with_labels=True)
plt.title("Red aleatoria (Erdos-Renyi)")
plt.show()

k = 4
p_ws = 0.3
print("Red de mundo pequeño (Watts-Strogatz):")
G_watts = crear_red_watts_strogatz(n, k, p_ws)
analizar_red(G_watts)
plt.figure()
nx.draw(G_watts, with_labels=True)
plt.title("Red de mundo pequeño (Watts-Strogatz)")
plt.show()


m = 2  
print("Red de Preferencia Preferencial (Barabási-Albert):")
G_barabasi = crear_red_barabasi_albert(n, m)
analizar_red(G_barabasi)
plt.figure()
nx.draw(G_barabasi, with_labels=True)
plt.title("Red de Preferencia Preferencial (Barabási-Albert)")
plt.show()
