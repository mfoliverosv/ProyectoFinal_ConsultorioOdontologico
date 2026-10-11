# Pila de contingencia para extracciones urgentes

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

    def mostrar(self):
        return self.elementos


clientes = [
    {
        "cedula": "1001",
        "nombre": "Ana",
        "tipo_atencion": "Extracción",
        "prioridad": "Urgente",
        "fecha_cita": "2026-10-10"
    },
    {
        "cedula": "1002",
        "nombre": "Luis",
        "tipo_atencion": "Limpieza",
        "prioridad": "Urgente",
        "fecha_cita": "2026-10-08"
    },
    {
        "cedula": "1003",
        "nombre": "Carlos",
        "tipo_atencion": "Extracción",
        "prioridad": "Normal",
        "fecha_cita": "2026-10-07"
    },
    {
        "cedula": "1004",
        "nombre": "Laura",
        "tipo_atencion": "Extracción",
        "prioridad": "Urgente",
        "fecha_cita": "2026-10-06"
    },
    {
        "cedula": "1005",
        "nombre": "Sofia",
        "tipo_atencion": "Extracción",
        "prioridad": "Urgente",
        "fecha_cita": "2026-10-12"
    }
]

clientes_prioritarios = [
    cliente for cliente in clientes
    if cliente["tipo_atencion"] == "Extracción"
    and cliente["prioridad"] == "Urgente"
]

# Ordenar de la fecha más cercana a la más lejana.
clientes_prioritarios.sort(key=lambda cliente: cliente["fecha_cita"])

# Como una Pila funciona LIFO se apilan en orden inverso para que la fecha más cercana quede arriba.
pila = Pila()

for cliente in reversed(clientes_prioritarios):
    pila.apilar(cliente)

print("INFORME DE PILA DE CONTINGENCIA")
print("--------------------------------")

print("Clientes que cumplen los criterios:")
for cliente in clientes_prioritarios:
    print(
        cliente["cedula"],
        "-",
        cliente["nombre"],
        "-",
        cliente["fecha_cita"]
    )

print("\nORDEN DE ATENCIÓN DE LA PILA")
numero = 1

while not pila.esta_vacia():
    cliente = pila.desapilar()

    print(
        numero,
        ".",
        cliente["nombre"],
        "- Cédula:",
        cliente["cedula"],
        "- Fecha:",
        cliente["fecha_cita"]
    )

    numero += 1
