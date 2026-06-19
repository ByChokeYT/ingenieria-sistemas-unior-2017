# Tema 5: Teoría de Grafos e Inducción Matemática
## 🏫 Materia: Álgebra y Lógica Formal (ALF-100)

---

### 📚 Apuntes y Conceptos Clave
##### 5.1 Conceptos Básicos de Grafos

Un **grafo** G = (V, E) está formado por un conjunto de **vértices** (V) y un conjunto de **aristas** (E) que conectan pares de vértices.

| Tipo de Grafo | Descripción |
|---|---|
| **No dirigido** | Las aristas no tienen dirección (A-B = B-A) |
| **Dirigido (dígrafo)** | Las aristas tienen dirección (A→B ≠ B→A) |
| **Ponderado** | Las aristas tienen un peso o costo asociado |
| **Simple** | Sin lazos ni aristas múltiples entre el mismo par de vértices |
| **Completo** | Todos los vértices están conectados entre sí |

##### 5.2 Conceptos Clave

- **Grado de un vértice:** número de aristas que llegan o salen de él.
- **Camino:** secuencia de vértices conectados por aristas, sin repetir vértices.
- **Ciclo:** camino que empieza y termina en el mismo vértice.
- **Conectividad:** un grafo es conexo si existe un camino entre cualquier par de vértices.

##### 5.3 Representación Matricial de Grafos

**Matriz de adyacencia:** matriz $n \times n$ donde la celda $(i,j) = 1$ si existe arista entre el vértice $i$ y el vértice $j$, y $0$ si no.

| | A | B | C |
|---|---|---|---|
| **A** | 0 | 1 | 1 |
| **B** | 1 | 0 | 0 |
| **C** | 1 | 0 | 0 |

> Este grafo de ejemplo tiene a A conectado con B y con C, pero B y C no están conectados entre sí.

##### 5.4 Inducción Matemática

La **inducción matemática** es un método de demostración para afirmaciones que dependen de un número natural $n$.

**Pasos del principio de inducción:**

1. **Caso base:** demostrar que la afirmación es verdadera para $n=1$ (o el primer valor del dominio).
2. **Paso inductivo:** suponer que es verdadera para $n=k$ (hipótesis inductiva) y demostrar que entonces también es verdadera para $n=k+1$.
3. **Conclusión:** si ambos pasos se cumplen, la afirmación es verdadera para todo $n$ natural.

> *Ejemplo clásico:* demostrar que $1+2+3+\dots+n = \frac{n(n+1)}{2}$ para todo $n \geq 1$, verificando el caso base $n=1$ y luego el paso inductivo de $k$ a $k+1$.

---

##### 📑 Banco de Preguntas (Auto-Evaluación)
1. **¿Qué diferencia a un grafo dirigido (dígrafo) de uno no dirigido?**
   * *Respuesta:* En el grafo dirigido, las aristas tienen una dirección definida (de un origen a un destino, representadas con flechas); en el no dirigido, las conexiones no tienen sentido de orientación.
2. **Explique los dos pasos esenciales del método de demostración por Inducción Matemática.**
   * *Respuesta:* 1. Caso base: se prueba que la proposición es válida para el menor elemento del conjunto (ej: $n=1$). 2. Paso inductivo: se asume que es cierta para $n=k$ (hipótesis inductiva) y se demuestra que entonces también es cierta para $n=k+1$.
3. **¿Qué representa la matriz de adyacencia de un grafo?**
   * *Respuesta:* Una matriz cuadrada donde la posición $(i,j)$ vale 1 si existe una arista que conecta al vértice $i$ con el vértice $j$, y 0 en caso contrario.
4. **Un grafo conexo que no tiene ciclos se denomina:**
   * A) Dígrafo completo
   * B) Árbol
   * C) Grafo bipartito
   * D) Bucle
   * *Respuesta correcta:* B) Árbol.

---

### ✍️ Mis Resúmenes y Notas de Clase
*Haz doble clic en este archivo para registrar tus notas, fórmulas o resúmenes de las clases del docente.*

---

### 📂 Archivos y Tareas de esta Unidad
*Arrastra tus prácticas, códigos o diapositivas a esta carpeta para organizarlas aquí.*

---
*Documento autogenerado para el control de estudios del Ing. José Luis Choquevilca - UNIOR*