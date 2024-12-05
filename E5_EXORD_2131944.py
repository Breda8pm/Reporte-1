val_int = {
    'a1': 40,
    'a2': 60,
    'a3': 50,
    'a4': 55
}

ofertas = val_int.copy()

ganador = max(ofertas, key=ofertas.get)
precio_pagar = sorted(ofertas.values(), reverse=True)[1]

print(f"Ofertas de cada agente: {ofertas}")
print(f"Agente ganador: {ganador}")
print(f"Precio que pagara el agente ganador: ${precio_pagar}")
