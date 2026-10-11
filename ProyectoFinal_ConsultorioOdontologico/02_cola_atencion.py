# Cola de atención diaria

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

    def mostrar(self):
        return self.elementos


# Agenda diaria.

agenda = [
    {
        "cedula": "2001",
        "nombre": "Maria",
        "tipo_atencion": "Limpieza",
        "prioridad": "Normal",
        "hora": "08:00"
    },
    {
        "cedula": "2002",
        "nombre": "Pedro",
        "tipo_atencion": "Extracción",
        "prioridad": "Normal",
        "hora": "09:00"
    },
    {
        "cedula": "2003",
        "nombre": "Valentina",
        "tipo_atencion": "Diagnóstico",
        "prioridad": "Urgente",
        "hora": "10:00"
    },
    {
        "cedula": "2004",
        "nombre": "Juan",
        "tipo_atencion": "Calzas",
        "prioridad": "Normal",
        "hora": "11:00"
    }
]

cola = Cola()

# Los clientes llegan y se agregan a la Cola

for cliente in agenda:
    cola.encolar(cliente)

print("AGENDA DEL CONSULTORIO")
print("----------------------")

for cliente in cola.mostrar():
    print(
        cliente["hora"],
        "-",
        cliente["nombre"],
        "-",
        cliente["tipo_atencion"]
    )

print("\nATENCIÓN DE LOS CLIENTES")
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
