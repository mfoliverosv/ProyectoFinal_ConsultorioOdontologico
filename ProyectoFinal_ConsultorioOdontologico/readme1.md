# Programa 1: Pila de contingencia

## Objetivo
Crear una Pila de clientes que solamente incluya personas que cumplan dos condiciones:

1. La atención sea una extracción dental.
2. La prioridad sea Urgente.

Los clientes se organizan desde la fecha más cercana hasta la más lejana.

## Estructura utilizada
Se utiliza una Pila, que trabaja con el principio LIFO:

**Last In, First Out**

Para cumplir con el requisito de atender primero la fecha más cercana, los clientes se ordenan por fecha y después se apilan en orden inverso.

## ¿Qué hace el programa?
- Guarda clientes de ejemplo.
- Filtra los casos de Extracción y Urgente.
- Ordena esos clientes por fecha.
- Los introduce en una Pila.
- Retira los clientes de la Pila y genera un informe de atención.


# Programa 2: Cola de atención diaria

## Objetivo
Implementar una Cola para atender diariamente a los clientes del consultorio en el estricto orden definido por la agenda.

## Estructura utilizada
Se utiliza una Cola, que trabaja con el principio FIFO:

**First In, First Out**

## ¿Qué hace el programa?
- Crea una agenda diaria.
- Agrega los clientes a la Cola respetando el orden de la agenda.
- Muestra la agenda.
- Desencola cada cliente.
- Muestra el orden en que serán atendidos.


# Programa 3: sistema integrado de Pila y Cola

## Objetivo
Integrar las dos estructuras solicitadas en la actividad:

- Pila para el plan de contingencia.
- Cola para la atención diaria.

## Pila
La Pila solamente recibe clientes que:
- Tienen una atención de Extracción.
- Tienen prioridad Urgente.

Los clientes se ordenan por fecha de la más cercana a la más lejana.

## Cola
La Cola recibe a todos los clientes de la agenda y los atiende en el mismo orden establecido.

## Conceptos utilizados
- Clases.
- Pila.
- Cola.
- Listas.
- Diccionarios.
- Condicionales.
- Ciclos.
- Ordenamiento.
- Filtrado de datos.
