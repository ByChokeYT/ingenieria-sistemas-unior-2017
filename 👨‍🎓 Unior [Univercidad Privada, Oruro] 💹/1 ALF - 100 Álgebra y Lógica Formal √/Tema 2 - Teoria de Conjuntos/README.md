# Tema 2: Teoría de Conjuntos
## 🏫 Materia: Álgebra y Lógica Formal (ALF-100)

---

### 📚 Apuntes y Conceptos Clave
##### 2.1 Definición de Conjuntos

Un **conjunto** es una colección bien definida de objetos (elementos), sin importar el orden ni repeticiones.

| Forma de definir | Notación | Ejemplo |
|---|---|---|
| **Por extensión** | Se listan los elementos | A = {2, 4, 6, 8} |
| **Por comprensión** | Se describe una propiedad que cumplen los elementos | A = {x \| x es par, 0<x<10} |

**Notación:** $a \in A$ (a pertenece a A); $a \notin A$ (a no pertenece a A); $A \subseteq B$ (A es subconjunto de B); $|A|$ (cardinalidad: número de elementos de A).

##### 2.2 Tipos de Conjuntos

| Tipo | Descripción | Ejemplo |
|---|---|---|
| Vacío | No tiene elementos | ∅ = {} |
| Unitario | Tiene un solo elemento | {5} |
| Finito | Número limitado de elementos | {1,2,3} |
| Infinito | Número ilimitado de elementos | ℕ = {1,2,3,...} |
| Universal | Contiene a todos los elementos del contexto en estudio | U |
| Disjuntos | Dos conjuntos sin elementos en común | A∩B = ∅ |

##### 2.3 Conjunto Potencia

El **conjunto potencia** $P(A)$ es el conjunto formado por TODOS los subconjuntos posibles de A, incluyendo el conjunto vacío y A mismo.

$$|P(A)| = 2^n \text{, donde } n = |A|$$

> *Ejemplo resuelto:* Si A = {1, 2, 3}, entonces $n=3$ y $|P(A)| = 2^3 = 8$.
>
> $P(A) = \{\emptyset, \{1\}, \{2\}, \{3\}, \{1,2\}, \{1,3\}, \{2,3\}, \{1,2,3\}\}$

##### 2.4 Operaciones entre Conjuntos (con ejemplos resueltos)

Sea $U = \{1,2,3,4,5,6,7,8,9,10\}$, $A=\{1,2,3,4,5\}$, $B=\{4,5,6,7,8\}$

| Operación | Símbolo | Definición | Resultado del ejemplo |
|---|---|---|---|
| **Unión** | A ∪ B | Elementos en A o en B (o ambos) | {1,2,3,4,5,6,7,8} |
| **Intersección** | A ∩ B | Elementos en A y en B | {4,5} |
| **Diferencia** | A − B | Elementos en A pero no en B | {1,2,3} |
| **Diferencia** | B − A | Elementos en B pero no en A | {6,7,8} |
| **Complemento** | A' | Elementos del universo que no están en A | {6,7,8,9,10} |
| **Diferencia simétrica** | A △ B | (A∪B) − (A∩B) | {1,2,3,6,7,8} |

##### 2.5 Leyes de De Morgan para Conjuntos

$$(A \cup B)' = A' \cap B'$$
$$(A \cap B)' = A' \cup B'$$

> *Verificación con el ejemplo anterior:*
> $A' = \{6,7,8,9,10\}$, $B' = \{1,2,3,9,10\}$
> $A' \cap B' = \{9,10\}$
> $(A\cup B)' = \{1,...,8\}' = \{9,10\}$ ✓ Coinciden, la ley se cumple.

##### 2.6 Producto Cartesiano

$$A \times B = \{(a,b) \mid a \in A, b \in B\}$$

> *Ejemplo:* Si A={1,2} y B={x,y}, entonces:
> $A \times B = \{(1,x),(1,y),(2,x),(2,y)\}$ → tiene $|A| \times |B| = 2\times2=4$ pares ordenados.

##### 2.7 Diagramas de Venn — Representación Gráfica

```
        U
   ┌─────────────────┐
   │   A        B     │
   │ ┌───┐    ┌───┐   │
   │ │ 1 │┌──┐│ 6 │   │
   │ │ 2 ││4,5││ 7 │   │
   │ │ 3 │└──┘│ 8 │   │
   │ └───┘    └───┘   │
   │      9, 10        │
   └─────────────────┘
```
La zona compartida entre los dos círculos representa $A \cap B = \{4,5\}$.

---

##### 📑 Banco de Preguntas (Auto-Evaluación)
1. **¿Qué es el conjunto potencia y cuántos elementos tiene el conjunto potencia de $A = \{a, b, c\}$?**
   * *Respuesta:* Es el conjunto formado por todos los subconjuntos de $A$. Tiene $2^3 = 8$ elementos: $\{\emptyset, \{a\}, \{b\}, \{c\}, \{a,b\}, \{a,c\}, \{b,c\}, \{a,b,c\}\}$.
2. **Defina la diferencia simétrica entre dos conjuntos $A$ y $B$.**
   * *Respuesta:* Es el conjunto de elementos que pertenecen a $A$ o a $B$, pero no a ambos a la vez ($A \Delta B = (A \cup B) - (A \cap B)$).
3. **Si el universo es $U = \{1, 2, 3, 4, 5\}$ y $A = \{1, 3, 5\}$, halle el complemento de $A$ ($A\prime$).**
   * A) $\{2, 4\}$
   * B) $\{1, 3, 5\}$
   * C) $\emptyset$
   * D) $\{1, 2, 3, 4, 5\}$
   * *Respuesta correcta:* A) $\{2, 4\}$.
4. **Enuncie una de las Leyes de De Morgan aplicadas a conjuntos.**
   * *Respuesta:* $(A \cup B)\prime = A\prime \cap B\prime$ o $(A \cap B)\prime = A\prime \cup B\prime$.

---

### ✍️ Mis Resúmenes y Notas de Clase
*Haz doble clic en este archivo para registrar tus notas, fórmulas o resúmenes de las clases del docente.*

---

### 📂 Archivos y Tareas de esta Unidad
*Arrastra tus prácticas, códigos o diapositivas a esta carpeta para organizarlas aquí.*

---
*Documento autogenerado para el control de estudios del Ing. José Luis Choquevilca - UNIOR*