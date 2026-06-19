# Tema 5: Recursividad y Algoritmos de Búsqueda/Ordenamiento
## 🏫 Materia: Informática I (INF-100)

---

### 📚 Apuntes y Conceptos Clave
##### 5.1 Recursividad

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

##### 5.2 Algoritmos de Ordenamiento

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

##### 5.3 Algoritmos de Búsqueda

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

##### 📑 Banco de Preguntas (Auto-Evaluación)
1. **¿Qué es la recursividad y por qué es fundamental definir un "caso base"?**
   * *Respuesta:* La recursividad es una técnica donde una función se llama a sí misma para resolver subproblemas. El caso base es fundamental porque detiene las llamadas recursivas y evita un bucle infinito de desbordamiento de pila (stack overflow).
2. **¿Cómo funciona el algoritmo de búsqueda binaria y qué requisito indispensable exige del arreglo?**
   * *Respuesta:* Divide el espacio de búsqueda por la mitad repetidamente comparando con el elemento central. Requiere obligatoriamente que el arreglo esté ordenado previamente.
3. **¿Cuál de los siguientes algoritmos de ordenamiento tiene la mejor eficiencia promedio ($O(n \log n)$)?**
   * A) Ordenamiento Burbuja (BubbleSort)
   * B) Ordenamiento por Inserción (InsertionSort)
   * C) Ordenamiento Rápido (QuickSort)
   * D) Búsqueda Lineal
   * *Respuesta correcta:* C) Ordenamiento Rápido (QuickSort).
4. **Explique el funcionamiento básico del ordenamiento Burbuja.**
   * *Respuesta:* Compara elementos adyacentes y los intercambia si están en el orden incorrecto. Repite este proceso recorriendo la lista varias veces hasta que no se necesiten más intercambios.

---

### ✍️ Mis Resúmenes y Notas de Clase
*Haz doble clic en este archivo para registrar tus notas, fórmulas o resúmenes de las clases del docente.*

---

### 📂 Archivos y Tareas de esta Unidad
*Arrastra tus prácticas, códigos o diapositivas a esta carpeta para organizarlas aquí.*

---
*Documento autogenerado para el control de estudios del Ing. José Luis Choquevilca - UNIOR*