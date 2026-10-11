# Sistema integrado de Pila y Cola

class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, cliente):
        self.elementos.append(cliente)

    def desapilar(self):
        if self.esta_vacia():
            return None
        return self.elementos.pop()

    def esta_vacia(self):
        return len(self.elementos) == 0


class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, cliente):
        self.elementos.append(cliente)

    def desencolar(self):
        if self.esta_vacia():
            return None
        return self.elementos.pop(0)

    def esta_vacia(self):
        return len(self.elementos) == 0


clientes = [
    {
        "cedula": "3001",
        "nombre": "Andrea",
        "tipo_atencion": "Extracción",
        "prioridad": "Urgente",
        "fecha_cita": "2026-10-05",
        "hora": "08:00"
    },
    {
        "cedula": "3002",
        "nombre": "Daniel",
        "tipo_atencion": "Limpieza",
        "prioridad": "Normal",
        "fecha_cita": "2026-10-05",
        "hora": "09:00"
    },
    {
        "cedula": "3003",
        "nombre": "Camila",
        "tipo_atencion": "Extracción",
        "prioridad": "Urgente",
        "fecha_cita": "2026-10-06",
        "hora": "10:00"
    },
    {
        "cedula": "3004",
        "nombre": "Jorge",
        "tipo_atencion": "Calzas",
        "prioridad": "Normal",
        "fecha_cita": "2026-10-06",
        "hora": "11:00"
    },
    {
        "cedula": "3005",
        "nombre": "Natalia",
        "tipo_atencion": "Extracción",
        "prioridad": "Urgente",
        "fecha_cita": "2026-10-08",
        "hora": "12:00"
    }
]

prioritarios = [
    cliente for cliente in clientes
    if cliente["tipo_atencion"] == "Extracción"
    and cliente["prioridad"] == "Urgente"
]

prioritarios.sort(key=lambda cliente: cliente["fecha_cita"])

pila = Pila()

# Se apilan en orden inverso para que, al desapilar, salga primero la fecha más cercana.

for cliente in reversed(prioritarios):
    pila.apilar(cliente)

print("INFORME DE PILA DE CONTINGENCIA")
print("--------------------------------")

numero = 1

while not pila.esta_vacia():
    cliente = pila.desapilar()

    print(
        numero,
        ".",
        cliente["nombre"],
        "-",
        cliente["tipo_atencion"],
        "-",
        cliente["prioridad"],
        "- Fecha:",
        cliente["fecha_cita"]
    )

    numero += 1

cola = Cola()

# La agenda se atiende en el orden establecido.
for cliente in clientes:
    cola.encolar(cliente)

print("\nAGENDA Y COLA DE ATENCIÓN")
print("-------------------------")

numero = 1

while not cola.esta_vacia():
    cliente = cola.desencolar()

    print(
        numero,
        ".",
        cliente["hora"],
        "-",
        cliente["nombre"],
        "-",
        cliente["tipo_atencion"]
    )

    numero += 1

print("\nProceso terminado.")
