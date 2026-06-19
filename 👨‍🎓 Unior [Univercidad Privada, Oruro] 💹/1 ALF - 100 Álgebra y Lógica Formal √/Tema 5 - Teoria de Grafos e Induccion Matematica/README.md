# Tema 5: Teoría de Grafos e Inducción Matemática
## 🏫 Materia: Álgebra y Lógica Formal (ALF-100)

---

### 📚 Apuntes y Conceptos Clave
##### 5.1 Conceptos Básicos de Grafos

Un **grafo** $G=(V,E)$ está formado por un conjunto de **vértices** (V) y un conjunto de **aristas** (E) que conectan pares de vértices.

| Tipo de Grafo | Descripción |
|---|---|
| **No dirigido** | Las aristas no tienen dirección (A-B = B-A) |
| **Dirigido (dígrafo)** | Las aristas tienen dirección (A→B ≠ B→A) |
| **Ponderado** | Las aristas tienen un peso/costo asociado |
| **Simple** | Sin lazos ni aristas múltiples entre el mismo par de vértices |
| **Completo ($K_n$)** | Todos los vértices están conectados entre sí; tiene $\frac{n(n-1)}{2}$ aristas |
| **Bipartito** | Los vértices se dividen en dos grupos, y las aristas solo conectan vértices de grupos distintos |

##### 5.2 Conceptos Clave y Fórmulas

- **Grado de un vértice** $\deg(v)$: número de aristas que llegan o salen de él.
- **Teorema de la suma de grados:** $\sum \deg(v) = 2|E|$ (la suma de todos los grados es el doble del número de aristas, porque cada arista se cuenta dos veces).
- **Camino:** secuencia de vértices conectados por aristas, sin repetir vértices.
- **Ciclo:** camino que empieza y termina en el mismo vértice.
- **Grafo conexo:** existe un camino entre cualquier par de vértices.

##### 5.3 Representación Matricial de Grafos

**Matriz de adyacencia** para el grafo: A-B, A-C, B-C

| | A | B | C |
|---|---|---|---|
| **A** | 0 | 1 | 1 |
| **B** | 1 | 0 | 1 |
| **C** | 1 | 1 | 0 |

> Este es un grafo completo $K_3$ (triángulo): todos conectados entre sí. Grado de cada vértice = 2. Suma de grados = 6 = 2×3 aristas ✓ (cumple el teorema).

##### 5.4 Inducción Matemática

**Los 3 pasos formales:**
1. **Caso base:** demostrar para $n=1$ (o el primer valor del dominio).
2. **Hipótesis inductiva:** suponer verdadero para $n=k$.
3. **Paso inductivo:** demostrar que, a partir de la hipótesis, también es verdadero para $n=k+1$.

> *Ejemplo resuelto completo:* Demostrar que $1+2+3+\dots+n = \frac{n(n+1)}{2}$ para todo $n\geq1$.
>
> **Caso base ($n=1$):** $1 = \frac{1(1+1)}{2} = \frac{2}{2} = 1$ ✓
>
> **Hipótesis inductiva:** suponemos que $1+2+\dots+k = \frac{k(k+1)}{2}$ es verdadero.
>
> **Paso inductivo:** demostrar para $n=k+1$:
> $$1+2+\dots+k+(k+1) = \frac{k(k+1)}{2}+(k+1)$$
> $$= \frac{k(k+1)+2(k+1)}{2} = \frac{(k+1)(k+2)}{2}$$
> Esto es exactamente la fórmula con $n=k+1$. ✓ Queda demostrado para todo $n$.

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