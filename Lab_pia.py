class Prisionero:
    def __init__(self, nombre):
        self.nombre = nombre
        self.utilidad = 0
        self.decision = None

    def accion(self, decision_ajena):
        """
                Evalúa la mejor decisión basándose en la decisión del otro prisionero.
                """
        decisiones = {
            ("Confesar", "Confesar"): (-2, -2),
            ("Confesar", "Mentir"): (0, -3),
            ("Mentir", "Confesar"): (-3, 0),
            ("Mentir", "Mentir"): (-1, -1)
        }

        confesar_utilidad = decisiones[("Confesar", decision_ajena)][0]
        mentir_utilidad = decisiones[("Mentir", decision_ajena)][0]

        if confesar_utilidad > mentir_utilidad:
            self.decision = "Confesar"
            self.utilidad = confesar_utilidad
        else:
            self.decision = "Mentir"
            self.utilidad = mentir_utilidad

def simulacion_dilema():
    prisionero1 = Prisionero("Prisionero 1")
    prisionero2 = Prisionero("Prisionero 2")

    decision_prisionero2 = "Confesar"
    prisionero1.accion(decision_prisionero2)

    prisionero2.accion(prisionero1.decision)

    print(f"{prisionero1.nombre} decidió: {prisionero1.decision} (Utilidad: {prisionero1.utilidad})")
    print(f"{prisionero2.nombre} decidió: {prisionero2.decision} (Utilidad: {prisionero2.utilidad})")

    if prisionero1.decision == "Confesar" and prisionero2.decision == "Confesar":
        print("Ambos confiesan: 2 años de prisión cada uno.")
    elif prisionero1.decision == "Confesar" and prisionero2.decision == "Mentir":
        print("Prisionero 1 queda libre, Prisionero 2: 3 años de prisión.")
    elif prisionero1.decision == "Mentir" and prisionero2.decision == "Confesar":
        print("Prisionero 2 queda libre, Prisionero 1: 3 años de prisión.")
    else:
        print("Ambos mienten: 1 año de prisión cada uno.")

simulacion_dilema()
