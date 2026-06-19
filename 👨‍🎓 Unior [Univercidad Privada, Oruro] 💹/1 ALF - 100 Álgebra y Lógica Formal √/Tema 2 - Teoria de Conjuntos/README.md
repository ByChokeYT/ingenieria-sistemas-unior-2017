# Tema 2: Teoría de Conjuntos
## 🏫 Materia: Álgebra y Lógica Formal (ALF-100)

---

### 📚 Apuntes y Conceptos Clave
##### 2.1 Definición de Conjuntos

Un **conjunto** es una colección bien definida de objetos llamados elementos.

| Forma de definir | Notación | Ejemplo |
|---|---|---|
| **Por extensión** | Se listan los elementos | A = {2, 4, 6, 8} |
| **Por comprensión** | Se describe una propiedad | A = {x \| x es par, 0<x<10} |

**Notación de pertenencia:** $a \in A$ (a pertenece a A), $a \notin A$ (a no pertenece a A).

##### 2.2 Tipos de Conjuntos

| Tipo | Descripción | Ejemplo |
|---|---|---|
| Vacío | No tiene elementos | ∅ o {} |
| Unitario | Tiene un solo elemento | {5} |
| Finito | Número limitado de elementos | {1,2,3} |
| Infinito | Número ilimitado de elementos | Números naturales ℕ |
| Universal | Contiene a todos los elementos del contexto | U |

##### 2.3 Conjunto Potencia

El **conjunto potencia** P(A) es el conjunto de todos los subconjuntos posibles de A, incluyendo el vacío y A mismo.

$$|P(A)| = 2^n \text{, donde } n = |A|$$

> *Ejemplo:* Si A = {1, 2}, entonces P(A) = {∅, {1}, {2}, {1,2}} → tiene $2^2=4$ elementos.

##### 2.4 Operaciones entre Conjuntos

| Operación | Símbolo | Definición | Diagrama de Venn |
|---|---|---|---|
| **Unión** | A ∪ B | Elementos en A o en B (o ambos) | Ambos círculos sombreados |
| **Intersección** | A ∩ B | Elementos en A y en B | Solo zona compartida |
| **Diferencia** | A − B | Elementos en A pero no en B | Solo A, sin la parte de B |
| **Complemento** | A' o Aᶜ | Elementos del universo que no están en A | Todo excepto A |
| **Diferencia simétrica** | A △ B | Elementos en A o B, pero no en ambos | (A∪B) − (A∩B) |

##### 2.5 Propiedades de las Operaciones

- **Leyes de De Morgan:** $(A \cup B)' = A' \cap B'$ ; $(A \cap B)' = A' \cup B'$
- **Distributivas:** $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$
- **Conmutativas:** $A \cup B = B \cup A$
- **Asociativas:** $(A \cup B) \cup C = A \cup (B \cup C)$

##### 2.6 Producto Cartesiano

$$A \times B = \{(a,b) \mid a \in A, b \in B\}$$

> *Ejemplo:* Si A={1,2} y B={x,y}, entonces A×B = {(1,x),(1,y),(2,x),(2,y)}

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