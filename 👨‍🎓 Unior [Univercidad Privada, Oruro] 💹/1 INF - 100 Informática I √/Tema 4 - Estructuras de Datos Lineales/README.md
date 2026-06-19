# Tema 4: Estructuras de Datos Lineales
## 🏫 Materia: Informática I (INF-100)

---

### 📚 Apuntes y Conceptos Clave
##### 4.1 Arreglos (Arrays)

| Tipo | Descripción | Declaración (ejemplo en C) |
|---|---|---|
| **Unidimensional** | Lista lineal de elementos del mismo tipo | `int notas[5];` |
| **Bidimensional (Matriz)** | Tabla organizada en filas y columnas | `int matriz[3][3];` |

**Características de los arreglos:**
- Tamaño fijo, definido al momento de declararlos (en lenguajes como C, Java).
- Acceso directo O(1) a cualquier elemento mediante su índice (que empieza en 0 en la mayoría de los lenguajes).
- Elementos almacenados de forma contigua en memoria.

```python
notas = [85, 90, 76, 88, 95]
print(notas[0])     # 85 (primer elemento)
print(notas[-1])    # 95 (último elemento, en Python)

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[1][2])  # 6 (fila 1, columna 2)
```

##### 4.2 Estructuras de Datos Dinámicas

**Pila (Stack) — LIFO (Last In, First Out):**

```python
pila = []
pila.append(1)   # push: [1]
pila.append(2)   # push: [1, 2]
pila.append(3)   # push: [1, 2, 3]
print(pila.pop()) # pop: devuelve 3 → queda [1, 2]
```
> Analogía: una pila de platos — solo puedes sacar (o agregar) el de arriba.
> Uso real: botón "Deshacer" (Ctrl+Z), pila de llamadas de funciones (call stack).

**Cola (Queue) — FIFO (First In, First Out):**

```python
from collections import deque
cola = deque()
cola.append("Cliente1")   # enqueue
cola.append("Cliente2")   # enqueue
print(cola.popleft())      # dequeue: devuelve "Cliente1"
```
> Analogía: una fila en el banco — el primero que llega es el primero en ser atendido.
> Uso real: cola de impresión, gestión de procesos del sistema operativo.

**Lista enlazada (Linked List):** cada nodo contiene un dato y un puntero/referencia al siguiente nodo.

```python
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

# Crear una lista enlazada manualmente: 1 -> 2 -> 3
nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
```

##### 4.3 Comparación: Arreglo vs. Lista Enlazada

| Característica | Arreglo | Lista Enlazada |
|---|---|---|
| Tamaño | Fijo (estático) | Dinámico, crece/decrece en tiempo de ejecución |
| Acceso a un elemento | Directo — O(1) | Secuencial — O(n) |
| Inserción/Eliminación al medio | Costosa, requiere desplazar elementos — O(n) | Eficiente, solo cambia un puntero — O(1) |
| Uso de memoria | Contigua | Dispersa (cada nodo en cualquier parte) |

---

##### 📑 Banco de Preguntas (Auto-Evaluación)
1. **¿Qué diferencia a un arreglo (array) de una lista enlazada dinámica?**
   * *Respuesta:* Un arreglo tiene un tamaño fijo definido en tiempo de compilación y elementos contiguos en memoria. Una lista enlazada tiene tamaño dinámico y sus elementos (nodos) se conectan mediante punteros en cualquier parte de la memoria.
2. **Explique la diferencia entre las estructuras Pilas (LIFO) y Colas (FIFO).**
   * *Respuesta:* Pila (LIFO - Last In First Out): el último elemento en entrar es el primero en salir. Cola (FIFO - First In First Out): el primer elemento en entrar es el primero en salir.
3. **Para acceder al elemento en la fila 2, columna 3 de una matriz bidimensional llamada `M`, la sintaxis habitual es:**
   * A) `M[2][3]`
   * B) `M[1][2]` (en indexación 0-based)
   * C) `M[3][2]`
   * D) `M(2,3)`
   * *Respuesta correcta:* B) `M[1][2]` (fila 2 es índice 1, columna 3 es índice 2).
4. **¿Qué operaciones básicas realiza una Pila?**
   * *Respuesta:* `push` (insertar un elemento en la cima) y `pop` (eliminar y retornar el elemento de la cima).

---

### ✍️ Mis Resúmenes y Notas de Clase
*Haz doble clic en este archivo para registrar tus notas, fórmulas o resúmenes de las clases del docente.*

---

### 📂 Archivos y Tareas de esta Unidad
*Arrastra tus prácticas, códigos o diapositivas a esta carpeta para organizarlas aquí.*

---
*Documento autogenerado para el control de estudios del Ing. José Luis Choquevilca - UNIOR*