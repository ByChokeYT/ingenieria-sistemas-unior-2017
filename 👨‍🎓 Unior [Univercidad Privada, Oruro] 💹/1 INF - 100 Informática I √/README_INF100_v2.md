# 💻 Informática I — INF-100

## 🏫 Universidad Privada de Oruro (UNIOR)
### 💻 Carrera: Ingeniería de Sistemas

---

### 📊 Ficha Técnica de la Asignatura

| Campo | Detalle |
|---|---|
| **Sigla** | INF-100 |
| **Semestre** | 1º Semestre |
| **Prerrequisitos** | Ninguno |
| **Estado** | 🟢 Aprobada |

### 📝 Descripción de la Materia

Fundamentos de la computación, algoritmos, lógica de programación e introducción práctica al desarrollo de software, base para todas las materias de programación posteriores de la carrera (Estructura de Datos, Lenguajes de Programación, Bases de Datos, Ingeniería de Software).

---

## 🗺️ Ruta de Aprendizaje Completa

---

## 📂 TEMA 1: Algoritmos y Pseudocódigo

### 1.1 ¿Qué es un Algoritmo?

Un **algoritmo** es una secuencia finita y ordenada de pasos lógicos que, dado un conjunto de datos de entrada, produce un resultado de salida, resolviendo un problema específico.

**Las 5 características que TODO algoritmo debe cumplir:**

| Característica | Significa que... |
|---|---|
| **Finito** | Debe terminar en algún momento, en un número determinado de pasos |
| **Definido (preciso)** | Cada paso debe estar claramente especificado, sin ambigüedad de interpretación |
| **Tiene entrada** | Recibe cero o más datos del exterior |
| **Tiene salida** | Produce al menos un resultado relacionado con la entrada |
| **Efectivo** | Cada paso debe poder ejecutarse exactamente, en tiempo finito, sin necesitar "intuición" |

> Un algoritmo NO es lo mismo que un programa: el algoritmo es la idea/lógica (independiente del lenguaje), el programa es su implementación concreta en un lenguaje como Python, C++ o Java.

### 1.2 Fases para Resolver un Problema Computacional

```
1. Análisis del problema    → ¿Qué datos tengo? ¿Qué necesito obtener?
2. Diseño del algoritmo     → Pseudocódigo / Diagrama de flujo
3. Codificación             → Traducir el algoritmo a un lenguaje de programación
4. Prueba y depuración      → Ejecutar con distintos casos, corregir errores (debugging)
5. Documentación            → Comentar el código, explicar la lógica
6. Mantenimiento            → Actualizar el programa ante nuevos requisitos
```

### 1.3 Pseudocódigo

El **pseudocódigo** es un lenguaje intermedio entre el español/inglés natural y un lenguaje de programación real. No tiene una sintaxis estricta, pero sí convenciones ampliamente usadas:

```
ALGORITMO SumaDeDosNumeros
    Inicio
        Definir a, b, suma Como Entero
        Escribir "Ingrese el primer número:"
        Leer a
        Escribir "Ingrese el segundo número:"
        Leer b
        suma <- a + b
        Escribir "La suma es: ", suma
    Fin
FinAlgoritmo
```

**Palabras clave típicas en pseudocódigo (español):** `Inicio`, `Fin`, `Leer`, `Escribir`, `Si...Entonces...Sino...FinSi`, `Mientras...FinMientras`, `Para...FinPara`, `Definir`, `<-` (asignación).

### 1.4 Diagramas de Flujo (Flowcharts)

Representación gráfica de un algoritmo usando símbolos estandarizados (norma ANSI):

| Símbolo | Forma | Significado |
|---|---|---|
| **Óvalo / Elipse** | ⬭ | Inicio o Fin del algoritmo |
| **Paralelogramo** | ▱ | Entrada de datos (Leer) o Salida (Escribir/Mostrar) |
| **Rectángulo** | ▭ | Proceso: cálculo, asignación de valores |
| **Rombo** | ◇ | Decisión: evalúa una condición y bifurca el flujo (V/F) |
| **Círculo pequeño** | ○ | Conector (une partes separadas del diagrama) |
| **Flecha** | → | Línea de flujo: indica la dirección de ejecución |

**Ejemplo — diagrama de flujo para determinar si un número es par o impar:**
```
   [Inicio]
       ↓
[Leer número N]
       ↓
  ◇ ¿N % 2 == 0? ◇
   /          \
  SÍ           NO
   ↓            ↓
[Escribir   [Escribir
 "Es par"]   "Es impar"]
   ↓            ↓
       [Fin]
```

### 1.5 Variables, Constantes y Tipos de Datos Primitivos

| Tipo de Dato | Descripción | Tamaño típico | Ejemplo |
|---|---|---|---|
| **Entero (int)** | Números sin parte decimal | 4 bytes | `edad = 20` |
| **Flotante (float)** | Números decimales, precisión simple | 4 bytes | `precio = 19.99` |
| **Doble (double)** | Números decimales, precisión doble (más exactos) | 8 bytes | `pi = 3.14159265` |
| **Carácter (char)** | Un solo símbolo | 1-2 bytes | `letra = 'A'` |
| **Cadena (string)** | Secuencia de caracteres | Variable | `nombre = "Juan"` |
| **Booleano (bool)** | Solo dos valores posibles | 1 bit (lógico) | `activo = true` |

- **Variable:** espacio de memoria con un identificador (nombre) cuyo **valor puede cambiar** durante la ejecución del programa.
- **Constante:** espacio de memoria cuyo valor se fija una vez y **no puede modificarse** después (ej: `CONST PI = 3.1416`).

**Reglas comunes para nombrar variables:**
- Deben empezar con una letra o guion bajo (`_`), nunca con un número.
- No pueden contener espacios ni símbolos especiales (`@`, `#`, `%`).
- Son sensibles a mayúsculas/minúsculas (`edad` ≠ `Edad`).
- Deben ser descriptivas: `saldoCuenta` es mejor que `x`.

### 1.6 Operadores

| Categoría | Operadores | Ejemplo | Resultado |
|---|---|---|---|
| **Aritméticos** | `+ - * / %` | `17 % 5` | `2` (resto de la división) |
| **Relacionales** | `== != > < >= <=` | `5 > 3` | `true` |
| **Lógicos** | `AND (&&)` `OR (\|\|)` `NOT (!)` | `(5>3) && (2<4)` | `true` |
| **Asignación** | `= += -= *= /=` | `x += 5` (equivale a `x = x+5`) | — |

**Jerarquía de operadores (precedencia, de mayor a menor):**
1. Paréntesis `()`
2. Multiplicación/División/Módulo `* / %`
3. Suma/Resta `+ -`
4. Relacionales `> < >= <= == !=`
5. Lógicos `&& ||`

> *Ejemplo:* `2 + 3 * 4` se evalúa como `2 + (3*4) = 14`, no como `(2+3)*4 = 20`.

---

## 📂 TEMA 2: Estructuras de Control y Secuenciales

### 2.1 Estructura Secuencial

Es la forma más básica: las instrucciones se ejecutan **una tras otra**, en el orden exacto en que aparecen escritas, sin saltos ni repeticiones, de arriba hacia abajo.

```python
# Ejemplo en Python
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tienes? "))
print(f"Hola {nombre}, el próximo año tendrás {edad + 1} años")
```

### 2.2 Estructuras de Decisión (Selectivas)

**a) Simple (`if`)**

```python
if nota >= 51:
    print("Aprobado")
```

**b) Doble (`if-else`)**

```python
if nota >= 51:
    print("Aprobado")
else:
    print("Reprobado")
```

**c) Múltiple (`if-elif-else` / `switch-case`)**

```python
if nota >= 90:
    letra = "A"
elif nota >= 80:
    letra = "B"
elif nota >= 70:
    letra = "C"
else:
    letra = "F"
```

```c
// switch en C/Java
switch (dia) {
    case 1: printf("Lunes"); break;
    case 2: printf("Martes"); break;
    default: printf("Día inválido");
}
```

**d) Anidada** — un `if` dentro de otro `if`, para evaluar condiciones dependientes:

```python
if edad >= 18:
    if tiene_licencia:
        print("Puede conducir")
    else:
        print("Necesita sacar licencia")
else:
    print("Es menor de edad")
```

### 2.3 Estructuras de Repetición (Iterativas / Bucles)

| Estructura | ¿Cuándo evalúa la condición? | ¿Se ejecuta al menos 1 vez? | Cuándo usarla |
|---|---|---|---|
| **for** | Al inicio, con contador definido | Solo si la condición inicial es verdadera | Se conoce el número exacto de repeticiones |
| **while** | ANTES de cada iteración | No, si la condición es falsa desde el inicio | Repetición controlada por una condición que puede cambiar |
| **do-while** | DESPUÉS de cada iteración | **Sí, siempre al menos una vez** | Cuando se necesita ejecutar el bloque mínimo una vez (ej: menús) |

**Bucle `for`:**
```python
for i in range(1, 11):  # del 1 al 10
    print(i)
```

**Bucle `while`:**
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

**Bucle `do-while` (ejemplo en C, Python no lo tiene nativamente):**
```c
int opcion;
do {
    printf("Menu:\n1. Nuevo\n2. Salir\n");
    scanf("%d", &opcion);
} while (opcion != 2);
```

### 2.4 Control de Flujo dentro de Bucles

- **`break`**: termina el bucle inmediatamente, sin evaluar más iteraciones.
- **`continue`**: salta directamente a la siguiente iteración, sin ejecutar el resto del código de la iteración actual.

```python
for i in range(1, 10):
    if i == 5:
        break          # se detiene completamente al llegar a 5
    if i % 2 == 0:
        continue        # se saltan los pares, sin imprimirlos
    print(i)             # imprime: 1, 3
```

---

## 📂 TEMA 3: Programación Orientada a Objetos (POO)

### 3.1 Clases y Objetos

| Concepto | Definición |
|---|---|
| **Clase** | Plantilla/molde que define atributos (datos) y métodos (comportamientos) comunes |
| **Objeto** | Instancia concreta de una clase, con valores propios en sus atributos |
| **Atributo** | Variable que pertenece a la clase, representa una característica |
| **Método** | Función que pertenece a la clase, representa un comportamiento |
| **Constructor** | Método especial ejecutado automáticamente al crear (instanciar) un objeto |

**Ejemplo completo en Python:**

```python
class Auto:
    def __init__(self, color, velocidad_max):  # Constructor
        self.color = color
        self.velocidad_max = velocidad_max
        self.velocidad_actual = 0

    def acelerar(self, incremento):
        self.velocidad_actual = min(
            self.velocidad_actual + incremento,
            self.velocidad_max
        )

    def frenar(self):
        self.velocidad_actual = 0

# Creación de objetos (instancias)
mi_auto = Auto("rojo", 180)
mi_auto.acelerar(50)
print(f"El auto {mi_auto.color} va a {mi_auto.velocidad_actual} km/h")
```

### 3.2 Los 4 Pilares de la POO

**1. Encapsulamiento** — ocultar los datos internos, exponiendo solo lo necesario mediante métodos públicos (`get`/`set`):

```python
class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # atributo privado (doble guion bajo)

    def get_saldo(self):
        return self.__saldo

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
```

**2. Herencia** — una clase hija reutiliza atributos y métodos de una clase padre:

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    def hacer_sonido(self):
        pass

class Perro(Animal):       # Perro hereda de Animal
    def hacer_sonido(self):
        return "Guau!"

class Gato(Animal):         # Gato hereda de Animal
    def hacer_sonido(self):
        return "Miau!"
```

**3. Polimorfismo** — un mismo método se comporta diferente según el objeto que lo invoque:

```python
animales = [Perro("Rex"), Gato("Michi")]
for a in animales:
    print(f"{a.nombre} dice: {a.hacer_sonido()}")
# Rex dice: Guau!
# Michi dice: Miau!
```

**4. Abstracción** — modelar solo lo relevante de un objeto del mundo real, ocultando la complejidad interna (ej: una clase `Vehiculo` general no necesita saber cómo funciona internamente el motor, solo expone `arrancar()`, `frenar()`, etc.)

### 3.3 Relaciones entre Clases

| Relación | Descripción | Ejemplo | ¿Puede existir independientemente? |
|---|---|---|---|
| **Asociación** | Una clase usa/conoce a otra | `Profesor` conoce a `Estudiante` | Sí, ambas existen aparte |
| **Agregación** | Una clase "tiene" otra, relación más fuerte | `Equipo` tiene `Jugadores` | Sí, el jugador existe sin el equipo |
| **Composición** | Una clase "es dueña" de otra, dependencia total | `Casa` tiene `Habitaciones` | No, la habitación no existe sin la casa |

---

## 📂 TEMA 4: Estructuras de Datos Lineales

### 4.1 Arreglos (Arrays)

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

### 4.2 Estructuras de Datos Dinámicas

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

### 4.3 Comparación: Arreglo vs. Lista Enlazada

| Característica | Arreglo | Lista Enlazada |
|---|---|---|
| Tamaño | Fijo (estático) | Dinámico, crece/decrece en tiempo de ejecución |
| Acceso a un elemento | Directo — O(1) | Secuencial — O(n) |
| Inserción/Eliminación al medio | Costosa, requiere desplazar elementos — O(n) | Eficiente, solo cambia un puntero — O(1) |
| Uso de memoria | Contigua | Dispersa (cada nodo en cualquier parte) |

---

## 📂 TEMA 5: Recursividad y Algoritmos de Búsqueda/Ordenamiento

### 5.1 Recursividad

Una función es **recursiva** cuando se llama a sí misma para resolver una versión más pequeña del mismo problema.

**Elementos obligatorios:**
1. **Caso base:** condición de parada que evita la recursión infinita.
2. **Caso recursivo:** la función se llama a sí misma acercándose siempre al caso base.

```python
def factorial(n):
    if n == 0:              # caso base
        return 1
    else:
        return n * factorial(n - 1)   # caso recursivo

print(factorial(5))   # 120
```

**Traza de ejecución de `factorial(3)`:**
```
factorial(3) = 3 * factorial(2)
             = 3 * (2 * factorial(1))
             = 3 * (2 * (1 * factorial(0)))
             = 3 * (2 * (1 * 1))
             = 6
```

**Otro ejemplo clásico — Fibonacci:**
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

> ⚠️ Cuidado: la recursividad sin un buen caso base provoca **desbordamiento de pila (stack overflow)**.

### 5.2 Algoritmos de Ordenamiento

**Burbuja (Bubble Sort)** — compara elementos adyacentes y los intercambia si están en el orden incorrecto:

```python
def burbuja(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # intercambio
    return arr
```

| Algoritmo | Idea principal | Complejidad promedio |
|---|---|---|
| **Burbuja** | Compara e intercambia adyacentes repetidamente | O(n²) |
| **Selección** | Busca el mínimo y lo coloca en su posición correcta | O(n²) |
| **Inserción** | Inserta cada elemento en su posición dentro de la parte ya ordenada | O(n²) |
| **QuickSort** | Elige un pivote, divide en menores/mayores, ordena recursivamente | O(n log n) |
| **MergeSort** | Divide el arreglo a la mitad recursivamente y luego combina ordenando | O(n log n) |

### 5.3 Algoritmos de Búsqueda

**Búsqueda Lineal** — recorre elemento por elemento:

```python
def busqueda_lineal(arr, objetivo):
    for i, valor in enumerate(arr):
        if valor == objetivo:
            return i
    return -1
```

**Búsqueda Binaria** — requiere que el arreglo esté **ordenado**; descarta la mitad en cada paso:

```python
def busqueda_binaria(arr, objetivo):
    inicio, fin = 0, len(arr) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1
```

| Algoritmo | Requisito | Complejidad |
|---|---|---|
| Búsqueda Lineal | Ninguno | O(n) |
| Búsqueda Binaria | Arreglo ordenado | O(log n) |

---

## 📂 TEMA 6: Archivos y Manejo de Excepciones

### 6.1 Manejo de Archivos

| Tipo | Descripción | Extensiones comunes |
|---|---|---|
| **Texto plano** | Contenido legible directamente, codificado en caracteres | `.txt`, `.csv`, `.json` |
| **Binario** | Contenido en formato de bytes, no legible directamente | `.dat`, imágenes, ejecutables |

**Modos de apertura de archivo:**

| Modo | Significado |
|---|---|
| `r` | Lectura (read) — falla si el archivo no existe |
| `w` | Escritura (write) — crea el archivo o **sobrescribe** su contenido |
| `a` | Append — agrega contenido al final sin borrar lo existente |
| `r+` | Lectura y escritura simultánea |

**Ejemplo en Python:**

```python
# Escribir en un archivo
with open("datos.txt", "w") as archivo:
    archivo.write("Primera línea\n")
    archivo.write("Segunda línea\n")

# Leer un archivo
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

# Agregar al final (append)
with open("datos.txt", "a") as archivo:
    archivo.write("Tercera línea agregada\n")
```

> `with` se usa porque cierra el archivo automáticamente al terminar el bloque, evitando dejar el archivo abierto innecesariamente.

### 6.2 Manejo de Excepciones

Una **excepción** es un evento anómalo que ocurre durante la ejecución e interrumpe el flujo normal del programa (ej: dividir por cero, archivo no encontrado, conversión de tipo inválida).

**Estructura `try-except-finally`:**

```python
try:
    numero = int(input("Ingrese un número: "))
    resultado = 100 / numero
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("Error: no se puede dividir por cero")
except ValueError:
    print("Error: debe ingresar un número válido")
finally:
    print("Este bloque siempre se ejecuta, haya error o no")
```

**Tipos comunes de excepciones:**

| Excepción | Causa |
|---|---|
| `ZeroDivisionError` | División por cero |
| `IndexError` | Acceso a un índice fuera de rango en un arreglo/lista |
| `FileNotFoundError` | El archivo que se intenta abrir no existe |
| `ValueError` | Conversión de tipos inválida (ej: `int("abc")`) |
| `TypeError` | Operación entre tipos incompatibles (ej: `"5" + 5`) |

> El bloque `finally` es clave para liberar recursos (como cerrar un archivo o una conexión), ya que se ejecuta **siempre**, sin importar si hubo error o no.

---

## 🎯 Ponderación y Control de Calificaciones

| Actividad Evaluativa | Ponderación | Nota Obtenida |
|---|---|---|
| **Examen Primer Parcial** | 30% | `__ / 100` |
| **Examen Segundo Parcial** | 30% | `__ / 100` |
| **Examen Final / Proyecto** | 30% | `__ / 100` |
| **Tareas y Prácticas** | 10% | `__ / 100` |
| **Nota Final** | **100%** | **`__ / 100`** |

---

## 📅 Cronograma de Fechas Importantes

- [ ] **Examen Primer Parcial:** *Fecha: **/**/*________
- [ ] **Examen Segundo Parcial:** *Fecha: **/**/*________
- [ ] **Entrega de Proyecto/Trabajo Final:** *Fecha: **/**/*________
- [ ] **Examen Final:** *Fecha: **/**/*________

---

## 📂 Archivos en esta Carpeta

- 📁 Examen 1er Parcial Informática I Unior2017

---

*Documento enriquecido para el control de estudios del Ing. José Luis Choquevilca — UNIOR 2017*
